from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
biddone = False
bids = {}
bidder = ""
bid = 0
while biddone == False:
  print(art.logo)
  bidder = input("Name of bidder: ")
  if bidder in bids:
    print(f"Your current bid is {bids[bidder]}.")
    bid = int(input("Increase your bid by (whole dollars only): $"))
    bids[bidder] += bid
  else:
    bid = int(input("What is your bid? (whole dollars only): "))
    bids[bidder] = bid
  if input("Are there more bidders? ('yes' or 'no'): ") == "no":
    biddone = True
  else:
    clear()
highestbidder = ""
highestbid = 0
for name in bids:
  if bids[name] > highestbid:
    highestbid = bids[name]
    highestbidder = name
clear()
print(art.logo)
print(f"The highest bidder is {highestbidder} with a bid of: ${highestbid}")

