#23/07/2025
class information_technology:
    def __init__(self):
        self.called = False
        self.has_called = False
    
    def staff_count(self,no_of_employee):
        self.called = True
        return f"Number of employee = {no_of_employee}"
    
    def majority_dept(self,majority_of_employee_dept,reason):
        self.has_called = True
        if self.called:
            return f"Majority of employee = {majority_of_employee_dept}, Reason = {reason}"
        else:
            return  "First update the staff count"
    
    def solution(self,solution):
        if self.called and self.has_called:
            return f"solution to solve problem = {solution}"
        else:
            if self.called:
                return "First address the problem"
            if self.has_called:
                return "First update the staff count"
            else:
                return "First update staff count and address the problem"
    
employee_info = information_technology()
print(employee_info.staff_count(100))
print(employee_info.majority_dept("IT","Because lack of facility in other dept"))
print(employee_info.solution("Improve  work environment and work life balance"))
