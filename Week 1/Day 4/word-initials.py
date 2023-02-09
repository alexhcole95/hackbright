def categorize_words_by_initial(text):
    words = text.split()

    words_by_initial = {}

    for word in words:
        if word == '':
            continue

        initial = word[0].upper()
        set_of_words = words_by_initial.get(initial, set())
        set_of_words.add(word)
        words_by_initial[initial] = set_of_words

    return words_by_initial


st_ives_poem = """
    As I was going to St. Ives
    I met a man with seven wives
    Every wife had seven sacks
    Every sack had seven cats
    Every cat had seven kits
    Kits, cats, sacks, wives.
    How many were going to St. Ives?
"""

print(categorize_words_by_initial(st_ives_poem))
