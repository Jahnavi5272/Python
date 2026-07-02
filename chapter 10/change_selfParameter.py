from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(janu, fro, to):
        print(f"Ticket is booked in train no: {janu.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no:{self.trainNo} is running")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(1000, 2000)}")

t = Train(369369)
t.book("Vizag", "Bengaluru")
t.getStatus()
t.getFare("Vizag", "Bengaluru")