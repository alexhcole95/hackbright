import re

txt = "amanda"
num = "12345678033455233345667789998222345219223238834"
dupes = "bbbaaaccccbbbaaadddccbbabbaabbbaabaaa"


# TODO: 1. All strings of lowercase letters that begin and end in a
x = re.findall("^a[a-z]*a$", txt)
print(x)

# TODO: 2. All strings of lowercase letters that either begin or end in a( or both and end with 'a')
x = re.findall("^a[a-z]*|[a-z]*a$", txt)
print(x)

# TODO: 3. All strings of digits that contain no leading zeros
x = re.findall(r"^[1-9]*", num)
print(x)


# TODO: 4. All strings of digits that represent even numbers
x = re.findall(r"[02468]", num)
print(x)

# TODO: 5. All strings of digits such that all the 2s occur before all the 9s
x = re.findall(r"^[0-8]*[013456789]*?", num)
print(x)

# TODO: 6. All strings of as and bs that contain no three consecutive bs


# TODO: 7. All strings of digits that represent a number divisible by 5


# TODO: 8. All strings of digits that contain at most one 0


# TODO: 9. All sequences of letters that contain at least one uppercase letter and at least one lowercase letter.


