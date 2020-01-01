Modules
###
:Author: David Boyd
:Date: 2020-01-01

Package Repo Index - https://pypi.python.org/pypi

.. code-block:: Bash

	# Python 2
	pip install <pkg>

	# Python 3
	pip3 install <pkg>

python-nmap
===========
:About: A python class to use nmap and access scan results from Python3.
:Ref: https://pypi.org/project/python-nmap/

Install
-------

.. code-block:: Bash

	# Python 2
	pip install python-nmap

	# If d/l from website (extract tarball)
	python setup.py install

Code
----

.. code-block:: Python

	import nmap
	var_nmap1 = nmap.PortScanner()

	# Assign nmap version
	var_a = var_nmap1.nmap_version()
	print(var_a)

xlrd
====
:About: Library for developers to extract data from MS Excel spreadsheet files.
:Ref: https://www.youtube.com/watch?v=ZRwiMcGUf-Y

Install
-------

.. code-block:: Bash

	pip3 install xlrd

Code
----

.. code-block:: Python

	# Excel files
	import xlrd

	var_filename = "filename"
	# Open Workbook
	var_book = xlrd.open_workbook(var_filename)

	# Read sheet number from Book
	var_sheet = var_book.sheet_by_index(0)  # 1st sheet begins at 0


