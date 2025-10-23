# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Scientific Python QuickStart'
copyright = '2025, Thomas J. Sargent and John Stachurski'
author = 'Thomas J. Sargent and John Stachurski'

version = '1.0.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.imgmath',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', '../mini_book/_static']

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- Additional configuration for ReadTheDocs --------------------------------

# Bibliography support
bibtex_bibfiles = ['../mini_book/_bibliography/references.bib']

# LaTeX configuration
latex_engine = 'xelatex'
latex_documents = [
    ('index', 'book.tex', 'Scientific Python QuickStart Documentation',
     'Thomas J. Sargent and John Stachurski', 'manual'),
]

# Math configuration
mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# ReadTheDocs specific settings
if 'READTHEDOCS' in os.environ:
    html_context = {
        'display_github': True,
        'github_user': 'executablebooks',
        'github_repo': 'quantecon-mini-example',
        'github_version': 'master',
        'conf_py_path': '/docs/',
    }
