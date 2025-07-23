#23/07/2025
class college_bus:
    def __init__(self):
        self.called = False
        self.has_called = False
     
    def college_bus_application(self,student_name,dept,year):
        self.called = True
        return f"NAME = {student_name} , DEPT = {dept} ,YEAR = {year}"
    
    def bus_route(self,bus_route,bus_no):
        self.has_called = True
        if self.called:
            return f"BUS ROUTE = {bus_route} , BUS NO =  {bus_no}"
        else:
            return f"First complete the application form"
    
    def boarding(self,boarding_point):
        if self.called and self.has_called:
            return f"BOARDING POINT = {boarding_point}"
        else:
            if self.called:
                return "First update bus route and bus number"
            if self.has_called:
                return "First fill the application form"
            else:
                return "First fill the application form and update bus route, bus number"
            
student = college_bus()
print(student.college_bus_application("DHARANI","BTECH","2016-2019"))
print(student.bus_route("THIRUPORUR TO KELAMBAKKAM","101A"))
print(student.boarding("SENGAMAL"))
