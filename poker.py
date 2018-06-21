import re
"""
Python version : 2.7.14

"""

def make_cards_from_input(strInput):
    # declare var to store cards and return 
    list_cards = list()
    regex = re.findall(r"((S|H|D|C)([2-9]|10|J|Q|K|A))", strInput)
    for i in regex:
        list_cards.append(i[0])
    return list_cards

def check_input(strInput): # must review?
    list_cards = make_cards_from_input(strInput)
    make_str = ''.join(list_cards)
    return True if len(list_cards) == 5 and make_str == strInput else False

class card():
    def __init__(self,card_info):
        if len(card_info) == 2:
            self.rank = card_info[1]
            self.suit = card_info[0]
        else:
            self.rank = card_info[1:]
            self.suit = card_info[0]

    @property # read-only 
    def get_rank(self):
        return self.rank

    @property # read-only
    def get_suit(self):
        return self.suit

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
        return "You dont have any typed..Good luck ^^"

            
if __name__ == "__main__":
    while(True):
        text_input = raw_input("Enter a input string: ")
        status = check_input(text_input)
        if status == False:
            print "Input is failed, please enter again.. "
        else:
            break

    list_cards = make_cards_from_input(text_input)
    # make card object for each element in list_cards
    cards = map(lambda x:card(x),list_cards)
    # make game object
    poker = game(cards)
    # call method
    poker.set_max_and_temp()
    # get output to print
    output = poker.return_output()
    # print output
    print output
