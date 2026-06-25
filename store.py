class Store:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Store.count+=1

    def get_info(self):
        print(f"Price of the {self.name} is Rs.{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total products in store : {cls.count}")

    @staticmethod
    def cal_discount(price,discount):
        print(f"Discounted price = {price-(price*discount/100)}")

s1=Store("Watch",10_000)
s2=Store("Bag",500)

s1.get_info()
s2.get_info()
Store.get_count()
s1.cal_discount(10_000,14)
s2.cal_discount(5_00,10)

         