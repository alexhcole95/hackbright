## Exercise: Calculator REPL
This exercise will have you complete functions to finish implementing a prefix calculator CLI application (an application that runs in the terminal). The calculator lets a user add, subtract, multiply, divide, square a number, cube a number, raise a number to a given power, and find the remainder when one number is divided by another (otherwise known as taking one number mod another).


### Setup
This exercise includes starter code. Follow the instructions to download the starter code and set up the project directory.

1. [Click here to download the materials for this exercise](https://fellowship.hackbrightacademy.com/materials/shiptm1-devops/_downloads/fd9d348e0815dce8af7f5cfb58a4ff6b/devops-calculator.zip) and unzip them into the folder where you store your programming projects.
2. Open the folder in VS Code.
3. In VS Code’s integrated terminal (you can open the terminal by clicking on View > Terminal), run the following commands to initialize a Git repository.

       git init
       git add calculator.py arithmetic.py  
       git commit -am "Initial commit"

Get in the habit of doing this at the beginning of every exercise. You don’t want to be in a situation where you’re knee-deep in an exercise but you’ve forgotten to use Git and then your pet eats your computer, causing you to lose all your work! Also, it’s nice having that initial commit to record what your project files looked like when you first received them.


### Introduction

#### Calculators and Notation
We typically write math equations using **infix notation** like this `3 + 2` where the operator (in this case, the plus sign) goes inside the numbers.

Another way to write equations is with **prefix notation**. As the name implies, in prefix notation, operators go before the operands so, instead of `3 + 2`, you'd write `+32`.

One advantage of prefix notation is the ability to have an arbitrary number of operands. For example, `4 + 3 + 2` in prefix notation is `+432`.

In this exercise, we will build a basic prefix calculator together. We will provide half of the program, and you will code the other half. We will use this idea to explore the concept of an **API (application programming interface)**.


#### What’s an API?
An **interface** is a shared boundary between two systems that allows one to communicate with the other. For example, a graphical user interface sits between you and your computer and gives you the ability to interact with its operating system. In software engineering, an **API (application programming interface)** sits between you and your program and allows you to perform a set of operations using your programming language.

APIs don’t come from the void — they’re implemented by other developers. When authors of an API want to distribute their code for other devs to use, they’ll publish documentation on their API. **API documentation** (colloquially, “API docs”) will contain information like the names of functions, what those functions take as input, and what the functions will output — all the information a dev like you would need to know to use the API!

If you’d like to see examples of good API docs, look no further than the Python documentation. Take a moment to [click on this link and skim the docs for Python’s Built-In Functions API](https://docs.python.org/3/library/functions.html). Note that each entry contains key pieces of information:

- The name of the function
- Its required and optional inputs
- What the function does and/or what it outputs

Together, these three pieces of information are a function's **signature**.

A function signature is a way of describing a function without going into the details of how it operates. For example, consider the following function:

    def square(x):
        """Return square of x."""
        return x * x

`If we were to describe its signature, we’d say that the function square accepts a number as input and returns the square of that number.`

Most docs will represent the sentence above like so:

    **square(n)**  
    Take a number as an argument and return a number with the value n².

Note that it doesn’t explain how the function works under-the-hood. This makes sense — when you want to use a function, you don’t care how it’s been implemented; you care about how to make it work.


### Completing Functions for a Calculator App

#### How the App Works
We’ve provided a terminal-based prefix calculator app with your exercise materials as a Python file called **calculator.py**. It relies on the other file we’ve included — **arithmetic.py** — so make sure both files are in the same directory. Otherwise, **calculator.py** won’t run.

First, let’s get oriented by running **calculator.py**:

1. Run the command below in the VS Code terminal to run calculator.py:  

        python3 calculator.py

2. Then, when you see the prompt `Enter your equation > ``, type ``+ 1 2` and press Enter:

        Enter your equation > + 1 2
        10

As you can see, **calculator.py** doesn’t work — `+ 1 2` is definitely not `10`!

This happens because **calculator.py** relies on functions from **arithmetic.py** and the problem with **arithmetic.py** is… well… you should check it out and see for yourself. Why do you think `+ 1 2` gave `10` instead of `3`?

#### Finish arithmetic.py
Your task is to complete the functions in **arithmetic.py** so **calculator.py** will actually work. Here’s an example of what the calculator should be able to do:

    Enter your equation > + 1 2
    3.0
    Enter your equation > - 10 5
    5.0
    Enter your equation > * 2 3
    6.0
    Enter your equation > / 7 2
    3.5 
    Enter your equation > square 2
    4.0
    Enter your equation > cube 3
    27.0
    Enter your equation > pow 2 5
    32.0
    Enter your equation > mod 10 3
    1.0
    Enter your equation > q

You can start by fixing the **add** function so `+ 1 2` prints the proper value to the screen. When you’re finished with **add**, run **calculator.py** so you can test and double-check that your function works.

Then — since you’ve just finished a unit of working code — you should stage and commit your changes:

    git add arithmetic.py
    git commit -am "Completed add function"

Rinse and repeat for the rest of the functions in **arithmetic.py**. A tip before you go: when you encounter errors as you test each function by running **calculator.py**, first try to understand where and why the error occurred. Read the error messages and apply fixes to one error at a time.
