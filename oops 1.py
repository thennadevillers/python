class Employee:
    name=""
    eid=0
    sal=0.0
    def get_details(self):
        print("name:",self.name)
        print("emp id:",self.eid)
        print("salary:",self.sal)
    def get_bouns(self):
        return self.sal*0.25
    def get_pf(self):
        return self.sal*0.12
emp=Employee()
print("before calling:")
emp.get_details()
emp.name=input("enter the name:")
emp.eid=int(input("enter the EmpID:"))
emp.sal=float(input("enter the salary:"))
emp.get_details()
print("pf=",emp.get_pf())
if emp.sal>=12000.00:
    print("bonus:",emp.get_bouns())
else:
    print("no bonus")