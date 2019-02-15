import json

def demo(string):
    if string:
        upper = string.upper()
        rep = upper.replace("A", "BBBBBBB")
        # print ("match...", upper)
        return ((string, upper, rep))
