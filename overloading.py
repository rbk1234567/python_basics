print("overloading ---------------------------------------------------------------------------------------------------")

class stonepaperscizzors:
    def __init__(self,hand):
        self.hand = hand


    def __cmp__(self, other):
        result = ""
        if self.hand == "stone":
            if other.hand == "paper":
                result = "paper wins"
            elif other.hand == "scizzors":
                result = "stone wins"
            elif other.hand == "stone":
                result = "draw"
            else: result = "error on second hand"
        else:
            if self.hand == "paper":
                if other.hand == "stone":
                    result = "paper wins"
                elif other.hand == "scizzors":
                    result = "scizzors wins"
                elif other.hand == "paper":
                    result = "draw"
                else:
                    result = "error on second hand"
            else:
                if self.hand == "scizzors":
                    if other.hand == "stone":
                        result = "stone wins"
                    elif other.hand == "paper":
                        result = "scizzors wins"
                    elif other.hand == "scizzors":
                        result = "draw"
                    else:
                        result = "error on second hand"
                else:
                    result = "error on first hand"






        print("first hand has '{}' and second hand has '{}', the result is '{}'".format(self.hand,other.hand,result))

while True:
    hand1 = stonepaperscizzors(input("enter first hand [paper,stone,scizzors]"))
    hand2 = stonepaperscizzors(input("enter second hand [paper,stone,scizzors]"))
    hand1.__cmp__(hand2)
    if input("quit? [y = yes, any other key = play again]") == "y":
        break