

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