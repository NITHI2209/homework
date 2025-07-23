#23/07/2025
class grocery:
    def __init__(self):
        self.called = False
        self.has_called = False

    def dairy(self,dairy_products):
        self.called = True
        return f"Dairy products,{dairy_products}"
    
    def price(self,price_product):
        self.has_called = True 
        if self.called:
            return f"Price,{price_product}"
        else:
            return "First enter the product"
        
    def liters (self,lit):
        if self.called and self.has_called:
            return f"Liter of the product,{lit}"
        else:
            if self.called:
                return "First enter the price"
            if self.has_called:
                return "First enter the dairy product"
            else:
                return "First enter the dairy product and the price"
            
products = grocery()
print(products.dairy("Milk and curd"))
print(products.price("34 and 24"))
print(products.liters("2L and 1L"))
