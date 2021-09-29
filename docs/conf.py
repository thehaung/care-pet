# -*- coding: utf-8 -*-
import os
import sys
from datetime import date

import recommonmark
from recommonmark.transform import AutoStructify

from sphinx_scylladb_theme.utils import multiversion_regex_builder

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.extlinks",
    "sphinx_scylladb_theme",
    "sphinx_multiversion",
    "recommonmark",
    "sphinx_markdown_tables"
]


# The suffix(es) of source filenames.
source_suffix = [".rst", ".md"]
autosectionlabel_prefix_document = True

# The master toctree document.
master_doc = "index"

# General information about the project.
project = 'ScyllaDB IoT Example Documentation'
copyright = str(date.today().year) + ', ScyllaDB. All rights reserved.'
author = u'Scylla Project Contributors'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "sizing.md"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# Setup Sphinx
def setup(sphinx):
    sphinx.add_config_value(
        "recommonmark_config",
        {
            "enable_eval_rst": True,
            "enable_auto_toc_tree": False,
        },
        True,
    )
    sphinx.add_transform(AutoStructify)


# List of substitutions
rst_prolog = """
"""
# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_scylladb_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'default_branch': 'master',
    'hide_sidebar_index': 'true',
    'hide_edit_this_page_button': 'false',
    'github_issues_repository': 'scylladb/care-pet',
    'github_repository': 'scylladb/care-pet',
    'site_description': 'ScyllaDB IoT Example Documentation',
    'conf_py_path': 'docs/',
}

extlinks = {
}

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
html_last_updated_fmt = '%d %B %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
html_sidebars = {'**': ['side-nav.html']}

# Output file base name for HTML help builder.
htmlhelp_basename = 'ScyllaDocumentationdoc'

# URL which points to the root of the HTML documentation. 
html_baseurl = 'https://care-pet.docs.scylladb.com'

# Dictionary of values to pass into the template engine’s context for all pages
html_context = {'html_baseurl': html_baseurl}

# -- Options for not found extension -------------------------------------------

# Template used to render the 404.html generated by this extension.
notfound_template = "404.html"

# Prefix added to all the URLs generated in the 404 page.
notfound_urls_prefix = ""

# -- Options for redirect extension ---------------------------------------

# Read a YAML dictionary of redirections and generate an HTML file for each
redirects_file = "_utils/redirections.yaml"

# -- Options for multiversion --------------------------------------------

# Whitelist pattern for tags (set to None to ignore all tags)
TAGS = []
smv_tag_whitelist = multiversion_regex_builder(TAGS)
# Whitelist pattern for branches (set to None to ignore all branches)
BRANCHES = ['master']
smv_branch_whitelist = multiversion_regex_builder(BRANCHES)
# Defines which version is considered to be the latest stable version.
# Must be listed in smv_tag_whitelist or smv_branch_whitelist.
smv_latest_version = 'master'
smv_rename_latest_version = ''
# Whitelist pattern for remotes (set to None to use local branches only)
smv_remote_whitelist = r"^origin$"
# Pattern for released versions
smv_released_pattern = r'^tags/.*$'
# Format for versioned output directories inside the build directory
smv_outputdir_format = '{ref.name}'

