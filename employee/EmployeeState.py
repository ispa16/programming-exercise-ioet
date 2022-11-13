class EmployeeState(object):
    name = "state"
    date = ''
    def switch(self, state,workDate,employee):
            state.date = workDate
            #add worked hours to history when checkout
            if state.name == "Checkout" :
                employee.hoursHistory.append([self.date,state.date])
            #indicate and change current state
            #print ('Current:',self,' => has ',state.name,'with the following date: ',state.date)
            self.__class__ = state

    def __str__(self):
        return self.name

#the default state will only be used when object is intializated
class Default(EmployeeState):
    pass
class Checkin(EmployeeState):
    name = "Checkin"
    date= EmployeeState.date
class Checkout(EmployeeState):
    name = "Checkout"
    date = EmployeeState.date
