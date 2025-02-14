import requests
import json

# url = "https://deckofcardsapi.com/"
# response = requests.get(url)
# print(response.json())
# data = response.json()
# with open ("bitcoindump.json", "w") as fp:
#    json.dump(data, fp)

# euroPriceObject = data["bpi"]["EUR"]
# rate = euroPriceObject["rate"]
# print(rate)

# Step 1: Shuffle the deck
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)
print(response.json()) 

data = response.json()
deck_id = data["deck_id"]

with open ("deckofcards.json", "w") as fp:
    json.dump(data, fp)

# Step 2: Draw 5 cards
url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
response = requests.get(url)
print(response.json())  # Print the card draw response for debugging

cards = response.json()["cards"]

# Step 3: Print each card's value and suit
for card in cards:
    print(f"{card['value']} of {card['suit']}")