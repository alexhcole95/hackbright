## Exercises: Regex Practice
Prompts for programming tasks to help you practice regular expressions.


### Date Detection
Write a regular expression to match dates written in the `DD/MM/YYYY` format. Then, store these strings into variables named **month**, **day**, and **year**. Write additional code to detect if it’s a valid date according to these rules:

- April, June, September, and November have 30 days.
- February has 28 days, except in leap years when it has 29 days.
- The rest of the months have 31 days.
- Leap years are every year evenly divisible by 4, except for years evenly divisible by 100, unless the year is also evenly divisible by 400.


### Validate Passwords
Write a function that checks if a given password is strong or not. A strong password:

- Is at least 8 characters long.
- Contains both uppercase and lowercase characters.
- Has at least one digit.

You might need multiple regex patterns to check for these requirements.


### Regex _strip_
Write a function that takes a string and does the same thing as the strip string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string.
