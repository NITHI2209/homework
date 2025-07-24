#23/07/2025
class parlour:
    def __init__(self):
        self.called = False
        self.has_called = False 

    def facial(self,enter_the_facial,price,duration):
        self.called = True
        return f"Facial:{enter_the_facial} ,price:{price} and duration:{duration}"
    
    def threading(self,type,price_for_threading,duration):
        self.has_called = True 
        if self.called:
            return f"Type for threading:{type} , price for threading:{price_for_threading},duration:{duration}"
        else:
            return "First do facial" 
        
    def upper_hair(self,type,price_for_upper_hair,time):
        if self.called and self.has_called:
            return f"Type for upper hair:{type}, price:{price_for_upper_hair}, time:{time}"
        else:
            if self.called:
                return "Do threading then do upper hair"
            if self.has_called:
                return "Do facial then upper hair first"
            else:
                return "Do facial and threading first"
            
customer = parlour()
print(customer.facial("skin brightining",1500,"1hr"))
print(customer.threading("Thread",45,"3mins"))
print(customer.upper_hair("wax",80,"5mins"))
