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

xlrd - Excel Files
==================
:Ref: https://www.youtube.com/watch?v=ZRwiMcGUf-Y

Dependencies
------------

.. code-block:: Bash

	pip3 install xlrd

Sample Code
-----------

.. code-block:: Python

	# Excel files
	import xlrd

	var_filename = "filename"
	# Open Workbook
	var_book = xlrd.open_workbook(var_filename)

	# Read sheet number from Book
	var_sheet = var_book.sheet_by_index(0)  # 1st sheet begins at 0


