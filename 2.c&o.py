#23/07/2025
class hospital:
    def __init__(self):
        self.called = False
        self.has_called = False 
        self.has_been_called = False
    
    def paitient_details(self,name,age):
        self.called = True
        return f"NAME = {name} , AGE = {age}"
        
    def disease_diagonised(self,disease):
        self.has_called = True
        if self.called:
            return f"DISEASE = {disease} "
        else:
            return "Enter the paitient details first"
    def cure(self,cure_for_disease):
        self.has_beed_called =  True
        if self.called and self.has_called:
            return f"CURE = {cure_for_disease}"
        else:
            if self.called:
                return "First indentify the disease"
            if self.has_called:
                return "First update the paitient details"
            else:
                return "Update the paitient details and indentify disease"
    def tablet(self,tablet_name):
        if self.called and self.has_called and self.has_beed_called:
            return f"TABLET = {tablet_name}"
        else:
            if self.called:
                return "First indentify disease and identify the cure"
            if self.has_called:
                return "First update paitient details and indentify cure"
            if self.has_been_called:
                return "First update paitient details and indentify the diease"
            else:
                return "update paitient_details and disease and cure"

paitient_info = hospital()
print(paitient_info.paitient_details("SNEHA",44))
print(paitient_info.disease_diagonised("TB"))
print(paitient_info.cure("TABLETS"))
print(paitient_info.tablet("CITRAZIN"))
