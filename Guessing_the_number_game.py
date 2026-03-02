import random
attempts = 0
print("Guess the number: ")
print("I am thinking a number between 1  and 100")
random_choose = random.randint(1,100)
print(random_choose)
choice = input("Choose a difficulty type 'easy' or 'hard' ").lower() 
if choice == 'easy':
    attempts = 10 
elif choice == 'hard':
    attempts = 5 
else:
    print("Please Enter the valid option")
for i in range(attempts):
    guess = int(input("Guess the number: "))
    if random_choose == guess:
        print("You win")
        break
    else:
        print("try again")
        
    if guess > random_choose:
        print("High")
    else:
        print('Low')
