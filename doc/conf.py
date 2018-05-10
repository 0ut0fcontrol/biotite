# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

__author__ = "Patrick Kunzmann"

from os.path import realpath, dirname, join, isdir, isfile, basename
import sys
import glob
from doc.apidoc import *
from doc.examples import *

absolute_path = dirname(realpath(__file__))
package_path = join(dirname(absolute_path), "src")
sys.path.insert(0, package_path)
import biotite

### Creation of API documentation ###

create_api_doc(package_path, join(absolute_path, "apidoc"))

##### Creation of code examples #####

dirs = glob.glob(join(absolute_path, "examples", "*"))
for d in dirs:
    if isdir(d):
        create_example_file(d)
create_example_index()

##### General #####

extensions = ["sphinx.ext.autodoc",
              "sphinx.ext.autosummary",
              "sphinx.ext.doctest",
              "sphinx.ext.mathjax",
              "sphinx.ext.viewcode",
              "numpydoc"]

templates_path = ["templates"]
source_suffix = [".rst"]
master_doc = "index"

project = "Biotite"
copyright = "2017, the Biotite contributors"
version = biotite.__version__

exclude_patterns = ["build"]

pygments_style = "sphinx"

todo_include_todos = False

# Prevents numpydoc from creating an autosummary which does not work
# due to Biotite's import system
numpydoc_show_class_members = False


##### HTML #####

html_theme = "alabaster"
html_static_path = ["static"]
html_favicon = "static/assets/general/biotite_icon_32p.png"
htmlhelp_basename = "BiotiteDoc"
html_sidebars = {"**": ["about.html",
                        #"localtoc.html",
                        "navigation.html",
                        "relations.html",
                        "searchbox.html",
                        "donate.html"]}
html_theme_options = {
    "description"      : "A general framework for computational biology",
    "logo"             : "assets/general/biotite_logo_s.png",
    "logo_name"        : "false",
    "github_user"      : "biotite-dev",
    "github_repo"      : "biotite",
    "github_banner"    : "true",
    "page_width"       : "85%",
    "fixed_sidebar"    : "true"
    
}

