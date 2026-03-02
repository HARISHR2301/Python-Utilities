import random 
print('Welcome to the Blackjack Game')
user_cards = []
computer_cards = []
con = True
while con == True:
    n = 2 
    for i in range(n):
        cards = int(input("Enter the cards: "))
        user_cards.append(cards)
        n -= 1 
        
    if sum(user_cards) <= 15:
        n = 1 
    
    n = 2 
    for i in range(n):
        cards = random.randint(1,11)
        computer_cards.append(cards)
        n -= 1 
        
    if sum(computer_cards) <= 15:
        n = 1 
    else:
        con = False
        
    
print(f"User_cards: {user_cards}") 
print(f"User_cards Sum: {sum(user_cards)} ")
print(f"Computer_cards: {computer_cards}")
print(f"Computer_cards: {sum(computer_cards)}")
if sum(user_cards) < 21 and sum(user_cards) > sum(computer_cards):
    print('User Wins')
elif sum(computer_cards) < 21 and sum(computer_cards) > sum(user_cards):
    print('Computer Wins')
else:
    print("Draw")

    
    
