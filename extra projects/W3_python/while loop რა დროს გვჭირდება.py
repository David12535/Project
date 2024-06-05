# როდესაც გვჭირდება რამე პროცესის გაშვება მინიმუმ ერთხელ.
# როდესაც გვინდა განათავსება კონკრეტულ შემთხვევაში, სანამ კონკრეტული პირობა არ გამოიყენება.
# როდესაც გვინდა დამთავრება კონკრეტულ შემთხვევაში, სანამ პირობა არ გამოიყენება.
# აქვე მაქვს მაგალითები:

# როდესაც გვჭირდება ინფორმაციის შესატანა მომავალი შემთხვევებისთვის:

user_input = ""
while user_input != "quit":
    user_input = input("Type 'quit' to exit: ")
    print("You typed:", user_input)
#როდესაც გვინდა რაიმე პროცესის შესრულება შემთხვევების გამო:
count = 0
while count < 5:
    print("The count is:", count)
    count += 1
#როდესაც გვინდა კონკრეტული შემთხვევის დროს დამთავრება:

import random

while True:
    random_number = random.randint(1, 10)
    print("Random number is:", random_number)
    if random_number == 7:
        print("Lucky number 7!")
        break  