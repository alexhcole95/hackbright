## Exercise: Data Structures

Data structure is a generic term used to describe a scheme for organizing, storing, and managing data. In this exercise, you’ll continue to practice working with the data structures and data types we’ve encountered so far but, this time, we’re increasing the complexity of the data by nesting data structures.

You can accomplish a lot with just a little Python and a large batch of data.

In this exercise, you’ll build programs to practice working with data structures like lists, dictionaries, tuples, and strings.


### Getting Started

[Click here to download the starter code](https://fellowship.hackbrightacademy.com/materials/shiptm1-devops/_downloads/2be176ab241f912c0d52472827110a44/devops-data-structs.zip), unzip, and open the folder in VS Code. Don’t forget to initialize a Git repo.


### Process Data from a File

#### Understanding the Data

The data you’ll work with is in a [CSV file](https://en.wikipedia.org/wiki/Comma-separated_values) named **villagers.csv**. CSV (comma-separated values) is a file format for storing spreadsheet data. The “comma-separated” part of CSV is a bit of a misnomer though — it’s not uncommon to see CSV files that use other characters like tab or | instead of commas.

villagers.csv uses | to separate the following fields:

    name|species|personality|hobby|motto

For example, if we applied the format above to the first line in **villagers.csv**, we get the following information:

- **name:** Cyrano
- **species:** Anteater
- **hobby:** Education
- **motto:** Don’t punch your nose to spite your face.

#### Write Functions to Process Data

Your task is to complete the functions in **villager_data.py**.

Here’s a summary of those functions:

**all_species(filename) → List[str]**
Take in the name of a data file (as a string) and return a list of species found in the file (it’s ok for the list to contain duplicates).

**get_villagers_by_species(filename, search_string='All') → List[str]**
Take in the name of a file and the name of a species. Return the names of all villagers of the given species, in alphabetical order.

If the species argument is omitted, return a list of all villagers’ names in alphabetical order.

**all_names_by_hobby(filename) → List[List[str]]**
Return a list of villagers, but group their names by hobby. To group names together, put them in the same list. Since there are six possible hobbies (Fitness, Nature, Education, Music, Fashion, and Play), your return value should be a list with **six lists inside**.

Make sure the six lists appear in this order:

1. Fitness
2. Nature
3. Education
4. Music
5. Fashion
6. Play

Like before, the names in each list should appear in alphabetical order.

**all_data(filename) → List[Tuple[str]]**
Return all the data in a file as a list of tuples.

Each line in the file is a tuple of `(name, species, personality, hobby, motto)`.

**find_motto(filename, villager_name) → str**
Take in the name of a file and the name of a villager. Return the villager’s motto. Return **None** if you’re not able to find a villager with the given name.

**find_likeminded_villagers(filename, villager_name) → List[str]**
Take in the name of a file and the name of a villager. Return a list of villagers with the same personality.
