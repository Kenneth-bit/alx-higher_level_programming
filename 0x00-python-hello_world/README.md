# 0x00. Python - Hello, World

| Script | What it does |
| ------ | ------------ |
| 0-run | This Shell script that runs a Python script.<br><br>The Python file name will be saved in the environment variable $PYFILE |
| 1-run_inline | This Shell script that runs Python code.<br><br>The Python code will be saved in the environment variable $PYCODE |
| 2-print.py |  |
| 3-print_number.py |  |
| 4-print_float.py |  |
| 5-print_string.py |  |
| 6-concat.py |  |
| 7-edges.py |  |
| 8-concat_edges.py |  |
| 9-easter_egg.py |  |
| 10-check_cycle.c, lists.h |  |
| 100-write.py | A Python script that prints exactly and `that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.<br><br>* Use the function write from the sys module.<br>* You are not allowed to use print<br>* Your script should print to stderr<br>* Your script should exit with the status code 1. |
| 101-compile | A script that compiles a Python script file.<br><br>The Python file name will be stored in the environment variable $PYFILE<br><br>The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc) |
| 102-magic_calculation.py | Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:`3           0 LOAD_CONST               1 (98)
	3 LOAD_FAST                0 (a)
	6 LOAD_FAST                1 (b)
	9 BINARY_POWER
	10 BINARY_ADD
	11 RETURN_VALUE` |
