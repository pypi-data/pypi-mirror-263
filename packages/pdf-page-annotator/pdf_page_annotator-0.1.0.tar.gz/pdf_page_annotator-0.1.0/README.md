# pdf-page-annotator
A light weight library to extract the table of contents and tag them to the pages containing the content.

To understand the structure of a PDF and for effective retrieval, it is important to understand the contents and know exactly 
what page contains what.

When the need to extract a specific subsection of the pdf comes up, it can be found in either of the two places--
1. In a section of a semi-structured (one with a structure and TOC) document.
2. In an unknown section or in a fragmented form inside an unstructured document.

For the more extreme case of unstructured document, we have to perform an analysis on the whole document. Each time we want to find some informationin an exhaustive fashion (Because naive vector retrieval can't do that).

So, for the semi-structured documents, conventionally all important PDF documents worth indexing have a TOC, we can perform an initial
TOC sweep, and extract relevant page numbers for each TOC item. In this manner, when we have to search for something exhaustively, 
instead of having to sesrch through the whole document, we can only search through the TOC to find the relevant pages, and then 
extract information from only those pages, saving time and tokens.

## Installation

```python
pip install pdf-page-annotator
```

## Usage

1. Import and initialize the PDFAnnotator class

```python
from pdf_page_annotator import PDFAnnotator
annotator = PDFAnnotator(pdf_path="path_to_your_pdf_file", verbose=True) # `verbose=True` logs progress on the console, default is `False`
```

2. Extract the contents

```python
annotator.run_extraction_pipeline()
```

3. Access the content list

```python
print(annotator.content[0].unique_title, annotator.content[0].start_page, annotator.content[0].end_page)
```

Enjoy!