# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Java OceanAtlas'
copyright = '2024, Jim Swift'
author = 'Jim Swift'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_design", "sphinx.ext.todo"]

todo_include_todos = True
todo_emit_warnings = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

myst_enable_extensions = ["attrs_inline", "fieldlist"]

numfig = True


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

html_theme_options = {
    "logo": {
        "text": "Java OceanAtlas",
        "image_light": "_static/joa_logo.svg",
        "image_dark": "_static/joa_logo.svg",
    },
    "collapse_navigation": True
}

html_extra_path = [
    "_include"
]