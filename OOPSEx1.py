# OOPS #
'''

Object Oriented Programming Structure

* Dynamic memory Processing
* Reusuablity of code.

Elements :

* Object - physical Entity
         - Access the members of a class.
         - Allocate the memory for members.
         - Instance of a class.
         Properties - id - var - unique
                     state - attributes - May be same.
                     behaviour - functionality - May be same.

* class - prototype.
        - It consists of variables, methods (functions) and objects.

* Data abstraction - Highlighting the particular data.

* Data Encapsulation - Wrapping upof different data's into single entity.

Example 1:

class Employee:
    name=""
    eid=0
    sal=0.0
    def get_details(self):
        print("Name:",self.name)
        print("Emp id:",self.eid)
        print("Salary:",self.sal)
    def get_bonus(self):
        return self.sal*0.25

emp=Employee()# obj=classname()
print("before Calling:")
emp.get_details()
emp.name=input("Enter The Name:")
emp.eid=int(input("Enter The EmpID:"))
emp.sal=float(input("Enter The Salary:"))
emp.get_details()
if emp.sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")

Example 2:

class Emp:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
 
class Employee:
    def set_details(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def get_details(self):
        print("Name:",self.name)
        print("Emp id:",self.eid)
        print("Salary:",self.sal)
    def get_bonus(self):
        return self.sal*0.25

emp=Employee()# obj=classname()
#print("Before Calling:")
#emp.get_details()
name=input("Enter The Name:")
eid=int(input("Enter The EmpID:"))
sal=float(input("Enter The Salary:"))
emp.set_details(name,eid,sal)
emp.get_details()
if sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")

-------------------------------------------------------------------
Initializer:
    * also called constructor in programming language.
    * create using __init__() method.
    * when object loading initializer call.

    types:
    * Default (without parameter)
    * Parameterized (with parameter)

Example 3:
'''
class Employee:
    #def __init__(self):
     #   print("Default loading...")
    def __init__(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def get_details(self):
        print("Name:",self.name)
        print("Emp id:",self.eid)
        print("Salary:",self.sal)
    def get_bonus(self):
        return self.sal*0.25

name=input("Enter The Name:")
eid=int(input("Enter The EmpID:"))
sal=float(input("Enter The Salary:"))
#emp2=Employee()
emp=Employee(name,eid,sal)
emp.get_details()
if sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")
'''
-----------------------------------------------------------------------

Class Members: (static)

    * create the members without self.
    * Loaded in memory during class loading.
    * no need for object to access.
    * access using classname.
    * lifetime until class ends.

Instance Members: (non-static)

    * access members using self.
    * Loaded in memory during object call.
    * object is must to access.
    * lifetime object into garbage collection.


Example 4:
'''
class Employee:
    name=""
    eid=0
    sal=0.0
    def get_details():
        print("Name:",Employee.name)
        print("Emp id:",Employee.eid)
        print("Salary:",Employee.sal)
        #print(self.get_bonus())
    def get_bonus(self):
        return Employee.sal*0.25
emp=Employee()# obj=classname()
Employee.name=input("Enter The Name:")
Employee.eid=int(input("Enter The EmpID:"))
Employee.sal=float(input("Enter The Salary:"))
Employee.get_details()
if Employee.sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")


