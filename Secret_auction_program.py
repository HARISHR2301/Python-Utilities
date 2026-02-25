print("Welcome to secret auction program")

bids = {}

while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: ₹ "))
    
    bids[name] = bid
    
    more = input("Are there other bidders? yes or no: ").lower()
    if more == "yes":
        print("\n" * 100)   # clears screen effect
    else:
        break

# Find winner
winner_name = ""
highest_bid = 0

for bidder, amount in bids.items():
    if amount > highest_bid:
        highest_bid = amount
        winner_name = bidder

print(f"The winner is {winner_name} with a bid of ₹{highest_bid}")
``
