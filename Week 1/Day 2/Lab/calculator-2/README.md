## Exercise: Calculator REPL, Revisited
In the main exercise, we asked you to create a prefix calculator application. We gave you calculator.py — which was responsible for running the application’s user interface — and you implemented functions in arithmetic.py — which was responsible for executing mathematical operations behind-the-scenes.

This time, you’ll do the opposite. We’ll give you the backend (**arithmetic.py**) and you’ll write the frontend (**calculator.py**).


### Setup
[Click here to download the materials for this exercise](https://fellowship.hackbrightacademy.com/materials/shiptm1-devops/_downloads/be3104dd4f43eca4c521e39676566451/devops-calculator-2.zip) and unzip them into the folder where you store your programming projects. Then, open the folder in VS Code.

Remember to initialize your Git repo once you’ve downloaded the materials.


### Introduction
A **REPL**, or read-evaluate-print-loop, is a loop designed to continuously read input from the keyboard, evaluate it, and print its results to the screen. This should sound familiar since you’ve worked with several REPLs already — the Python shell, the game from **Guessing Game**, and the app from **Calculator, Part 1** are all powered by REPLs. REPLs are often implemented with while loops like this one:

    while exit_condition_not_reached:
        input = consume_input()
        output = evaluate_input(input)
        print(output)

In this exercise, you will re-implement the REPL in **calculator.py** from scratch. To do this, you will need to **tokenize** a string.

#### Tokenization
Tokenizing a string is the process of taking a string and breaking it up into its constituent parts as a list. Consider the following string:

    ocean_animals = 'shark,squid,tuna,flounder'

If we were to tokenize the string above, using a comma (`,`) as our delimiter, we’d get a list of tokens like so:

    ['shark', 'squid', 'tuna', 'flounder']

To create this list, you can use a string method called **split**:

    ocean_animals.split(',')  # => ['shark', 'squid', 'tuna', 'flounder']

#### Tokenization in calculator.py¶
Now consider the following string as read from the keyboard:

    input_string = 'pow 3 5'

If we tokenize on spaces, we get the following list:

    tokens = input_string.split(' ')   # => ['pow', '3', '5']

Now, how should we evaluate our list of tokens (`['pow', '3', '5']`)? Take some time to think about this and jot down some preliminary pseudocode before you continue to the next paragraph.

The first token — `pow` — lets us know what we ought to do with the remaining tokens. For example, in pseudocode:

    if the first token is 'pow':
        call the power function with the other two tokens

We can incorporate the pseudocode above into the pseudocode for the entire REPL:

    repeat forever:
        read input
        tokenize input
            if the first token is "q":
                quit
            else:
                (decide which math function to call based on first token)
                if the first token is 'pow':
                    call the power function with the other two tokens

                (...etc.)


### Building the Calculator REPL
This time, we’ve provided you with **arithmetic.py**, which contains the underlying math functions but feel free to use your own **arithmetic.py** from **Calculator, Part 1**.

#### arithmetic API
Either way, you’ll require the following functions from arithmetic.py:

    add(x, y) → float
    Return the sum of the two inputs

    subtract(x, y) → float
    Return the second number subtracted from the first.

    multiply(x, y) → float
    Multiply the two inputs together and return the result.

    divide(x, y) → float
    Divide the first input by the second and return the result.

    square(x) → float
    Return the square of the input.

    cube(x) → float
    Return the cube of the input.

    power(x, y) → float
    Raise the first input to the power of the second and return the result.

    mod(x, y) → float
    Divide the first input by the second input and return the remainder.

#### Finish calculator.py
Your task is to finish **calculator.py** by creating a REPL that will serve as the user interface for a prefix-notation calculator app.

A sample session of a finished calculator looks like this:

    > + 1 2
    3.0
    > - 10 5
    5.0
    > * 2 3
    6.0
    > / 7 2
    3.5
    > square 2
    4.0
    > cube 3
    27.0
    > pow 2 5
    32.0
    > mod 10 3
    1.0
    > q

(Notice the use of `q` to exit the REPL. You need to implement this behavior as well as the addition, subtraction, etc.)

Remember to commit your work as you go.