class Patient :
    def __init__(self , name , last, age, sickness):
        self.name=name
        self.last=last
        self.age=age
        self.sickness=sickness
        
class Present(Patient):
    def __init__(self, name, last, age, sickness , present):
        super().__init__(name, last, age, sickness)
        self.present=present         
        
class Discharged(Patient):
    def __init__(self, name, last, age, sickness , discharged):
        super().__init__(name, last, age, sickness) 
        self.discharged=discharged
        
               
