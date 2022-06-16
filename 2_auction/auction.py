next_person = True
while next_person:
    bidders = {}
    name = input('What is your name?')
    bid = float(input('What is your bid?'))
    bidders[name] = bid
    other_bidders = input("Are there other users who want to bid?")
    if other_bidders == 'yes':
        continue
    else:
        next_person= False
        highest_bidder = ""
        highest_bid = 0
        for i in bidders:

            if bidders[i] > highest_bid:
                highest_bid = bidders[i]
                highest_bidder = i 
        print(f"Winner is {highest_bidder} at ${highest_bid}.")


            