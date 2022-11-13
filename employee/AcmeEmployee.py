from .EmployeeState import EmployeeState,Default

class AcmeEmployee(object):
    #object init  
    def __init__(self,nameEmp):
        self.hoursHistory = []
        self.name = nameEmp
        #init object with state default
        self.state = Default()
    
    def change(self, EmployeeState,date):
        #change state
        self.state.switch(EmployeeState,date,self)