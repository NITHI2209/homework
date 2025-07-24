#23/07/2025
class gym:
    def __init__(self):
        self.called = False
        self.has_called = False
    
    def warmupp(self,warmup,time):
        self.called = True
        return f"warm-up:{warmup}, Time:{time}"
    
    def chest_workout(self,workout,time_chest_workout):
        self.has_called = True
        if self.called:
            return f"workout:{workout},Time:{time_chest_workout}"
        else:
            return "Do warmup first"
    
    def shoulder(self,exercise,time_shoulder,total_workout):
        if self.called and self.has_called:
            return f"exerice:{exercise},time for shoulder:{time_shoulder},total workout:{total_workout}"
        else:
            if self.called:
                return "Do chest workout now"
            if self.has_called:
                return "Do warmup first then do shoulder workout"
            else:
                return "Do warmup and chest workout now then do shoulder"

gymrat = gym()
print(gymrat.warmupp("pushups and pullups","5mins"))
print(gymrat.chest_workout("dumbell press","5 mins"))
print(gymrat.shoulder("Front raise","10 mins","1hr"))
