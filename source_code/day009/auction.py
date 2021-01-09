from auctionart import logo

print(logo)
print("Welcome to the secret auction program!")
print()

bids = {}

def collect_bidder_info():
    print()
    name = input("Name: ")
    bid = int(input("Bid: $"))
    bids[name] = bid

collect_bidder_info()
while input("Another (yes/no): ") == "yes":
    collect_bidder_info()

winning = {
    "name": "no one",
    "bid": 0
}

for name in bids:
    this_bid = bids[name]
    if this_bid > winning["bid"]:
        winning["name"] = name
        winning["bid"] = this_bid

print(f"The winner is {winning['name']} with a bid of ${winning['bid']}!")