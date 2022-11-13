from employee.EmployeeState import Checkin,Checkout
from employee.AcmeEmployee import AcmeEmployee

def inputData(txtname):
    employeeList = []
    data = open("data/"+txtname+".txt", "r",encoding='utf-8')
    #get data following txt structure
    for line in data:
        line = line.split('=')
        employee = AcmeEmployee(line[0])
        hoursList= line[1].split(',')
        for i in hoursList:
            date = i.split('-')
            employee.change(Checkin,date[0])
            employee.change(Checkout,date[1])
        employeeList.append(employee)
    data.close()
    return employeeList

#get time range by hours
def rangeTime(a,b):
    results = []
    CONST_TIME_LIMIT = 0.59
    # not gonna consider the first minute or the last just the time between 
    a=a+0.01
    while(a<b):
        a = round(a, 2)
        results.append(a)
        #controll if 60 minutes are reached 
        minutes = round((a-int(a)),2)
        if( minutes == CONST_TIME_LIMIT):
            a=float(int(a)+1)
        else:
            #use two decimals to compare every minute
            a+=0.01
    return(results)


#get working range by day
def getWorkingRange(list):
    rangeList = []
    for element in list:
        day = element[0][:2]
        #delete the day in the element
        element[0] = element[0][2:]
        checkIn = element[0].replace(':','.')
        checkOut = element[1].replace(':','.')
        hoursRange = rangeTime(float(checkIn),float(checkOut))
        rangeList.append([day,hoursRange])
    return(rangeList)

def compareLists(listA,listB):
    count = 0
    for x in listA:
        for j in listB:
            #if week day the same and time range match
            if(x[0]==j[0]):
                if any(item in x[1] for item in j[1]):
                    count+=1
    return count
    
def employeeMatchFrecuency(dataName):
    employeeList =inputData(dataName)
    finalList = []
    auxList = []
    matchFrequency =''
    for employee in employeeList:
        hoursList = getWorkingRange(employee.hoursHistory)
        finalList.append([employee.name,hoursList])
    for element in finalList:
        auxList.append(element[0])
        for other in finalList:
            if (other[0] not in auxList):
                totalMatches =compareLists(element[1],other[1])
                matchFrequency=matchFrequency+element[0]+'-'+other[0]+': '+str(totalMatches)+'\n'
    return matchFrequency