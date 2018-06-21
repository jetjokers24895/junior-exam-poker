import re
from card import card
from game import game


def make_cards_from_input(strInput):
    # declare var to store cards and return 
    list_cards = list()
    regex = re.findall(r"((S|H|D|C)([2-9]|10|J|Q|K|A))", strInput)
    for i in regex:
        list_cards.append(i[0])
    return list_cards

def check_input(strInput): # check input valid?
    list_cards = make_cards_from_input(strInput)
    make_str = ''.join(list_cards)
    # input must have five cards,and string after and string before must equal
    return True if len(list_cards) == 5 and make_str == strInput else False
   
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
