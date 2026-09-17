from random import randint

class Train:
    def __init__(self, trainno, fro, to):
        self.trainno = trainno
        self.fro = fro
        self.to = to

    def book(self):
        print(f"Train ticket booked: {self.trainno} from {self.fro} to {self.to}")

    def getstatus(self):
        print(f"Train {self.trainno} is running successfully")

    def getfare(self):
        print(f"Ticket fare for train {self.trainno} from {self.fro} to {self.to} is {randint(200, 1000)}")

# create object
t = Train("GUJ123", "Gujarat", "Mumbai")

# call methods
t.book()
t.getstatus()
t.getfare()
