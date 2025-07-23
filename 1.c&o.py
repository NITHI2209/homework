#23/07/2025
class employee_info:
    def __init__(self):
        self.called = False
        self.has_called = False
    def info(self,name,age,department):
        self.called = True
        return f"Name = {name} , age = {age}, department ={department}"
    def salary_info(self,monthly_salary,per_annum):
        if self.called:
            return f"Monthly salary ={monthly_salary} , Perannum ={per_annum}"
        else:
            return "First updated your details"
    def edu_into(self,educational_status):
        if self.called and self.has_called:
            return f" Educational status = {educational_status}"
        else:
            if self.called:
                return "First update salary_info"
            if self.has_called:
                return "First update perosnal info"
            else:
                return "First update both perosnal and salary details"
    
employee =  employee_info()
print(employee.info("NITHYASREE",21,"DS"))
print(employee.salary_info("25k", "3L"))
print(employee.edu_into("BBA & MBA"))
