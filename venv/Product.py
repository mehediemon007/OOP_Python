class Xiaomi_Note7:
    ProductName = "Xiaomi Note 7"
    ProductQuantity = 100
    ProductBasePrice = 16500

    def __init__(self,discount):
        self.__discount = discount
        Xiaomi_Note7.ProductQuantity-=1

    def SalePrice(self):
        return Xiaomi_Note7.ProductBasePrice-self.__discount

    def set_discountPrice(self,discount):
        self.__discount = discount

    def get_discountPrice(self):
        return self.__discount

class Xiaomi_Note8:
    ProductName = "Xiaomi Note 7"
    ProductQuantity = 100
    ProductBasePrice = 20500
    DiscountPrice = 500

    def __init__(self):
        Xiaomi_Note8.ProductQuantity-=1

    @classmethod
    def SalePrice(cls):
        if Xiaomi_Note8.ProductBasePrice > 20000:
            giftValue = cls.__giftVauchar()
            return Xiaomi_Note8.ProductBasePrice-Xiaomi_Note8.DiscountPrice-giftValue

        else:
            return Xiaomi_Note8.ProductBasePrice-Xiaomi_Note8.DiscountPrice

    @staticmethod
    def __giftVauchar():
        giftValue = 100
        return giftValue


