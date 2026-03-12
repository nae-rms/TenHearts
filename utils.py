import pandas as pd
import random

def get_villager_lookup(database) -> dict:
        """
        To convert the items in the gift columns into a dictionary to have a numerical value to be used for the scoring
        :param database: DataFrame imported from the notebook. It should contain all the data values of each villager
        :return: A dictionary for each item in a database columns to have numerical value
        """
        villager_lookup = {}
        for name, row in database.iterrows():
                villager_lookup[name] = {}
                for item in row['Specific Loved Gifts']:
                        villager_lookup[name][item] = 5
                for item in row['Specific Liked Gifts']:
                        villager_lookup[name][item] = 3
                for item in row['Specific Disliked Gifts']:
                        villager_lookup[name][item] = -0.5
                for item in row['Specific Hated Gifts']:
                        villager_lookup[name][item] = -1
                for item in row['Loved Movies']:
                        villager_lookup[name][item] = 1

                villager_lookup[name][row['Birthday Season']] = 3
                villager_lookup[name][row['Birthday Day']] = 2
                villager_lookup[name][row['Interest']] = 4

        return villager_lookup

def get_choices() -> list:
        """
        Converting dictionaries into a master list
        :return: A list containing random choices chosen through stratified and true random sampling
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

        category_cap = [15, 13, 7, 7, 25, 8, 5, 2, 7]
        count = 0
        random_choices = []
        flat_list = []
        for category in gift_categories:
                picks = (random.sample(gift_categories[category], category_cap[count]))
                random_choices.extend(picks)
                count += 1
                flat_list.extend(gift_categories[category])

        random_choices.extend(random.sample(sorted(set(flat_list) - set(random_choices)),36))

        random.shuffle(random_choices)
        chunk_size = 5
        random_choices = [random_choices[i:i + chunk_size] for i in range(0, len(random_choices), chunk_size)]

        return random_choices

def run_quiz(database) -> list:
        """"
        Runs the quiz that containts a 4 introduction quiz and 15 multiple choice of pick your favorite.
        :return: A list that contain answers to the introduction questions, and the multiple choice one.
        """
        all_answers = []
        while True:
                answer = input("What is your favorite season. (Spring, Summer, Fall, Winter): ")
                if answer.capitalize() in ["Spring", "Summer", "Fall", "Winter"]:
                        all_answers.append(answer.capitalize())
                        break
                else:
                        print("Choose only from the following choices: Spring, Summer, Fall, Winter")

        while True:
                try:
                        answer = int(input("What is your favorite day of the month. (1-28): "))
                        if 1 <= answer <= 28:
                                all_answers.append(answer)
                                break
                        else:
                                print("Choose only from the following range: 1-28")
                except ValueError:
                        print('Invalid input.')

        interest_choices = database['Interest'].tolist()
        while True:
                print(f"From the following.\n{interest_choices}")
                answer = input("What is your interest: ")
                if answer.capitalize() in interest_choices:
                        all_answers.append(answer.capitalize())
                        break

                else:
                        print("Choose only among the following choices: ")
                        print(interest_choices)

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
                        all_answers.append(answer.capitalize())
                        break

                else:
                        print("Choose among the following choices: ")
                        print(list(movie_genres.keys()))


        random_choices = get_choices()
        for choices in random_choices:
                while True:
                        try:
                                print(choices)
                                answer = int(input("Choose from the following. Answer in 1-5: "))
                                if 1 <= answer <= 5:
                                        all_answers.append(choices[answer-1])
                                        break
                                else:
                                        print("Choose from the following range. (1-5)")

                        except ValueError:
                                print("Invalid output.")


        return all_answers

def calculate_scores(answers: list, villagers_lookup:dict) -> list:
        """
        Calculating the scores for the answers with the use of the villager_lookup function.
        :param answers: all_answers from the run_quiz function.
        :param villagers_lookup: The dictionary used to determine scores for each item in a villager's gifts' column
        :return: A dictionary that has scores for each key (villager name) and value (score)
        """
        all_villager_score = []

        for villager in villagers_lookup:
                score = 0
                for item in answers:
                        if item in villagers_lookup[villager]:
                                score += villagers_lookup[villager][item]

                all_villager_score.append(score)

        return all_villager_score

def show_results(database, scores):
        """"
        Showing the results, with the most compatible villager is rank 1.
        :param databaase: DataFrame imported from the notebook. It should contain all the data values of each villager
        :param scores: results of all villager score from calculate_scores function
        """
        villager_results = database[['Name']].copy()
        villager_results['Score'] = scores
        print(villager_results)
        highest_villager = villager_results.loc[villager_results['Score'].idxmax()]
        print(highest_villager)

def main() -> None:
        # loading / importing pkl file
        villagers_db = pd.read_pickle('data/villagers_clean.pkl')
        user_answers = run_quiz(villagers_db)
        villager_lookup = get_villager_lookup(villagers_db)
        scores = calculate_scores(user_answers, villager_lookup)
        show_results(villagers_db, scores)

if __name__ == '__main__':
    main()