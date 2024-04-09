=========================
Sphinx Tools for OpenQASM
=========================

This project is a Sphinx extension that adds an OpenQASM domain for Sphinx.
The Python package is called ``openqasm-sphinx``, and `can be downloaded from PyPI <https://pypi.org/project/openqasm-sphinx>`__.

To install the package using pip:

.. code-block:: bash

   pip install openqasm-sphinx

`The source is hosted on GitHub <https://github.com/openqasm/openqasm-sphinx>`__.


The ``oq`` domain
=================

This package provides a domain called ``oq``, and can be used to document both OpenQASM 2 and 3.
To use this domain, make sure this package is installed in your docs build, and add ``openqasm_sphinx`` to your ``extensions`` list in your ``conf.py`` file, such as:

.. code-block:: python

   project = "My Project"
   author = "Me"
   version = "1.0"

   extensions = [
       "openqasm_sphinx",
   ]

If your documentation project is primarily (or only) about documenting OpenQASM gates, you can set `the default domain for documentation <https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-primary_domain>`__ by setting ``primary_domain`` in your ``conf.py`` file, such as:

.. code-block:: python

   extensions = ["openqasm_sphinx"]
   primary_domain = "oq"

The project defines a directive for documenting OpenQASM gates.

.. directive:: .. gate:: signature

   Document an OpenQASM gate with the given signature.
   The body of the directive is the documentation content.

   Gates defined with this directive are cross-referenced using the :role:`gate` role.

   The signature should look like it would in OpenQASM, for example:

   .. code-block:: rst

      .. oq:gate:: cx a, b

         The controlled-X gate.

      .. oq:gate:: rz(θ) a

         A rotation by :math:`\theta` around the :math:`Z` axis.

   renders as

   .. oq:gate:: cx a, b

      The controlled-X gate.

   .. oq:gate:: rz(θ) a

      A rotation by :math:`\theta` around the :math:`Z` axis.

   .. versionadded:: 0.1.0

.. role:: gate

   The cross-referencing role for the :dir:`gate` directive.

   .. versionadded:: 0.1.0
