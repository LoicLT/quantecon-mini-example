# Configuration file for the Sphinx documentation builder.
# Generated from mini_book/_config.yml
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
# Based on mini_book/_config.yml

project = 'Scientific Python QuickStart'
copyright = '2024, Thomas J. Sargent and John Stachurski'
author = 'Thomas J. Sargent and John Stachurski'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
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
    'sphinx.ext.imgconverter',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# Based on mini_book/_config.yml html settings

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', '../mini_book/_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
html_sidebars = {}

# HTML-specific settings from _config.yml
html_title = 'Scientific Python QuickStart'
html_short_title = 'Scientific Python QuickStart'

# -- Options for LaTeX output ------------------------------------------------
# Based on mini_book/_config.yml latex settings

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    \usepackage{amsmath}
    \usepackage{amsfonts}
    \usepackage{amssymb}
    ''',

    # Latex figure (float) alignment
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'book.tex', 'Scientific Python QuickStart Documentation',
     'Thomas J. Sargent and John Stachurski', 'manual'),
]

# LaTeX engine from _config.yml
latex_engine = 'xelatex'

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'scientificpythonquickstart', 'Scientific Python QuickStart Documentation',
     [author], 1)
]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'ScientificPythonQuickStart', 'Scientific Python QuickStart Documentation',
     author, 'ScientificPythonQuickStart', 'A brief introduction to Python programming for scientific applications.',
     'Miscellaneous'),
]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# -- Bibliography configuration -----------------------------------------------
# Based on mini_book/_config.yml bibtex_bibfiles

bibtex_bibfiles = ['../mini_book/_bibliography/references.bib']

# -- Repository and Binder configuration -------------------------------------
# Based on mini_book/_config.yml repository and binder settings

# Repository information
repository_url = 'https://github.com/executablebooks/quantecon-mini-example'
repository_path = 'mini_book'

# Binder configuration
binderhub_url = 'https://mybinder.org'
binder_text = 'Launch binder'

# -- Math configuration ------------------------------------------------------

# MathJax configuration
mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML'
mathjax_config = {
    'TeX': {
        'Macros': {
            'RR': '{\\mathbb{R}}',
            'NN': '{\\mathbb{N}}',
            'ZZ': '{\\mathbb{Z}}',
            'QQ': '{\\mathbb{Q}}',
            'CC': '{\\mathbb{C}}',
        }
    }
}

# -- Image configuration ------------------------------------------------------

# Image converter settings
image_converter = 'Pillow'
image_converter_args = ['-quality', '85']

# -- Additional Sphinx configuration ----------------------------------------

# Suppress warnings
suppress_warnings = ['image.nonlocal_uri']

# Enable numbered figures
numfig = True
