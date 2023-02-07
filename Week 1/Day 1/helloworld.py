msg = "Hello World"
print(msg)

name = "Alex"
if name == "Alex":
    print("Hi Alex")
print("Done")

spam = 0
while spam < 5:
    print("This is a for loop, essentially.")
    spam = spam + 1

print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

total = 0
for num in range(101):
    total = total + num
print(total)  # for loop

print('My name is')
i = 0
while i in range(5, -1, -1):
    print("Jimmy Five Times " + str(i))
    i = i + 1


def hello():
    print("Howdy!")
    print("Hola!")
    print("Bonjour!")


test = 42  # global variable


def eggs():
    test = 43  # local variable
    print(test)


eggs()
print(test)


def div42by(divide_by):
    try:
        return 42/divide_by
    except ZeroDivisionError:
        print("Error: You tried to divide by zero.")


# lists
animals = ["cat", "rat", "bat", "raccoon"]
print(animals[1])

numbers = [[1, 2, 3, 4], ["dog", "log", "bog", "cog"]]
print(numbers[0])
print(numbers[1][0])
print(numbers[1][-1])

list_slice = [10, 20, 30]
list_slice[1] = "Test"
print(list_slice)
list_slice[1:3] = ["Cat", "Dog", "Mouse"]
print(list_slice)
print(list_slice[:2])
print(list_slice[1:])

del list_slice[2]
print(list_slice)

true = "ello" in "Hello"
print(true)

false = "bye" in "Hello"
print(false)

supplies = ["pens", "staplers", "binders", "rulers"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

example_list = ["apple", "berries", "carrots", "danishes"]
for i, food in enumerate(example_list):
    print(f"The food at index {i} is {food}")

example = ["Yo", "my", "homie"]
print(example.index("Yo"))

example.append("what's up")
print(example)

example.insert(1, "chicken")
print(example)

example.remove("chicken")
print(example)

example.sort()
print(example)

example.sort(reverse=true)
print(example)

example.sort(key=str.lower)
print(example)

# dictionary in python
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])
print(f"My cat has {myCat['color']} fur.")

false = [1, 2, 3] == [3, 2, 1]
print(false)

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'species': 'cat', 'name': 'Zophie', 'age': 8}
print(eggs == ham)
print('name' in eggs)
print('name' not in eggs)

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))
print(eggs.keys())

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

print(eggs)
print('cat' in eggs.values())

if 'color' in eggs:
    print(eggs['color'])

print(eggs.get('age', 0))
print(eggs.get('color', ''))

