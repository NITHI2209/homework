#23/07/2025
class mental_hos:
    def __init__(self):
        self.called = False
        self.has_called = False 
    
    def check(self,checking):
        self.called = True
        return f"The paitient is mentally unstable assuming by ppl around,{checking}"
    
    def dr(self,dr_check):
        self.has_called = True
        if self.called:
            return f"Report by doctor,{dr_check}"
        else:
            return "First check the behaviour of the paitent by ppl around and then take to hospital"
    def medical_facility(self,suggestion):
        if self.called and self.has_called:
            return f"The doctor suggest to {suggestion}"
        else:
            if self.called:
                return "Consult with the dr first"
            if self.has_called:
                return "First check the behaviour"
            else:
                return "First check the behaviour and consult with the dr first"
            
paitent = mental_hos()
print(paitent.check("yes"))
print(paitent.dr("yes"))
print(paitent.medical_facility("dr suugest to admit"))
