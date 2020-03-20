README
#######
:Author: David Boyd
:Date: 2020-03-20

Overview
================
+-----------------------------+-------------------------+
| Libraries/Functions/Methods | Description             |
+=============================+=========================+
| import os                   | remove & rename files   |
+-----------------------------+-------------------------+
| os.remove                   | remove a file           |
+-----------------------------+-------------------------+
| os.rename                   | rename a file           |
+-----------------------------+-------------------------+
| open(filenmae, mode)        | open file as r,w, or a  |
+-----------------------------+-------------------------+
| .write(var)                 | write to file           |
+-----------------------------+-------------------------+
| .read()                     | read entire contents    |
+-----------------------------+-------------------------+
| .close()                    | close file              |
+-----------------------------+-------------------------+
| .readline()                 | read a line from file   |
+-----------------------------+-------------------------+
| .rstrip('\n')               | strip from readline obj |
+-----------------------------+-------------------------+

+-------------------+-----------------------------+--------------------------+
| ExceptionName     | Description                 | Example                  |
+===================+=============================+==========================+
| ZeroDivisionError | stops division by '0'       | 22/0                     |
+-------------------+-----------------------------+--------------------------+
| ValueError        | cannot convert to data type | int('forty')             |
+-------------------+-----------------------------+--------------------------+
| IOError           | no such file or directory   | open("badfile.txt", 'r') |
+-------------------+-----------------------------+--------------------------+
| except            | catches any and all exception types                    |
+-------------------+--------------------------------------------------------+

Notes
=====

	- Numbers written to a file must be converted to **str(num)**

Working With Files
==================

.. code-block :: Python3

	# Openining a File
	file_var = open(filename, mode)		# mode = 'r'ead, 'w'rite, 'a'ppend

	# Specifying the location of a file
	file_var = open(r'C:\Users\...', 'w')	# r' = raw string (\ = literals)

	# Writing data to a file
	file_obj.write("string")
	file_obj.write(variable)

	# Reading data from a file
	variable = infile.read()		# var.read() = entire contents
	print(variable)

	var_line1 = infile.readline()	# var.readline() = line, where -d '\n'
	print(var_line1)

	# Concatenate newline
	outfile = open(filename, 'w')
	outfile.write(var + '\n')

	# Stripping the newline
	var_readline2 = var_readline2.rstrip('\n')

	# Appending data to an existing file
	infile = open(filename, 'a')
	infile.write(var + '\n')
	infile.close()

	###
	# Reading to End of File (EOF)
	###
	## METHOD1: read until empty line
	##	[[warning: if file has blank line then exit]]
	line = file.readline()
	while line != '':
		...
		line = file.readline()

	## METHOD2
	## for *variable* in *file_object*:
	##		...
	for line in infile:
		pirnt(line)

	# Remove and rename functions --MODIFYING FILES
	import os
	os.remove('filename0')
	os.rename('filename1', 'otherFilename')

try/except
==========

Gracefully handle exceptions to prevent your program from crashing.

.. code-block :: Python3

	# syntax
	try:
		...
		...
	except <ExceptionName>:
		...
		...

	###
	# Displaying an Exception's Default Error Message
	###
	try:
		...
		...
	except ValueError as err:		# assign the exception obj to var err
		print(err)

	### The 'else' clause --executed if no exceptions were raised
	else:
		...
		...
	### 'finally' clause --executed whether an exception occurs or not
	## purpose: perform cleanup operations
	finally:
		...
		...

