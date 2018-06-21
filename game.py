

class game():
    def __init__(self,list_cards):
        self.list_cards = list_cards
        # number each of the rank
        self.temp = {'2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '10':0, 'J':0, 'Q':0, 'K': 0, 'A':0}
        self.max = 0 # {'2':1,'3':1,..'Q':0,'K':3} => self.max = 3

    def set_max_and_temp(self):
        for card in self.list_cards:
            # if temp have a rank,add 1
            if card.get_rank in self.temp.keys():
                self.temp[card.get_rank]+=1
        self.max = max(self.temp.values())
    
    def return_output(self):
        #####
        # if max = 4 => FourCard
        # if max = 3 => Full House or Three Cards
        # if max = 2 => Two Pair or One Pair
        #####
        if self.max == 4:
            return '4C'
        if self.max == 3:
            return 'FH' if 2 in self.temp.values() else '3C'
        if self.max == 2:
            return '2P' if self.temp.values().count(2) == 2 else '1P'
        return "--"