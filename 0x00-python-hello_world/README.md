# 0x00. Python - Hello, World

| Script | What it does |
| ------ | ------------ |
| 0-run | This Shell script that runs a Python script.<br><br>The Python file name will be saved in the environment variable $PYFILE |
| 1-run_inline | This Shell script that runs Python code.<br><br>The Python code will be saved in the environment variable $PYCODE |
| 2-print.py | A Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.<br><br>Use the function `print`. |
| 3-print_number.py |  Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.<br><br>* You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)<br>* The output of the script should be:+ the number, followed by `Battery street`,+ followed by a new line<br>* You are not allowed to cast the variable `number` into a string<br>* Your code must be 3 lines long.<br>* You have to use the new print numbers [tips](https://pyformat.info/#number) (with .format(...)). |
| 4-print_float.py |  |
| 5-print_string.py |  |
| 6-concat.py |  |
| 7-edges.py |  |
| 8-concat_edges.py |  |
| 9-easter_egg.py |  |
| 10-check_cycle.c, lists.h | Technical interview preparation:<br><br>You are not allowed to google anything<br>Whiteboard first<br>This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.<br><br>Write a function in C that checks if a singly linked list has a cycle in it.<br><br>* Prototype: `int check_cycle(listint_t *list)`;<br>* Return: 0 if there is no cycle, 1 if there is a cycle.<br><br>Requirements:<br><br>Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`. |
| 100-write.py | A Python script that prints exactly and `that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.<br><br>* Use the function write from the sys module.<br>* You are not allowed to use print.<br>* Your script should print to stderr.<br>* Your script should exit with the status code 1. |
| 101-compile | A script that compiles a Python script file.<br><br>The Python file name will be stored in the environment variable $PYFILE<br><br>The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc) |
| 102-magic_calculation.py | Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode: <pre>3           0 LOAD_CONST               1 (98)<br>            3 LOAD_FAST                0 (a)<br>            6 LOAD_FAST                1 (b)<br>            9 BINARY_POWER<br>            10 BINARY_ADD<br>            11 RETURN_VALUE </pre> |
