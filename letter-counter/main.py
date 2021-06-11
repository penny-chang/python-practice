welcome_message = "Welcome to Letter Counter! This is an mini project that takes a message and a letter from you.\n" \
                  "The application task is to count how many times this letter occurred in the given message \n" \
                  "and also to calculate its percentage appeared."

print(welcome_message)
user_message = input("Please enter your message:")
user_letter = input("Please enter the letter you want to count:")

print("Your message:{}".format(user_message))
print("Your letter:{}".format(user_letter))

letter_count = user_message.count(user_letter)
letter_percentage = letter_count / len(user_message) * 100.00

print("The letter '{}' occurred {} time(s)".format(user_letter,letter_count))
print("The percentage of this letter '{}' occurrence is {}%".format(user_letter,letter_percentage))
