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
import os
import sys
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../scripts'))
sys.path.insert(0, os.path.abspath('../oemof_b3/config/'))

# -- Project information -----------------------------------------------------

project = 'oemof-B3'
copyright = '2020, Reiner Lemoine Institut'
author = 'Reiner Lemoine Institut'

# The full version, including alpha/beta/rc tags
release = '0.0.3dev'


# -- General configuration ---------------------------------------------------
master_doc = 'index'
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinxcontrib.bibtex',
    'sphinx.ext.autosectionlabel'
]

# specify bibfiles for sphinxcontrib.bibtex
bibtex_bibfiles = ['bibliography.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for Sphinx autodoc ----------------------------------------------

autodoc_mock_imports = [
    "pandas",
    "matplotlib",
    "numpy",
    "demandlib",
    "rtree",
    "pyyaml",
    "docutils",
    "dynaconf",
    "yaml",
    "pyomo",
    "oemof",
    "oemof.outputlib",
    "oemof.tabular",
    "oemoflex",
    "oemof.solph",
    "oemof_b3.config.config",
    "geopandas",
    "shapely",
    "oem2orm",
]
