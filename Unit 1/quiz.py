# Create a new document called quiz1.py copy/ paste the following questions
# on your document and answer the following questions.

# quiz rules:
# - There is no talking during the quiz
# - You may only use your classnotes and w3schools.com for reference
# - If you have a question about a quiz question, please raise your hand
# - Once finished, submit your code to your repository using the source control 
# button. Your commit should be "completed quiz 1."

'note: all written responses should be written/ formatted as strings.'

# 1. In your own words, describe the differences between a linear search and a 
# binary search. Please write your response using complete sentences.\
Answer1: = "linear search is a method for finding a specific value in a list by checking each element one by one from the beginning to the end. It works on both sorted and unsorted lists."
    "Binary search, on the other hand, is a more efficient method that works only on sorted lists. It starts by checking the middle element of the list and compares it to the target value"

# 2. How many steps would it take to get to the desired number of 98 using linear search?
# Please write your response using complete sentences.
Answer2: = "it would take 6 steps to find the number 98 using a linear search in the given list, because the search checks each element one by one until it finds the target number."

listA = [10,24,34,35,67,98,101]

# 3. How many steps would it take to get to the desired number of 150 using a binary search?
# Please write your response using complete sentences.
listB = [1,40, 44, 55, 70, 93, 99, 134, 145, 150, 200, 244]
Answer3: = "it would take 2 steps to find the number 150 using a binary search in the given sorted list, because the search divides the list in half."

# 4. In your own words describe what an algorithm is. 
# Please write your response using complete sentences.
Answer4: = "An algorithm is a step-by-step set of instructions or rules designed to perform a specific task or solve a particular problem."
    
# 5. A person and their family is visiting a medical building. the medical building has
# 10 floors. The patient that the person and their family is visiting is on the 7th floor 
# of the building. The family also knows what room they need to go to to visit the
# patient on the 7th floor. which big-O time complexity would best describe the steps it
# would for them to get to the desired room and why? 
# Please write your response using complete sentences.
Answer5 ="The best big-O time complexity to get to floor 7 is using binary search so that the elevator can quickly reach the floor the need to go to quickly by dividing the number of floors in half."

# 6. You and your friends are headed out to a party, as you're preparing to walk out the door to meet with
# your pals, your realize you forgot your phone. you you can't remember exactly where you misplaced it 
# but you know it is in one of your pairs of pants. You have 10 pairs of paints. which big-O time complexity
# would best describe the steps it would take to find your phone?
# Please write your response using complete sentences.
Answer6 = "The best big-O time complexity to find the phone is linear search because you would need to check each pair of pants one by one until you find the phone."

# 7. Create a class that will represent and create game console objects. 
# Your class should have 4 attributes and 3 methods. 
# Once you've created your class, create 2 unique video game consoles.
class GameConsole:
    def __init__(self, brand, model, storage, color):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.color = color
        
consoleA = GameConsole("Sony", "PlayStation 5", "825GB", "White")
consoleB = GameConsole("Microsoft", "Xbox Series X", "1TB", "Black")

def power_on(self):
        print(f"{self.brand} {self.model} is now powered on.")

def power_off(self):
        print(f"{self.brand} {self.model} is now powered off.")

def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model}.")

# 8. Create a class that will represent a video game for your console.
# Your class should have 4 attributes and 3 methods objects.
# ONCE You've created your class, create 2 unique video games objects.. 
class VideoGame:
    def __init__(self, title, genre, platform, rating):
        self.title = title
        self.genre = genre
        self.platform = platform
        self.rating = rating
    
game1 = VideoGame("Sekiro: Shadows Die Twice", "Action-Adventure", "PlayStation 5", "Mature")
game2 = VideoGame("Grand Theft Auto V", "Action-Adventure", "Xbox Series X", "Mature")