"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a list of species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[str]: a list of strings
    """

    species = []

    # TODO: replace this with your code
    f = open(filename)
    for row in f:
        animal = row.split("|")[1]
        species.append(animal)

    return species


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    # TODO: replace this with your code
    f = open(filename)
    for row in f:
        name, species = row.split("|")[:2]

        if search_string in ("All", species):
            villagers.append(name)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    hobbies = []

    # TODO: replace this with your code
    f = open(filename)
    for row in f:
        fields = row.split("|")
        name = fields[0]
        hobby = fields[3]

        hobbies.append((hobby, name))

    fitness = []
    for h, f in hobbies:
        if h == "Fitness":
            fitness.append(f)

    nature = []
    for h, n in hobbies:
        if h == "Nature":
            nature.append(n)

    education = []
    for h, e in hobbies:
        if h == "Education":
            education.append(e)

    music = []
    for h, m in hobbies:
        if h == "Music":
            music.append(m)

    fashion = []
    for h, fa in hobbies:
        if h == "Fashion":
            fashion.append(fa)

    play = []
    for h, p in hobbies:
        if h == "Music":
            play.append(p)

    hobbies = [sorted(fitness), sorted(nature), sorted(education), sorted(music), sorted(fashion), sorted(play)]

    return hobbies


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code
    f = open(filename)
    for row in f:
        animal = row.split("|")
        all_data.append(tuple(animal))

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    f = open(filename)
    for row in f:
        name, species, person, hobby, motto = row.split("|")[:5]

        if villager_name in ("All", name):
            return motto

    return


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - list[str]: a set of names

    For example:
        -> find_likeminded_villagers('villagers.csv', 'Wendy')
        ['Bella', ..., 'Carmen']
    """

    attitude = ''
    names = []

    # TODO: replace this with your code
    f = open(filename)
    for row in f:
        name, species, personality = row.split("|")[:3]
        if name == villager_name:
            attitude += personality
        if personality == attitude:
            names.append(name)

    return names


print(all_species("villagers.csv"))
print(get_villagers_by_species("villagers.csv"), )
print(all_names_by_hobby("villagers.csv"))
print(all_data("villagers.csv"))
print(find_motto("villagers.csv", "Cyrano"))
print(find_likeminded_villagers("villagers.csv", "Cyrano"))