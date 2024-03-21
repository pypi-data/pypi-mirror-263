HAS_TABLE_OF_CONTENTS = """Reply with 'yes' if the attached excerpt from a PDF contains list of contents, and 'no' otherwise.
Excerpt:
{excerpt}
Response:"""

EXTRACT_PAGES = """Given an excerpt from a PDF, if you see contents listed with the page number in a table format, output the title of the contents and the start page and the end page of the contents.
Example:
1.1.5 Heading 1, 5, 5
1.1.6 Heading 2, 6, 6
1.1.7 Heading 3, 7, 8
where the first column is the title of the contents along with the unique identifier, the second column is the start page of the contents, and the third column is the end page of the contents.
Excerpt:
{excerpt}
---
For each heading, start a new line with the unique heading.
Response:"""