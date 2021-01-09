from art import logo

####
print(logo)
print ("Welcome to the secret auction program.")

contestants = []
collecting_bids = True

while collecting_bids == True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder = {"name":name, "bid":bid}
    contestants.append(bidder)
    more_bids = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if more_bids == "no":
        collecting_bids = False

winning_bid = {"name":"","bid":0}
for con in contestants:
    if con["bid"] > winning_bid["bid"]:
        winning_bid = con

print(f"The winning bid belongs to {winning_bid['name']} with a bid of ${winning_bid['bid']}")

