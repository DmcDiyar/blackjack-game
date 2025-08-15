import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    return f"{self.rank} of {self.suit}"
  

class Deck:
  def __init__ (self):
    self.listOfCards = []
    for suit in suits:
      for rank in ranks:
        self.listOfCards.append(Card(suit,rank))
  def shuffle(self):
    random.shuffle(self.listOfCards)

  def deal_one(self):
    return self.listOfCards.pop()

class Player: 
  def __init__(self,name):
    self.name=name
    self.all_cards = []
    self.chips = 100

  def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."
  
  def remove_one(self):
    return self.all_cards.pop(0)

  def add_cards(self,new_cards):
    if type(new_cards) == list:
      self.all_cards.extend(new_cards)
    else:
      self.all_cards.append(new_cards)
  
  def __str__(self):
    return f"{self.name} has {len(self.all_cards)}"
  
  def bet(self):
    while True:
      try:
        amount = int(input(f"your suit chips {self.chips}: amout:"))
        if amount >0 and amount <= self.chips:
          self.chips -= amount
          return amount
        else:
          print("Invalid bet! Please enter an amount less than or equal to your chips.")
      except ValueError:
        print("please enter an interger")




def calculate_hand(cards):
    total = 0
    aces = 0
    for card in cards:
        if card.rank == "Ace": 
            aces += 1
        total += card.value 
    while total > 21 and aces > 0: 
        total -= 10
        aces -= 1
    
    return total 

