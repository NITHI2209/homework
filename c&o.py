#22/07/2025
class mrng_routine:
    def __init__(self):
        self.fun_called = False
    def brushing(self):
        self.fun_called = True
        return "brush your teeth" 
    def face_wash(self):
        if self.fun_called:
            return "wash your face"
        else:
            return "brush your teeth first"
    def coffee_drink(self):
        if self.fun_called:
            return "drink coffee"
        else:
            return "brush your teeth first"

nithi = mrng_routine()
print(nithi.face_wash())
print(nithi.brushing())
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
        
