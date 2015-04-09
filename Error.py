class Error(Exception):
    pass

class NotSixError(Error):
    def __init__(self):
        print "YOU MUST SELECT SIX NUMBERS"
class DistinctError(Error):
    def __init__(self):
        print "YOUR INPUTS DISTINCT NUMBERS"
class OverRangeError(Error):
    def __init__(self):
        print "YOUR INPUT IS NOT IN RANGE(1~45)"