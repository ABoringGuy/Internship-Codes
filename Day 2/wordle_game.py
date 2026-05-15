import random
no_of_guess=6

answer_word=random.choice(["APPLE","BLANK","BLIND","BROWN","CROWN"])
while no_of_guess > 0:
    guess=input("Enter your guess:").upper()#upper() converts the Input to Uppercase

    if(len(guess)!=5):
        print("Word can only have 5 letters")
        continue#Skips current iteration
    if guess==answer_word:
        print("Correct Guess")
        break#Break lets us get out of Loop if guess is correct
    no_of_guess-=1

    correct_letters= set()#set() is used to store multiple items in single variable. Here it stores correct letters
    for letter, correct in zip(guess, answer_word):#zip(a,b) connects the items of same order in a & b. Here it connects each letter from Guess in Letter and Answer_word in correct
        if letter == correct:
            correct_letters.add(letter)#Only add correct letters

    misplaced_letters = set(guess) & set(answer_word) - correct_letters#set(guess) & set(answer_word) seperates letter contained on both guess and answer_word. It then substracts the correct_letters giving misplaced letters.
    wrong_letters= set(guess) -set(answer_word)

    print("Correct Letters:", sorted(correct_letters))
    print("Incorrect Letters:", sorted(wrong_letters))
    print("Misplaced Letters:", sorted(misplaced_letters))

print("Answer was", answer_word)

