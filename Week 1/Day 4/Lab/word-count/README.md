## Exercise: Data Structures
Data structure is a generic term used to describe a scheme for organizing, storing, and managing data. In this exercise, you’ll continue to practice working with the data structures and data types we’ve encountered so far but, this time, we’re increasing the complexity of the data by nesting data structures.

You can accomplish a lot with just a little Python and a large batch of data.

In this exercise, you’ll build programs to practice working with data structures like lists, dictionaries, tuples, and strings.


### Getting Started

[Click here to download the starter code](https://fellowship.hackbrightacademy.com/materials/shiptm1-devops/_downloads/2be176ab241f912c0d52472827110a44/devops-data-structs.zip), unzip, and open the folder in VS Code. Don’t forget to initialize a Git repo.

### Word Count
Write a program, **wordcount.py**, that opens a file and counts how many times each space-separated word occurs in that file. Your program should then output each word and the number of times it appears in the file.

For example, these are the contents of **test.txt** (it’s included in your starter code):

    test.txt
        As I was going to St. Ives
        I met a man with seven wives
        Every wife had seven sacks
        Every sack had seven cats
        Every cat had seven kits
        Kits, cats, sacks, wives.
        How many were going to St. Ives?

Running **wordcount.py** should produce the following output:

    > python3 wordcount.py
    As 1
    I 2
    was 1
    going 2
    to 2
    St. 2
    Ives 1
    met 1
    a 1
    man 1
    with 1
    seven 4
    wives 1
    Every 3
    wife 1
    had 3
    sacks 1
    sack 1
    cats 1
    cat 1
    kits 1
    Kits, 1
    cats, 1
    sacks, 1
    wives. 1
    How 1
    many 1
    were 1
    Ives? 1

In addition to **test.txt**, we’ve provided a longer file, **twain.txt**, which you can use to test out a longer input text.

You may find it useful to switch to **twain.txt** to see how your program performs when the text gets longer.
