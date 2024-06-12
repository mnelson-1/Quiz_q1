# Duplicate Integer Finder
## Programming Assignment : Mid-term Quiz
### Task Description:
Using any programming language you choose, Write a program that reads a list of integers from an input file. Generate an output file with a list of duplicate integers present in the input file.

## Features
Reads integers from an input file
Identifies duplicate integers
Writes duplicate integers to an output file in increasing order
Handles whitespace and invalid input gracefully

## Requirements
Python compiler (interpreter): depending on your machine specifications python or python3 is required for this program.
Use python --version to check the version of python on your machine.

## How to Use

## Installation

You will need to clone the repository of the project from Github. This will contain the simple shell program and all of its dependencies.

```
git clone https://github.com/mnelson-1/Quiz_q1.git
```

To compile and run the program run the following command in your terminal:
python(3) -u <program_file-name> <input_file-name>
The python interpreter you use is dependent on the version installed on your machine; for me this will look like this:
python3 -u [DuplicateInt.py] [sample_04.txt]

Pls note that square brackets won't be used when actually running the program, this has been included for emphatic basis.

*<input_file-name> - file containing integers*

## Example

Say we have an input file sample_input_02.txt with the following content:

1023
-1023
500
500
-1023
100

Run the program:
python(3) -u UniqueInt.py sample_input_02.txt

The program will create an output file named sample_input_02.txt_results.txt containing the unique integers:

-1023
500

## Output
The program will generate an output file named <input_file-name>_results.txt. This file will contain all the unique integers from the input file, each on a new line, arranged in increasing order.

## Handling Different Input Scenarios
### Whitespace Handling:
Lines with only whitespace characters are skipped
Leading and trailing whitespaces around integers are ignored.
## Invalid Lines:
Lines containing non-integer values (alphabets, punctuation, floating-point numbers, etc.) are skipped.
Lines with integers out of the range [-1023, 1023] are skipped.
### Empty Lines:
Lines that are completely empty or contain only whitespace are skipped.


# Author
Nelson Somtochukwu <m.nelson@alustudent.com>
