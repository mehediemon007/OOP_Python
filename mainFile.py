from Customer import *
from Product import *
from Purchase import *

product1 = Xiaomi_Note7(1000)
price1 = product1.SalePrice()

product2 = Xiaomi_Note7(500)
price2 = product2.SalePrice()

product3 = Xiaomi_Note8()
price3 = Xiaomi_Note8.SalePrice()

purchase1 = PurchaseDetails(price1, "21/10/2019", 2)
purchase2 = PurchaseDetails(price2, "21/11/2017", 1)
purchase3 = PurchaseDetails(price3, "21/11/2019", 1)


customer1 = Customer("Mehedi Hasan Emon", "01629795421", "Sherpur , Bogura", "2Gb", "Banglalink", "16Gb", "Black", "6.5''", purchase1)
customer2 = Customer("Farabi Siam", "01765752071", "Sherpur , Bogura", "1Gb", "GramaenPhone", "8Gb", "Black", "4.5''", purchase2)
customer3 = Customer("Sakib Knam", "01765752571", "Sherpur , Bogura", "4Gb", "GramaenPhone", "64Gb", "Black", "7.5''", purchase3)


if __name__ == "__main__":
    print(customer1.name, customer1.mobileNumber)
    print(customer1.ram, customer1.sim, customer1.rom, customer1.color, customer1.displaySize)
    print(customer1.purchaseDetails.price, customer1.purchaseDetails.purchaseDate, customer1.purchaseDetails.warranty)

    print("Customer2 Purchase Details:")
    print(customer2.purchaseDetails.price, customer2.purchaseDetails.purchaseDate, customer2.purchaseDetails.warranty)

    print("Product Name and Product Quantity:")
    print(Xiaomi_Note7.ProductName, Xiaomi_Note7.ProductQuantity)

    print("Customer3 Details:......")
    print(customer3.name, customer3.mobileNumber)
    print(customer3.ram, customer3.sim, customer3.rom, customer3.color, customer3.displaySize)
    print(customer3.purchaseDetails.price, customer3.purchaseDetails.purchaseDate, customer3.purchaseDetails.warranty)

    print("Product Name and Product Quantity:")
    print(Xiaomi_Note8.ProductName, Xiaomi_Note8.ProductQuantity)

    print("Try to change discount of Note_7 ")
    # product1.discount = 2000  #not possible this way because attribute make private
    product1.set_discountPrice(3000)
    print(product1.get_discountPrice())
    print(product1.SalePrice())

    # print("--------------------")
    #
    # print(Xiaomi_Note7.ProductBasePrice)
    # print(product1.ProductBasePrice)
    # print(product2.ProductBasePrice)
    #
    # Xiaomi_Note7.ProductBasePrice = 25000
    #
    # print(Xiaomi_Note7.ProductBasePrice)
    # print(product1.ProductBasePrice)
    # print(product2.ProductBasePrice)
    #
    # product1.ProductBasePrice = 30000
    #
    # print(Xiaomi_Note7.ProductBasePrice)
    # print(product1.ProductBasePrice)
    # print(product2.ProductBasePrice)

    print(purchase1.price)
    purchase1.ShowPayment()




