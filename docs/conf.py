# SPDX-License-Identifier: Apache-2.0

# pylint: disable=invalid-name

import openqasm_sphinx

project = 'OpenQASM Sphinx extension'
project_copyright = '2024, OpenQASM contributors'
author = 'OpenQASM contributors'
version = openqasm_sphinx.__version__

primary_domain = "rst"

extensions = [
    "sphinx.ext.githubpages",
    "sphinxcontrib.katex",
    "openqasm_sphinx",
]
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'
