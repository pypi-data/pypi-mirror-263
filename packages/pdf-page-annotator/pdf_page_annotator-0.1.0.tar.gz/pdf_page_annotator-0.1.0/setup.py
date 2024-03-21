from setuptools import setup, find_packages

setup(
    name='pdf_page_annotator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        "llama_index",
        "pypdf",
        "python-dotenv",
    ],
    # Additional metadata about your package.
    author='Chinmay Shrivastava',
    author_email='cshrivastava99@gmail.com',
    description='A light weight library to extract the table of contents and tag them to the pages containing the content.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ChinmayShrivastava/pdf-page-annotator',
    license='GPLv3',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
        "Environment :: X11 Applications",
    ],
    entry_points={},
)