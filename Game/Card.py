import random  
class Card:


    def __init__(self):

        self.card_number1 = 0
        self.num_turns = 0
        self.card_number2 = 0 
        self.point_total = 0 
    
    def card(self):
        self.card_number1 = random.randint(1,13)
        self.num_turns += 1

    def high(self):


        if self.card_number2 > self.card_number1:
            return self.point_total + 100
        elif self.card_number2 < self.card_number1:
            return self.point_total - 75
    
    def low(self):
        if self.card_number2 < self.card_number1:
            return self.point_total + 100
        elif self.card_number2 > self.card_number1:
            return self.point_total - 75

#does this work?.

print("hello world")