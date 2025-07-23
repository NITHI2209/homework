#22/07/2025
class mrng_routine:
    def __init__(self):
        self.fun_called = False
        self.called = False
    def brushing(self):
        self.fun_called = True
        return "brush your teeth" 
    def face_wash(self):
        self.called = True
        if self.fun_called:
            return "wash your face"
        else:
            return "brush your teeth first"
    def coffee_drink(self):
        if self.fun_called and self.called:
            return "drink coffee"
        else:
            if self.fun_called:
                return "wash your face and drink coffee"
            if self.called:
                return "brush your teeth then drink coffee"
            else:
                return "brush your teeth first"
            
nithi = mrng_routine()
print(nithi.face_wash())
print(nithi.coffee_drink())
print(nithi.brushing())
print(nithi.face_wash())
print(nithi.coffee_drink())

class afternoon_routine:
    def __init__(self):
        self.has_called = False
        
    def attend_classes(self):
        self.has_called = True
        return "attend classes"
        
    def sleep(self):
        if self.has_called:
            return "you can sleep now"
        else:
            return "attend your classes first"

jeni = afternoon_routine()
print(jeni.sleep())
print(jeni.attend_classes())
print(jeni.sleep())

class eve_routine:
    def __init__(self):
        self.called = False
        
    def tea_drink(self):
        self.called = True
        return "drink tea"
    def study_time(self):
        
        if self.called:
            return "study now"
        else:
            return "drink your tea first"

jaisha = eve_routine()
print(jaisha.study_time())
print(jaisha.tea_drink())

class night_routine:
    def __init__(self):
        self.have_called = False
        
    def python_class(self):
        self.have_called = True 
        return "attend python classes"
        
    def nptel_class(self):
        if self.have_called:
            return "attend nptel course"
        else:
            return "attend your python classes first"
        
jayanthi = night_routine()
print(jayanthi.nptel_class())
print(jayanthi.python_class())
print(jayanthi.nptel_class())

class face_pack:
    def __init__(self):
        self.been_called = False 
        
    def rice_flour(self):
        self.been_called = True
        return "face pack time"
    def bed_time(self):
        if self.been_called:
            return "its bed time now"
        else:
            return "wear your face pack now then go to bed"

sriram = face_pack()
print(sriram.bed_time())
print(sriram.rice_flour())
print(sriram.bed_time())
        
class extra_work:
    def __init__(self):
        self.called = False
        self.has_called = False
    
    def aptitue(self):
        self.called = True
        return "study aptitue"
    
    def verbal(self):
        self.has_called = True
        if self.called:
            return "study verbal"
        else:
            return "first study aptitue"
    def logical(self):
        if self.called and self.has_called:
            return "study logical reasoning"
        else:
            if self.called:
                return "study verbal first then study logical"
            if self.has_called:
                return "study aptitue"
            else:
                return "study aptitue and verbal first then study logical"

name = extra_work()
print(name.logical())
print(name.aptitue())
print(name.verbal())
        

class college:
    def __init__(self):
        self.called = False 
        self.had_called = False
    
    def college_bus(self):
        self.called = True
        return "get into clg bus"
        
    def breakfast_at_clg(self):
        if self.called:
            return "go have your breakfast"
        else:
            return "first go to college through bus"
    def attend_clg_hours(self):
        if self.called and self.had_called:
            return "attend clg classes"
        else:
            if self.called:
                return "have breakfast first then attend classes"
            if self.had_called:
                return "first go to college through bus"
            else:
                return "first go to clg and have breakfast then attend classes"

college_student = college()
print(college_student.breakfast_at_clg())
print(college_student.college_bus())
print(college_student.attend_clg_hours())

class stock:
    def __init__(self):
        self.called = False
    
    def nifty(self):
        self.called = True 
        return "stock price is 23"
    
    def sensex(self):
        if self.called:
            return "market is going down"
        else:
            return "market is high"
            
stock_market = stock()
print(stock_market.nifty())
            
