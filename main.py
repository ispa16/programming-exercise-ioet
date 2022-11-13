from utils import employeeMatchFrecuency
import sys
num = sys.argv[1]
if __name__ == "__main__":
    #use try to manage some unexpected expection
    try:
        if int(num)==1:
            print(employeeMatchFrecuency('data'))
        elif int(num)==2:
            print(employeeMatchFrecuency('data2'))
        elif int(num)==3:
            print(employeeMatchFrecuency('data3'))
        elif int(num)==4:
            print(employeeMatchFrecuency('data4'))
        else:
            print('select a number between 1 to 4')
    except Exception as e:
        print(e)
