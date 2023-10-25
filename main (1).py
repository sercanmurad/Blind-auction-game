from replit import clear
#HINT: You can call clear() to clear the output in the console.
#1. Show logo from art.py
from art import logo
print(logo)


def find_highest_bidder(bidding_record):
  highest_bid=0
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner=bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}!!!")

bid_dictionary={} 
biding_finished=False
while not biding_finished:
  #2.Ask for name input
  name=input("Please enter your name: \n")
  #3.Ask for bid input
  bid=int(input("What is your bid: $ "))
  #4.Add name and bid into a dictionary as key and value.
  bid_dictionary[name] = bid
#5.Ask if there are other users who to bid
  should_countinue=input("Are there any other bidders? Type 'yes' or 'no'! ")
  if should_countinue == "no":
    biding_finished = True
    #6Find the highest bid 
    find_highest_bidder(bid_dictionary)
  elif should_countinue == "yes":
    clear()




    