"""Count words in file."""

# put your code here.


def wordcount(filename):
    f = open(filename)
    contents = f.read()
    words = contents.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    for word, count in word_counts.items():
        print(f"{word}: {count}")


filename = input("Enter the filename: ")
wordcount(filename)
