# define interface for store
# contains name, rating, address, recommend_count

# if a store's name is the same, then it is the same store
class Matzip:

    def __init__(self, name, rating, address, recommend_count):
        self.name = name
        self.rating = rating
        self.address = address
        self.recommend_count = recommend_count

    def __str__(self):
        return f"{self.name}({self.rating})"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "name": self.name,
            "rating": self.rating,
            "address": self.address,
            "recommend_count": self.recommend_count
        }

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)
