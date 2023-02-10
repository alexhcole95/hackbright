#   TODO: Date Detection

import re

date_regex = '[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}'
dates = input("Please type in a date in DD/MM/YYYY format: ")

day = ''
month = ''
year = ''

date = re.findall(date_regex, dates)
for data in date:
    fields = data.split("/")

    if fields[0] <= "0":
        print("There is no month with " + fields[0] + " days!")
        break

    if fields[0] >= "32":
        print("There is no month with " + fields[0] + " days!")
        break

    if fields[1] == "02":
        if int(fields[2]) % 4 == 0:
            if int(fields[2]) % 100 == 0 and int(fields[2]) % 400 == 0:
                if fields[0] <= "29":
                    day += fields[0]
                    month += fields[1]
                    year += fields[2]

                else:
                    print("This month doesn't have " + fields[0] + " days!")

        elif fields[0] >= "29":
            print(fields[2] + " isn't a leap year!")

        else:
            day += fields[0]
            month += fields[1]
            year += fields[2]

    elif fields[1] in ["04", "06", "09", "11"]:
        if fields[0] == "31":
            print("This month only has thirty days!")
        else:
            day += fields[0]
            month += fields[1]
            year += fields[2]

    else:
        day += fields[0]
        month += fields[1]
        year += fields[2]

print("Day:", day)
print("Month:", month)
print("Year:", year)


#   TODO: Validate Passwords
# This is incomplete, we got pretty far along but was having issues with making a function.

password = input("Type password here: ")

while len(password) < 8:
    print("Password must be at least 8 characters!")
    break

regex = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$"

data = re.findall(regex, password)

#   TODO: Regex Strip

stripChar = input('Enter character to strip: ')
context = input('Enter string to strip: ')
stripContext = None


def strip(char, string):
    if char == "":                # not "stripChar"
        space = re.compile(r'^\s+|\s+$')
        word = space.sub("", string)
        return word
    else:                       # some changes are here in this else statement
        word = re.sub(r'{}|{}'.format(char, char), "", strip("", string))
        return word


print(strip(stripChar, context))
