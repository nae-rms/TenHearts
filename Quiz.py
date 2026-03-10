import pandas as pd
import random

# loading / importing pkl file
villagers_db = pd.read_pickle('data/villagers_clean.pkl')

def get_villager_lookup(database) -> dict:
        """
        To convert the items in the gift columns into a dictionary to have a numerical value to be used for the scoring
        :param database: DataFrame imported from the notebook. It should contain all the data values of each villager
        :return: A dictionary for each item in a villagers_db gifts columns has numerical value
        """
        villager_lookup = {}
        for name, row in database.iterrows():
                villager_lookup[name] = {}
                for item in row['Specific Loved Gifts']:
                        villager_lookup[name][item] = 3
                for item in row['Specific Liked Gifts']:
                        villager_lookup[name][item] = 1
                for item in row['Specific Disliked Gifts']:
                        villager_lookup[name][item] = -1
                for item in row['Specific Hated Gifts']:
                        villager_lookup[name][item] = -3
                for item in row['Loved Movies']:
                        villager_lookup[name][item] = 1

        return villager_lookup

def get_choices() -> list:
        """
        Converting dictionaries into a master list
        :return: a list containing random choices chosen through stratified and true random sampling
        """
        gift_categories = {
                "Gems & Minerals": [
                        "Amethyst", "Aquamarine", "Emerald", "Gold Bar", "Iridium Bar", "Jade", "Omni Geode",
                        "Ruby", "Topaz", "Diamond", "Radioactive Bar", "Tigerseye", "Frozen Tear", "Obsidian",
                        "Quartz", "Copper Bar", "Iron Bar", "Radioactive Ore", "Prismatic Shard", "Cinder Shard",
                        "Coal", "Gold Ore", "Iridium Ore", "Refined Quartz"
                ],
                "Crops and Fruits": [
                        "Pumpkin", "Pomegranate", "Coconut", "Cauliflower", "Strawberry", "Melon", "Cactus Fruit",
                        "Hot Pepper", "Ginger", "Snow Yam", "Spring Onion", "Wild Horseradish", "Salmonberry",
                        "Blackberry", "Crystal Fruit", "Amaranth", "Spice Berry", "Grape", "Hops"
                ],
                "Flowers and Forageables": [
                        "Sunflower", "Poppy", "Crocus", "Daffodil", "Sweet Pea", "Dandelion", "Holly", "Leek",
                        "Common Mushroom", "Hazelnut", "Chanterelle", "Magma Cap", "Morel", "Purple Mushroom",
                        "Winter Root", "Red Mushroom"
                ],
                "Artisan Goods": [
                        "Cloth", "Coffee", "Pickles", "Truffle Oil", "Wine", "Goat Cheese", "Beer", "Oak Resin",
                        "Pine Tar",
                        "Sugar", "Mystic Syrup", "Cheese", "Maple Syrup", "Honey", "Mead", "Pale Ale",
                        "Duck Mayonnaise",
                        "Mayonnaise"
                ],
                "Cooked Meals": [
                        "Banana Pudding", "Blackberry Cobbler", "Chocolate Cake", "Spicy Eel", "Complete Breakfast",
                        "Salmon Dinner", "Artichoke Dip", "Fiddlehead Risotto", "Crab Cakes", "Tom Kha Soup",
                        "Survival Burger", "Fruit Salad", "Pink Cake", "Coffee", "Super Meal", "Poppyseed Muffin",
                        "Salad", "Stir Fry", "Vegetable Medley", "Cheese Cauliflower", "Miner's Treat",
                        "Pepper Poppers",
                        "Rhubarb Pie", "Red Plate", "Roots Platter", "Maple Bar", "Pizza", "Mango Sticky Rice",
                        "Pumpkin Soup",
                        "Sashimi", "Field Snack", "Fried Eel", "Ice Cream", "Rice Pudding", "Blueberry Tart", "Bread",
                        "Cookie", "Cranberry Sauce", "Fried Mushroom", "Glazed Yams", "Hashbrowns", "Pancakes",
                        "Carp Surprise",
                        "Fried Egg", "Tortilla", "Algae Soup", "Pale Broth", "Fish Taco", "Maki Roll", "Piña Colada",
                        "Farmer's Lunch",
                        "Omelet"
                ],
                "Fish & Sea": [
                        "Pufferfish", "Lobster", "Squid Ink", "Sandfish", "Octopus", "Squid", "Flounder", "Clam",
                        "Seaweed",
                        "Sea Cucumber", "Super Cucumber", "Coral", "Nautilus Shell", "Rainbow Shell"
                ],
                "Animal Products": [
                        "Duck Feather", "Wool", "Truffle", "Void Egg", "Dinosaur Egg", "Duck Egg", "Goat Milk",
                        "Large Goat Milk",
                        "Rabbit's Foot"
                ],
                "Books & Collectibles": [
                        "Monster Compendium", "Jack Be Nimble, Jack Be Thick", "Combat Quarterly", "Mining Monthly"
                ],
                "Random": [
                        "Parrot Egg", "Battery Pack", "Dwarf Gadget", "Frog Egg", "Ancient Sword", "Basilisk Paw",
                        "Bone Flute", "Driftwood", "Joja Cola", "Clay", "Bone Fragment"
                ]
        }

        category_cap = [7, 7, 3, 4, 14, 3, 4, 2, 3]
        count = 0
        random_choices = []
        flat_list = []
        for category in gift_categories:
                picks = (random.sample(gift_categories[category], category_cap[count]))
                random_choices.extend(picks)
                count += 1
                flat_list.extend(gift_categories[category])

        random_choices.extend(random.sample(sorted(set(flat_list) - set(random_choices)),28))

        random.shuffle(random_choices)
        chunk_size = 5
        random_choices = [random_choices[i:i + chunk_size] for i in range(0, len(random_choices), chunk_size)]

        return random_choices

