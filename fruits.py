class Fruit: 
    def __init__(self, name, color, season, price):
        self.name = name
        self.color = color
        self.season = season
        self.price = float(price)
    
    #print fruit details
    def details(self): 
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Fruit Type: {self.name}
        Fruit Color: {self.color}
        Fruit Season: {self.season}
        Fruit Price: {self.price}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)
 
    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Total Cost of {self.name}: {total}
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """)


        
apple = Fruit("Apple", "Red", "Fall", "1.25")
pear = Fruit("Pear", "Green", "Summer", "1.75")
strawberry = Fruit("Strawberry", "Red", "Spring", "3.50")
blueberry = Fruit ("Blueberry", "Blue", "Spring", "2.00")

apple.details()
pear.details()
strawberry.details()
blueberry.details()


apple.calc_sales_tax(.04)
pear.calc_sales_tax(.04)
strawberry.calc_sales_tax(.04)
blueberry.calc_sales_tax(.04)

#print(f"Your fruit is {self.name}, the color is {self.color}, it is in season in {self.season}, and its price is {self.price}")