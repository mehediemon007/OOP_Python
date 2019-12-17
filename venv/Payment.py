from abc import ABC,abstractmethod

class PaymentFunction(ABC):

    def __init__(self):
       self.tag = True

    @abstractmethod
    def CalculatePayment(self):pass
    def showPaymentClarification(self):

        if self.Tag == True:
            print("Payment Done!")
        else:
            print("Due Payment")


class PaymentDetails(PaymentFunction):
    def __init__(self,TotalPrice,CustomerPay):
        self.TotalPrice = TotalPrice
        self.CustomerPay = CustomerPay
        # super().__init__()

    def CalculatePayment(self):
         if (self.CustomerPay-self.TotalPrice) >= 0:
             self.Tag = True


         else:
             self.Tag = False


         self.showPaymentClarification()



