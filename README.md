# Exercise

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame.
The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.
Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data.
## Restrinctions
- You can not use any external library to solve the exercise

# Solution
### Architecture Selection
For this exercise I propose an architecture based on the states pattern, the reason why I propose this pattern is because it fits my perception of how attendance dialing works, I consider that when an employee checks in or out his state changes, so it seems to me a correct way to approach the problem by defining a pattern based on state. 
### Architecture Explanation
Firstly, what was done was to create the AcmeEmployee class, where certain initial attributes were defined, such as the name and the history of hours worked, as well as its initial state, which will be Default, and finally we defined a function that will be in charge of changing the state of the object, and that it will receive as a parameter the time of the change

Then we define the states of the employee as well as its handler, in the handler we define the function in charge of changing between the states, as well as we put a restriction so that the range of hours is added to the history only when an exit is marked.
We define the three states that an employee can have
- Default: when an employee is initialized for the first time
- Checkin: when the employee marks the beginning of his shift
- Checkout: when the employee marks the end of his day

One benefit of this pattern is that we can easily use these states and this handler with other classes.

# Solution Description

As the restrictions say, I could not use a datetime library that would have simplified things a lot, so in order to compare the times correctly, i treat the hours as if they were real numbers, that is, if the time is 01:15, then I converted it to 1.15 and defined restrictions so that it works like a normal clock, that is, in ranges of up to 60.

To compare the day I took the first two characters and with this I defined a list that had the day in the first position and the range in the second This way we can easily compare if an element in a range on one day is in another of the same day, I also defined the ranges for the hours in such a way that if someone works from 10:00-11:00 and another from 11:00-12:00, the time 11:00 do not count as a false positive

# Approach and methodology 
As I mentioned before, my focus was on the employee, initially I thought of a solution that allows me to control the work history of an employee, after thinking about it a lot, the best way I came up with is to control it according to its status, this way I can control it in one better way if the employee has marked his entry or exit, in addition to allowing me to have his history of hours worked.
# Testing
For this exercise I defined five functions in the file utils.py
- inputData: the function reads the txt file following its structure to create employee type objects and change their status according to the information in the file, it also returns a list of employees
- rangeTime: the function obtains the range in minutes between two given times, returning a list with all the minutes between these times
- getWorkingRange: the function takes a work list as a parameter and separates it according to the days, and the hours worked in the ranges that are available, returning a list with the day and the minutes worked on that day
- compareLists: the function compares two lists with the days and minutes worked on that day and returns the number of times their schedules have crossed in total
- employeeMatchFrecuency the function takes a txt file as a parameter and returns how many times the staff schedules have been crossed in the file

All these functions where tested multiple times in the file testUtils.py using unittest and all tests where succesfully


## Installation

First clone the repository.

The solution has none dependencies, so there's no need to install anything, by the way Python 3.10.5 was used.

In the project root execute:
#### to run example 1:
```sh
py main.py 1
```
#### to run example 2:
```sh
py main.py 2
```
#### to run example 3:
```sh
py main.py 3
```
#### to run example 4:
```sh
py main.py 4
```

examples 1 and 2 are the ones that were provided in the problem, while examples 3 and 4 were made by me, all the solutions were correct.
