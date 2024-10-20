import random
import time
position = 0
questions = [
    "What is the capital of France?\nChoices: London, Berlin, Paris, Madrid",
    "Which animal is known as the 'king of the jungle'?\nChoices: Elephant, Tiger, Lion, Gorilla",
    "What is the largest planet in our solar system?\nChoices: Earth, Mars, Jupiter, Venus",
    "Which planet is known as the Red Planet?\nChoices: Saturn, Mars, Uranus, Neptune",
    "How many continents are there?\nChoices: 5, 6, 7, 8",
    "What is the name of the toy cowboy in Toy Story?\nChoices: Woody, Buzz, Rex, Jessie",
    "Which holiday celebrates the birth of Jesus Christ?\nChoices: Thanksgiving, Christmas, Halloween, Easter",
    "Who painted the Mona Lisa?\nChoices: Van Gogh, Picasso, Leonardo da Vinci, Michelangelo",
    "What is the main ingredient in guacamole?\nChoices: Tomato, Avocado, Onion, Pepper",
    "What is the largest ocean on Earth?\nChoices: Atlantic, Indian, Arctic, Pacific",
    "In which country did the Olympic Games originate?\nChoices: Greece, Italy, Egypt, China",
    "Which of these is a primary color?\nChoices: Green, Purple, Blue, Orange",
    "What is the largest mammal in the world?\nChoices: Elephant, Whale, Giraffe, Shark",
    "How many bones are there in the adult human body?\nChoices: 206, 208, 210, 202",
    "What is the hardest natural substance on Earth?\nChoices: Gold, Iron, Diamond, Silver",
    "Which country is known as the Land of the Rising Sun?\nChoices: China, Japan, Thailand, South Korea",
    "What is the largest island in the world?\nChoices: Australia, Greenland, Borneo, Madagascar",
    "What is the name of the fairy in Peter Pan?\nChoices: Wendy, Tinker Bell, Aurora, Cinderella",
    "What is the most common gas in Earth’s atmosphere?\nChoices: Oxygen, Carbon Dioxide, Nitrogen, Hydrogen",
    "What is the smallest prime number?\nChoices: 1, 2, 3, 4",
    "Which animal is the fastest on land?\nChoices: Lion, Cheetah, Gazelle, Horse",
    "Which famous scientist developed the theory of relativity?\nChoices: Isaac Newton, Albert Einstein, Nikola Tesla, Galileo Galilei",
    "In which year did the Titanic sink?\nChoices: 1912, 1905, 1921, 1898",
    "Which of these elements is a noble gas?\nChoices: Hydrogen, Helium, Oxygen, Nitrogen",
    "In what movie would you find a character named Darth Vader?\nChoices: Star Trek, Star Wars, Guardians of the Galaxy, Lord of the Rings",
    "What is the longest river in the world?\nChoices: Nile, Amazon, Mississippi, Yangtze",
    "What is the main ingredient in the dish 'sushi'?\nChoices: Rice, Noodles, Fish, Seaweed",
    "Which planet is known for having rings around it?\nChoices: Jupiter, Uranus, Saturn, Neptune",
    "Who wrote the famous play 'Romeo and Juliet'?\nChoices: Charles Dickens, Jane Austen, William Shakespeare, Mark Twain",
    "What is the square root of 64?\nChoices: 6, 7, 8, 9",
    "What is the capital city of Canada?\nChoices: Toronto, Ottawa, Vancouver, Montreal",
    "Which famous artist is known for cutting off his own ear?\nChoices: Claude Monet, Vincent van Gogh, Pablo Picasso, Andy Warhol",
    "What does the chemical symbol 'Na' represent?\nChoices: Nickel, Sodium, Nitrogen, Neon",
    "Which of these is not a prime number?\nChoices: 5, 13, 15, 23",
    "In what year did the Berlin Wall fall?\nChoices: 1961, 1989, 1975, 1991",
    "Which artist painted the 'Starry Night'?\nChoices: Claude Monet, Jackson Pollock, Vincent van Gogh, Pablo Picasso",
    "What does DNA stand for?\nChoices: Deoxyribonucleic Acid, Deoxynucleic Acid, Dicarboxyl Nucleotide Acid, Deoxyribose Nucleotide Acid",
    "What is the currency of Japan?\nChoices: Yen, Won, Baht, Peso",
    "Which element has the atomic number 1?\nChoices: Helium, Hydrogen, Lithium, Oxygen",
    "What is the name of the largest desert in the world?\nChoices: Kalahari, Sahara, Arabian, Antarctic Desert",
    "Which scientist is credited with discovering the law of gravity?\nChoices: Galileo Galilei, Isaac Newton, Nikola Tesla, Albert Einstein",
    "Who invented the telephone?\nChoices: Thomas Edison, Alexander Graham Bell, Nikola Tesla, Michael Faraday",
    "Which of these countries has never been part of the United Kingdom?\nChoices: Ireland, Wales, Scotland, France",
    "Who was the first president of the United States?\nChoices: Thomas Jefferson, Abraham Lincoln, George Washington, John Adams",
    "Which gas do plants use for photosynthesis?\nChoices: Oxygen, Carbon Dioxide, Nitrogen, Hydrogen",
    "What is the largest volcano in the solar system?\nChoices: Mount Everest, Mount Vesuvius, Olympus Mons, Mount Fuji",
    "Who discovered penicillin?\nChoices: Louis Pasteur, Alexander Fleming, Marie Curie, Thomas Edison",
    "In what year did World War II end?\nChoices: 1940, 1945, 1950, 1942",
    "What is the tallest building in the world?\nChoices: Burj Khalifa, CN Tower, Empire State Building, Eiffel Tower",
    "What is the main ingredient in the Japanese dish 'tempura'?\nChoices: Tofu, Vegetables, Fish, Deep-fried vegetables and seafood"
]
answers = ["Paris",
    "Lion",
    "Jupiter",
    "Mars",
    "7",
    "Woody",
    "Christmas",
    "Leonardo da Vinci",
    "Avocado",
    "Pacific",
    "Greece",
    "Blue",
    "Whale",
    "206",
    "Diamond",
    "Japan",
    "Greenland",
    "Tinker Bell",
    "Nitrogen",
    "2",
    "Cheetah",
    "Albert Einstein",
    "1912",
    "Helium",
    "Star Wars",
    "Nile",
    "Rice",
    "Saturn",
    "William Shakespeare",
    "8",
    "Ottawa",
    "Vincent van Gogh",
    "Sodium",
    "15",
    "1989",
    "Vincent van Gogh",
    "Deoxyribonucleic Acid",
    "Yen",
    "Hydrogen",
    "Antarctic Desert",
    "Isaac Newton",
    "Alexander Graham Bell",
    "France",
    "George Washington",
    "Carbon Dioxide",
    "Olympus Mons",
    "Alexander Fleming",
    "1945",
    "Burj Khalifa",
    "Deep-fried vegetables and seafood"
]
prize = ['100\n', '150\n', '300\n', '600\n', '1.000\n', '2.500\n', '6.000\n', '11.000\n', '22.000\n', '35.000\n', '66.000\n', '99.000\n', '120.000\n', '250.000\n', '500.000']
answers_list_adjust = []
for i in answers:
    answers_list_adjust.append(i.strip())
