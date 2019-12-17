from Payment import *


class PurchaseDetails:

    def __init__(self, price, purchaseDate, warranty):
        self.price = price
        self.purchaseDate = purchaseDate
        self.warranty = warranty
        self. payment1 = PaymentDetails(self.price, 22000)

    def ShowPayment(self):
        self.payment1.CalculatePayment()
