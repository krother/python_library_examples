# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Python Library Examples'
copyright = '2025, Kristian Rother'
author = 'Kristian Rother'
release = '1.0'
html_title = f"{project}"

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_design',
    'sphinx_copybutton',
    'sphinx.ext.todo',
    'myst_parser',
    #'sphinxcontrib.cairosvgconverter',
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'learning_goals.md', 'README.md']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_logo = "_static/academis_logo.png"
html_favicon = "_static/favicon.ico"


html_css_files = [
    "academis.css",
]

html_theme_options = {
    'github_user': 'krother',
    'github_repo': 'python_library_examples',
    'show_relbar_top' : True,
    'show_relbar_bottom' : True,
    "source_repository": "https://github.com/krother/python_library_examples",
    "source_branch": "main",
    "source_directory": "",
}

# ---- Options for PDF output ----

latex_elements = {
    'preamble': r"\linespread{1.25}",
}
