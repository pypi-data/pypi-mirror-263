import logging

from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from pypdf import PdfReader

from .preprocess import remove_double_spaces
from .prompts import EXTRACT_PAGES, HAS_TABLE_OF_CONTENTS

load_dotenv()

class ContentItem:
    def __init__(
        self,
        unique_title: str,
        start_page: int,
        end_page: int
    ):
        self.unique_title = unique_title
        self.start_page = start_page
        self.end_page = end_page

class PDFAnnotator:

    def __init__(
        self,
        pdf_path: str,
        llm: OpenAI = OpenAI(model="gpt-3.5-turbo"),
        verbose = False
    ):
        self.llm = llm
        self.reader = PdfReader(pdf_path)
        self.annotation_state = {
            "started": False,
            "finished": False,
            "current_page": 0,
            "toc_pages": [],
        }
        self.contents = []
        if verbose:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.INFO)
            self.logger.addHandler(logging.StreamHandler())
        else:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(logging.WARNING)
            self.logger.addHandler(logging.StreamHandler())
        self.verbose = verbose
        self.chunks = []
        self.logger.info(f"Initialized PDFAnnotator with {pdf_path}")

    def run_extraction_pipeline(self) -> None:
        self.get_toc()
        self.extract_contents()

    def get_toc(self) -> None:
        self._get_toc()
        return self.annotation_state["toc_pages"]

    def _get_toc(self) -> None:
        if self.annotation_state["finished"]:
            return
        if not self.annotation_state["started"]:
            self._start_annotation()
        self._continue_annotation()

    def _start_annotation(self) -> None:
        if self.annotation_state["finished"]:
            return
        self.annotation_state["started"] = True
        self._continue_annotation()

    def _continue_annotation(self) -> None:
        if self.annotation_state["finished"]:
            return
        if self.annotation_state["current_page"] < len(self.reader.pages):
            self._annotate_page()
        else:
            self.annotation_state["finished"] = True

    def _annotate_page(self) -> None:
        self.logger.info(f"Page {self.annotation_state['current_page']} ...")
        page = self.reader.pages[self.annotation_state["current_page"]]
        text = page.extract_text(extraction_mode="layout")
        text = remove_double_spaces(text)
        response = self.llm.complete(HAS_TABLE_OF_CONTENTS.format(excerpt=text)).text
        if "yes" in response.lower():
            self.annotation_state["toc_pages"].append(self.annotation_state["current_page"])
        else:
            # if the response is no, and we have already found the table of contents, we can stop
            # assuming that the toc is continuous
            if len(self.annotation_state["toc_pages"]) > 0:
                self.annotation_state["finished"] = True
                self.logger.info("Finished annotating table of contents")
        self.annotation_state["current_page"] += 1
        self._continue_annotation()

    def extract_contents(self) -> None:
        if not self.annotation_state["finished"]:
            self._get_toc()
        return self._extract_contents()
    
    def _extract_contents(self) -> str:
        self.logger.info("Extracting contents ...")
        chunks = []
        for i, page in enumerate(self.annotation_state["toc_pages"]):
            self.logger.info(f"Extracting contents from page {page} ...")
            text = self.reader.pages[page].extract_text(extraction_mode="layout")
            lines = [line.strip() for line in text.split("\n") if line.strip()]
            lines = [remove_double_spaces(line) for line in lines if line.strip()]
            for j in range(0, len(lines), 10):
                chunk = "\n".join(lines[j:j+10])
                chunks.append(chunk)
        self.logger.info("Extracted contents")
        self.chunks = chunks
        for chunk in chunks:
            self.logger.info(f"Extracting contents from chunk ...")
            response = self.llm.complete(EXTRACT_PAGES.format(excerpt=chunk)).text
            lines = response.split("\n")
            for line in lines:
                parts = line.split(", ")
                if len(parts) == 3:
                    self.contents.append(ContentItem(parts[0], int(parts[1]), int(parts[2])))
        return self.contents

if __name__ == "__main__":
    pdf_path = "doefund.pdf"
    annotator = PDFAnnotator(pdf_path, verbose=True)
    annotator.run_extraction_pipeline()
    content = annotator.contents
    # save into a file
    with open("contents.txt", "w") as f:
        for line in content:
            f.write(", ".join(line) + "\n")
