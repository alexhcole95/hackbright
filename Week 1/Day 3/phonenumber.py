# def is_phone_number(text):
#     if len(text) != 12:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != '_':
#         return False
#     for i in range(4, 7):
#         if not text [i].isdecimal():
#             return False
#     if text[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not text[i].isdecimal():
#             return False
#     return True

import re, pyperclip

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search("Call me 415-555-1011 tomorrow, or at 415-555-9999")
print(mo.group())

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phone_num_regex.findall("Call me 415-555-1011 tomorrow, or at 415-555-9999"))

pattern = re.compile(r"\d\d\d-\d\d\d-\d\d\d\d")
input = "My phone number is 555-555-1234"

mo = pattern.search(input)
print(mo.group())

# regex that matches domain name
# r" is a delimiter
# r"(https?://)?((\w+\.)+(com|edu|gov|net|org|co.uk))$  for domain
# r"^(\w+)@((\w+\.)+(com|edu|gov|net|org|co.uk))$  for email

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneRegex)

text = "Serve the public trust.\nProtect the innocent.\nUphold the law."

pattern = re.compile(r".*", re.DOTALL)
mo = pattern.search(text)
print(mo.group())


# TODO: Create a regex for phone numbers.
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-000, 555-0000 ext 12345, ext. 12345, x12345

(((\d\d\d | (\(\d\d\d\)))?   # area code (optional)
(\s|-)                       # first separator
\d\d\d                       # first three digits
-                            # separator
\d\d\d\d                     # last 4 digits
((ext(\.)?\s)|x)             # extension (optional)
(\d{2,5}))?)                 # extension number-part (optional

''', re.VERBOSE)

# TODO: Create a regex for email addresses.
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+     # name part
@                   # @ symbol
[a-zA-Z0-9_.+]+     # domain name part

''', re.VERBOSE)

# TODO: Get the text off the clipboard.
text = pyperclip.paste()


# TODO: Extract the email / phone from this text.
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)

# TODO: Copy the extracted email / phone to the clipboard.
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
