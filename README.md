# TuringMachineSimulator.com Tester

# File struct
Each student has a folder with their name, and problems 1 through 8 names problem1.txt, problem2.txt... for each problem there is also a problemXTests.txt with a test case per row in the form of `101,True` where the first part is the input to the TM, and True or False identifies that the TM should accept or reject respectively.

## testing.py
You can run the testing.py script to run tests for all problems. The script will generate a grades.txt file with one line per student, and each line with a grade (computed as percentage of test cases passed).

## makeTests.py
The makeTests.py script automatically generates test cases for problems 1-8.

## Requirements
The Python scripts were run using Python3 on a Windows machine (but are also compatible with Mac by changing the Selenium Chrome Driver binding). The Python scripts use Selenium, NumPy, and alive-progress.