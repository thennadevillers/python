0# OOPS #
'''
* Inheritance *

 - Access one class properties into another class.
 - Reuse the code also.

general format:

class A:
    statements
class B(A):
    Statements

A - superclass
B - subclass

Types of Inheritance

* single inheritance  - one superclass inherited by one subclass.

Example:

class Employee:
    def set_details(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def get_details(self):
        print("Name:",self.name)
        print("Emp id:",self.eid)
        print("Salary:",self.sal)

#class Bonus:
class Bonus(Employee):
    def get_bonus(self):
        return self.sal*0.25

emp=Bonus()
name=input("Enter The Name:")
eid=int(input("Enter The EmpID:"))
sal=float(input("Enter The Salary:"))
emp.set_details(name,eid,sal)
emp.get_details()
if sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")

----------------------------------------------------------------------------
* Multilevel Inheritance -
superclass inherited by subclass again the subclass inherited by another subclass.

Example :


class Employee:
    def set_details(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def get_details(self):
        print("Name:",self.name)
        print("Emp id:",self.eid)
        print("Salary:",self.sal)

class Pf(Employee):
    def get_pf(self):
        return self.sal*0.12

class Bonus(Pf):
    def get_bonus(self):
        return self.sal*0.25

emp=Bonus()
name=input("Enter The Name:")
eid=int(input("Enter The EmpID:"))
sal=float(input("Enter The Salary:"))
emp.set_details(name,eid,sal)
emp.get_details()
print("Pf:",emp.get_pf())
if sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")

-------------------------------------------------------------------------
* Multiple Inheritance - more than one superclasses inheritanced by single subclass.

Example:


class Employee:
    def set_details(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def get_details(self):
        print("Name:",self.name)
        print("Emp id:",self.eid)
        print("Salary:",self.sal)

class Pf:
    def get_pf(self,sal):
        self.sal=sal
        return self.sal*0.12

class Bonus(Employee,Pf):
    def get_bonus(self):
        return self.sal*0.25

emp=Bonus()
name=input("Enter The Name:")
eid=int(input("Enter The EmpID:"))
sal=float(input("Enter The Salary:"))
emp.set_details(name,eid,sal)
emp.get_details()
print("Pf:",emp.get_pf(sal))
if sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")

------------------------------------------------------------------------------

* Hierarchical Inheritance  - one superclass inherited by more than one subclasses.

Example :

class Employee:
    def set_details(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def get_details(self):
        print("Name:",self.name)
        print("Emp id:",self.eid)
        print("Salary:",self.sal)

class Pf(Employee):
    def get_pf(self):
        return self.sal*0.12

class Bonus(Employee):
    def get_bonus(self):
        return self.sal*0.25

emp=Bonus()
name=input("Enter The Name:")
eid=int(input("Enter The EmpID:"))
sal=float(input("Enter The Salary:"))
emp.set_details(name,eid,sal)
emp.get_details()
if sal>=12000.00:
    print("Bonus:",emp.get_bonus())
else:
    print("No Bonus")

emppf=Pf()
emppf.set_details(name,eid,sal)
print("Pf:",emppf.get_pf())

----------------------------------------------------------------------------
----------------------------------------------------------------------------------
* Polymorphism

    - one format with different functionality.
    Types:
    * compile time - Operator Overloading , Method Overloading
    * Runtime - Method Overriding.

    Operator Overloading:
    - Single operator do the different data types. (+)

Example:

a,b=10,20
print("Int:",(a+b))# +

a,b="Hello","world"
print("String:",(a+b))

a,b=[1,2,3],[4,5,6]
print("List:",(a+b))

    Method Overloading
    - Method having same name with different arquments.(no.of arquments)
    Ex: range(start[,stop,]step)
Example:

class MethodOverload:
    def area(self,a=None,b=None):
        if a!=None and b!=None:
            print("Area of Rect:",(a*b))
        elif a!=None:
            print("Area of Square:",(a*a))
        else:
            print("no area")

m=MethodOverload()
m.area()
m.area(10)
m.area(10,20)


    MethodOverriding
    - same name with same arquments. Done between the classes with inheritance.
    - done using super() method.

class Area:
    def circle(self,r):
        self.r=r
        print("Area:",(3.14*r**2))

class Peri(Area):
    def circle(self,r):
        self.r=r
        print("Perimeter:",(3.14*r*2))
        super().circle(r)

p=Peri()
p.circle(10)
#p.circle(10)


'''
