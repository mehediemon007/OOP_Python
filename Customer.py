from Mobile import *


class Customer(Mobile):

     #inheritance

    def __init__(self, name, mobileNumber, address, ram, sim, rom, color, displaySize, purchaseDetails):

         self.name = name
         self.mobileNumber = mobileNumber
         self.address = address
         #call parent class(super class) __init__()
         super().__init__(ram, sim, rom, color, displaySize)
         #aggregation
         self.purchaseDetails = purchaseDetails

