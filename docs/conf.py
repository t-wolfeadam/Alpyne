# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "..")))


# -- Project information -----------------------------------------------------

project = "Alpyne"
copyright = "2024, AnyLogic North America, LLC"
author = "Tyler Wolfe-Adam"

# The short X.Y version
version = "1.0"

# The full version, including alpha/beta/rc tags
release = "1.0.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_rtd_theme',
    'sphinx.ext.githubpages',
    'enum_tools.autoenum',
    'rst2pdf.pdfbuilder'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "./_static/alpyne_logo_3.png"

# -- Extension configuration -------------------------------------------------

## rst2pdf settings
pdf_documents = [('index', u'alpyne-doc', u'Alpyne Documentation', u'Tyler Wolfe-Adam'),]
pdf_toc_depth = 2
# If false, no index is generated, default True.
pdf_use_index = True
# If false, no modindex is generated, default True.
pdf_use_modindex = False
# If false, no coverpage is generated, default True.
pdf_use_coverpage = False
pdf_stylesheets = ['sphinx', 'a4']
pdf_style_path = ['.', '_styles']

## Autodoc settings
autodoc_default_options = {
    'member-order': 'bysource',
}

autodoc_typehints = 'both'

autodoc_type_aliases = {
    'EngineSettingKeys': 'alpyne.typing.EngineSettingKeys',
    'Number': 'alpyne.typing.Number',
    'OutputType': 'alpyne.typing.OutputType'
}

autoclass_content = 'both'

## Sphinx_RTD_Theme settings
## https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    #'canonical_url': '',
    #'analytics_id': 'UA-XXXXXXX-1',  #  (Provided by Google in your dashboard)
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom', # (alts: bottom, top, both, None)
    'style_external_links': True, # (default: False)
    #'vcs_pageview_mode': '',
    'style_nav_header_background': '#1e9bd8', # (Can be any valid CSS background property)
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 8,
    'includehidden': True,
    'titles_only': False
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False
