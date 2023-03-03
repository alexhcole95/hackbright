import csv


class RestaurantRating:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def __repr__(self):
        return f"<RestaurantRating name={repr(self.name)} rating={repr(self.rating)}>"

    def __lt__(self, other):
        return self.rating < other.rating

    def update_rating(self, rating):
        self.rating = rating


class RestaurantRatings:
    def __init__(self, ratings=None):
        self.ratings = ratings or []

    def __repr__(self):
        return f"<RestaurantRatings ratings={repr(self.ratings)}>"

    def add_rating(self, name, rating):
        """Create and add a new RestaurantRating."""

        # Create a new RestaurantRating instance
        r = RestaurantRating(name, rating)

        # Add it to the list of ratings
        self.ratings.append(r)

    def remove_rating_by_index(self, index):
        """Remove a rating by index."""

        self.ratings.pop(index)

    def remove_rating_by_name(self, name):
        """Remove a rating by name."""

        for index in range(len(self.ratings)):
            if self.ratings[index].name == name:
                self.remove_rating_by_index(index)

    def get_rating_by_name(self, name):
        """Get a rating by name."""

        for n in self.ratings:
            if name == n.name:
                print(n.rating)

    def to_file(self, filename):
        """Write ratings to filename."""

        with open(filename, "w") as f:
            writer = csv.writer(f)

            for r in self.ratings:
                writer.writerow([r.name, r.rating])

    def from_file(cls, filename):
        """Read ratings from filename."""

        # TODO: Create a new RestaurantRatings instance
        # TODO: Open filename in read mode
        # TODO: Create a CSV reader
        # TODO: Loop over each row in the CSV file
        # TODO: Add it to the list of ratings

        return


r = RestaurantRating("State Bird", 3)
print(r)

r.update_rating(5)
print(r)

r1 = RestaurantRating("State Bird", 3)
r2 = RestaurantRating("State Bird Provisions", 5)
print(r1 < r2)

restaurants = [r1, r2]
restaurants.sort()
print(restaurants)

r1 = RestaurantRating("State Bird", 3)
r2 = RestaurantRating("State Bird Provisions", 5)
rr = RestaurantRatings([r1, r2])
print(rr.ratings)
print(rr)

rr.add_rating("McDonald's", 3)
rr.add_rating("Jack's", 5)
print(rr)

rr.remove_rating_by_index(2)
print(rr)

rr.remove_rating_by_name("Jack's")
print(rr)

rr.get_rating_by_name("State Bird")

rr.to_file("ratings.csv")