prize_list_adjust = []
for j in prize:
    prize_list_adjust.append(j.strip())
for i in range(21): 
    what_question = ("Question {}/20:".format(position + 1))
    print(what_question)
    question_position = random.randint(1,51)
    question_appeared = []
    while question_position in question_appeared:
        question_position = random.randint(1,51)
    position += 1
    print(questions[question_position])
    user_answer = input("Type your answer here: ")
    if user_answer.lower() == answers[question_position].lower():
        print("Correct!")
        print("Your prize now is: ",prize_list_adjust[position],"USD!")
        continue_or_stop = input("Do you want to continue playing? You are at question {}. Yes or No: ".format(position + 1))
        if continue_or_stop.lower() == "yes".lower():
            question_appeared.append(question_position)
            print("Up to the next question!")
            time.sleep(0.5)
            continue
        elif continue_or_stop.lower() == "no".lower():
            print("You ended the game with the prize of {} USD!".format(prize_list_adjust[position]))
            print("Thank you for playing the game!")
            break
    else:
        if position == 1:
            print("You got your answer wrong in the first question, so you got no prize. Sad!")
            print("But it's fine, thank you!")
            break
        elif position > 1:
            print("You got your answer wrong. You ended the game with the prize of {} USD!".format(prize_list_adjust[0]))
            break
    if position == 20:
        print("You won the game with the grand prize of {} USD!".format(prize(14)))

