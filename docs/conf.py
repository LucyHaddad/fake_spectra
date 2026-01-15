# a loooot of this from python-copier-template
import sys
import requests

project = "fake-spectra"

extensions = [
    # For graphviz diagrams
    "sphinx.ext.graphviz",
    # For linking to external sphinx documentation
    "sphinx.ext.intersphinx",
    # So we can write markdown files
    "myst_parser",
]

# So we can use the ::: syntax
myst_enable_extensions = ["colon_fence"]

nitpicky = True
nitpick_ignore = []
graphviz_output_format = "svg"

default_role = "any"

# The suffix of source filenames.
source_suffix = ".md"

# The master toctree document.
master_doc = "index"

exclude_patterns = ["_build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

rst_epilog = """
.. _fake-spectra: https://github.com/LucyHaddad/fake_spectra
"""

# Set copy-button to ignore python and bash prompts
# https://sphinx-copybutton.readthedocs.io/en/latest/use.html#using-regexp-prompt-identifiers
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: "
copybutton_prompt_is_regexp = True

# -- Options for HTML output -------------------------------------------------

html_theme = "pydata_sphinx_theme"
github_repo = project
github_user = "LucyHaddad"

html_theme_options = {
    "logo": {
        "text": project,
    },
    "use_edit_page_button": True,
    "github_url": f"https://github.com/{github_user}/{github_repo}",
    "navbar_end": ["theme-switcher", "icon-links", "version-switcher"],
}

html_context = {
    "github_user": github_user,
    "github_repo": github_repo,
    "doc_path": "docs",
    "github_version":"0.0.0"
}

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False


# Logo
# html_logo = "path to a logo ...."
# html_favicon = html_logo