def run_quiz() -> list:
        """"
        Runs the quiz that containts a 4 introduction quiz and 15 multiple choice of pick your favorite.
        :return: a list that should contain 2 list inside. One for the introduction questions, and the one for the multiple choice one.
        """
        all_answers = []
        intro_answers = []
        while True:
                answer = input("What is your favorite season. (Spring, Summer, Fall, Winter): ")
                if answer.capitalize() in ["Spring", "Summer", "Fall", "Winter"]:
                        intro_answers.append(answer.capitalize())
                        break
                else:
                        print("Choose only from the following choices: Spring, Summer, Fall, Winter")

        while True:
                try:
                        answer = int(input("What is your favorite day of the month. (1-28): "))
                        if answer >= 1 and answer <= 28:
                                intro_answers.append(answer)
                                break
                        else:
                                print("Choose only from the following range: 1-28")
                except ValueError:
                        print('Invalid input.')

        while True:
                print(f"From from the following.\n{villagers_db['Interest'].tolist()}")
                answer = input("What is your interest: ")
                if answer.capitalize() in villagers_db['Interest'].tolist():
                        intro_answers.append(answer.capitalize())
                        break

                else:
                        print("Choose only among the following choices: ")
                        print(villagers_db['Interest'].tolist())

        # referece for chocies for movie genres
        movie_genres = {
                "Horror": ["It Howls In The Rain"],
                "Mystery": ["Mysterium"],
                "Comedy": ["Wumbus"],
                "Romance": ["The Miracle At Coldstar Ranch"],
                "Adventure": ["The Zuzu City Express", "Journey Of The Prairie King: The Motion Picture"],
                "Documentary": ["Natural Wonders: Exploring Our Vibrant World"],
                "Family": ["The Brave Little Sapling"]
        }

        while True:
                print(f"From from the following.\n{list(movie_genres.keys())}")
                answer = input("What is your favorite movie genre: ")
                if answer.capitalize() in list(movie_genres.keys()):
                        intro_answers.append(answer.capitalize())
                        break

                else:
                        print("Choose among the following choices: ")
                        print(list(movie_genres.keys()))

        all_answers.append(intro_answers)

        mul_answers = []
        random_choices = get_choices()
        for choices in random_choices:
                while True:
                        try:
                                print(choices)
                                answer = int(input("Choose from the following. Answer in 1-5: "))
                                if answer >= 1 and answer <= 5:
                                        mul_answers.append(answer)
                                        break
                                else:
                                        print("Choose from the following range. (1-5)")

                        except ValueError:
                                print("Invalid output.")

        all_answers.append(mul_answers)

        return all_answers

def calculate_scores(answers: list, villagers_lookup:dict) -> dict:
        """
                desc here: yoko na
        :param answers:
        :param villagers_lookup:
        :return:
        """
        pass

def show_results(scores) -> str:
        """"
        :param scores:
        """
        pass

def main() -> None:
        run_quiz()

if __name__ == '__main__':
    main()