HAS_TABLE_OF_CONTENTS = """Reply with 'yes' if the provided text exhibits characteristics commonly found in lists of contents, such as variations in numbering or lettering formats like numbers, letters, Roman numerals, etc., or includes keywords like "Table of Contents" or "Contents". Consider hierarchical structures, patterns, and mixed formats of list items to distinguish between regular headings and a list of contents. If unsure, provide feedback on why the text may or may not be a list of contents.
Excerpt:
{excerpt}
Response:"""

EXTRACT_PAGES = """Given a chunk of the Table of Contents from a PDF, extract the title of the contents, the start page, and the end page of each entry in a consistent format. Ensure that the page ranges are standardized with hyphens. Differentiate between hierarchical and non-hierarchical entries. Support alphanumeric characters and Roman numerals in entries. Skip or flag missing/incomplete entries for review. Handle nested levels by indenting or numbering sub-level entries for clarity.
---
Example 1:
Section 1, 5-5
Section 2, 6-6
Section 3, 7-8
Output:
Section 1, 5, 5
Section 2, 6, 6
Section 3, 7, 8
---
Example 2:
I. Heading 1, 5-5
A. Heading 2, 6-6
1. Heading 3, 7-8
Output:
Heading 1, 5, 5
Heading 2, 6, 6
Heading 3, 7, 8
---
where the first column is the title of the contents along with the unique identifier, the second column is the start page of the contents, and the third column is the end page of the contents.
Excerpt:
{excerpt}
---
For each heading, start a new line with the unique heading.
Response:"""

GET_RELEVANT_PAGES = """As an advanced language model your job is to figure out which section contains the user requested information.
You are given a list of table of contents along with the start and end page numbers of each section.
For the user query, output the start and end page numbers, as a tuple, that contain the information.
Respect the hirerachy and consider all the sub-sections nested within the section that contain the information.
Example:
User Query:
What is the definition of a llama?
Expected response:
(1, 5)
---
Table of Contents:
{contents}
---
Based on the table of contents above, output the start and end page numbers that contain the information.
User Query:
{query}
Response:"""