# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'EDPS'
copyright = '2025, ESO'
author = 'Lodovico Coccato'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = []
numfig = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']
html_css_files = ['lightbox.css']
html_js_files = ['lightbox.js']
html_theme_options = {
    "body_max_width": "none",
    "primary_sidebar_end": ["indices.html", "sidebar-ethical-ads.html"]
}
html_sidebars = {
    'quick/**':[
        'globaltoc.html',  # Global Table of contents
        ],
    'edpsgui/**':[
        'globaltoc.html',  # Global Table of contents
        ],
    'muse/**':[
        'globaltoc.html',  # Global Table of contents
        ],
    '**': [
        'globaltoc.html',  # Global Table of contents
        'searchbox.html',  # search box
    ]
}
