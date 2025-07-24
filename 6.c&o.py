#23/07/2025
class grocery:
    def __init__(self):
        self.called = False
        self.has_called = False

    def dairy(self,dairy_products,fruits,veg):
        self.called = True
        return f"Dairy products:{dairy_products} ,fruits:{fruits} and veg:{veg}"
    
    def price(self,price_dairy,price_fruits,price_veg):
        self.has_called = True 
        if self.called:
            return f"Price of dairy:{price_dairy} ,price of fruits:{price_fruits} and price of veg:{price_veg}"
        else:
            return "First enter the product"
        
    def liters (self,lit,fruit_kg,veg_kg):
        if self.called and self.has_called:
            return f"Liter of the product:{lit} ,fruits:{fruit_kg} and veg:{veg_kg}"
        else:
            if self.called:
                return "First enter the price"
            if self.has_called:
                return "First enter the dairy product"
            else:
                return "First enter the dairy product and the price"
            
products = grocery()
print(products.dairy("Milk and curd","apple","tomato"))
print(products.price("34 and 24","40","30"))
print(products.liters("2L and 1L","1kg","2kg"))
