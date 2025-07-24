#23/07/2025
class mental_hos:
    def __init__(self):
        self.called = False
        self.has_called = False 
    
    def check(self,checking):
        self.called = True
        return f"The paitient is mentally unstable assuming by ppl around,{checking}"
    
    def dr(self,dr_check,prescribtion):
        self.has_called = True
        if self.called:
            return f"Report by doctor,{dr_check} and prescribed,{prescribtion}"
        else:
            return "First check the behaviour of the paitent by ppl around and then take to hospital"
    def medical_facility(self,suggestion,medication,time):
        if self.called and self.has_called:
            return f"The doctor suggest to {suggestion}, medication,{medication} and duration of time to cure {time}"
        else:
            if self.called:
                return "Consult with the dr first"
            if self.has_called:
                return "First check the behaviour"
            else:
                return "First check the behaviour and consult with the dr first"
            
paitent = mental_hos()
print(paitent.check("yes"))
print(paitent.dr("yes","prescribed to neurologist"))
print(paitent.medical_facility("dr suugest to admit","tablets and meditation","6 months"))
