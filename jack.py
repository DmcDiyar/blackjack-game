import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        self.listOfCards = []
        for suit in suits:
            for rank in ranks:
                self.listOfCards.append(Card(suit, rank))
    
    def shuffle(self):
        random.shuffle(self.listOfCards)

    def deal_one(self):
        return self.listOfCards.pop()
    
    def __str__(self):
        return f"Deck has {len(self.listOfCards)} cards."  # Düzeltme: __str__ sadeleştirildi

class Player: 
    def __init__(self, name):
        self.name = name
        self.all_cards = []
        self.chips = 100
    
    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == list:
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_cards)} cards."  # Düzeltme: İkinci __str__ kaldırıldı
    
    def bet(self):
        while True:
            try:
                amount = int(input(f"Current chips: {self.chips}, enter bet amount: "))  
                if amount > 0 and amount <= self.chips:
                    self.chips -= amount
                    return amount
                else:
                    print("Invalid bet! Please enter an amount less than or equal to your chips.")
            except ValueError:
                print("Please enter a valid integer!")  

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

while True:
    print("Welcome to Blackjack! Try to get as close to 21 as possible without going over.")
    deck = Deck()
    deck.shuffle()
    player = Player("Player")  
    dealer = Player("Dealer")  
    
    # Kart dağıtımı
    player.add_cards([deck.deal_one(), deck.deal_one()]) 
    dealer.add_cards([deck.deal_one(), deck.deal_one()])
    
    # Çip kontrolü
    if player.chips <= 0:
        print("Game over, no chips left!")  
        break
    
    # Bahis alma
    bet_amount = player.bet()
    print(f"{player.name} bet {bet_amount} chips. Remaining chips: {player.chips}")
    
    # Kartları gösterme
    print("\nYour cards:")
    for card in player.all_cards:
        print(card)
    print("\nDealer's cards:")
    print(dealer.all_cards[0])
    print("Hidden Card")

    playing = True
    while playing:
        action = input("Hit or Stand? (h/s): ").lower()
        while action not in ["h", "s"]:  # Düzeltme: Geçersiz giriş için kontrol eklendi.
            print("Invalid input! Please enter 'h' or 's'.")
            action = input("Hit or Stand? (h/s): ").lower()
        
        if action == "h":
            player.add_cards(deck.deal_one())
            print("\nYour cards:")
            for card in player.all_cards:
                print(card)
            player_total = calculate_hand(player.all_cards)
            print(f"{player.name}'s total: {player_total}")
            if player_total > 21:
                print("Player busts! Dealer wins!")
                playing = False
        elif action == "s":
            playing = False
    
    # Krupiye mantığı
    if player_total <= 21:  # Düzeltme: Krupiye sadece oyuncu bust olmadığında oynar.
        print("\nDealer's cards:")
        for card in dealer.all_cards:
            print(card)
        dealer_total = calculate_hand(dealer.all_cards)
        while dealer_total < 17:  # Düzeltme: Krupiye toplam 17 olana kadar kart çeker.
            dealer.add_cards(deck.deal_one())
            print(dealer.all_cards[-1])  # Yeni çekilen kartı göster.
            dealer_total = calculate_hand(dealer.all_cards)
        
        print(f"{player.name}'s total: {player_total}")
        print(f"{dealer.name}'s total: {dealer_total}")
        
        # Kazanma/kaybetme kontrolü
        if player_total > 21:  # Düzeltme: Oyuncu bust kontrolü tekrar yapıldı 
            print("Player busts! Dealer wins!")
        elif dealer_total > 21:
            print("Dealer busts! Player wins!")
            player.chips += 2 * bet_amount
        elif player_total > dealer_total:
            print("Player wins!")
            player.chips += 2 * bet_amount
        elif dealer_total > player_total:
            print("Dealer wins!")
        else:
            print("Push!") 
            player.chips += bet_amount
    
    print(f"Final chips for {player.name}: {player.chips}")
    
    # Tekrar oynama
    play_again = input("Play again? (y/n): ").lower()  # Düzeltme: play_again döngü dışına taşındı.
    while play_again not in ["y", "n"]:
        print("Invalid input! Please enter 'y' or 'n'.")
        play_again = input("Play again? (y/n): ").lower()
    if play_again != "y":
        print("Game over! Thanks for playing!")
        break
    player.all_cards = []  # Düzeltme: Yeni tur için kartlar sıfırlanıyor.
    dealer.all_cards = []