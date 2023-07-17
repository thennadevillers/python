class employee:
    def set_details(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal
    def get_details(self):
        print("name:",self.name)
        print("emp id:",self.eid)
        print("salary:",self.sal)
class bonus(employee):
    def get_bonus(self):
        return self.sal*0.25
emp=bonus()
name=input("enter the name:")
eid=int(input("enter the empid:"))
sal=float(input("enter the salary:"))
emp.set_details(name,eid,sal)
emp.get_details()
if sal>=12000.00:
    print("bonus:",emp.get_bonus())
else:
    print("no bonus")
