class employee:
    def set_details(self,name,eid,sal):
        self.name=name
        self.eid=eid
        self.sal=sal

    def get_details(self.name):
        print("name:",self.name)
        print("emp id:",self.eid)
        print("salary:",self.sal)

class pf(employee):
    def get_pf(self)
        return self.sal*0.12
class bonus(pf):
    def get_bonus(self):
        return self.sal*0.25
emp=bonus()
name=input("enter the name:")
eid=int(input("enter the eid:"))
sal=float(input("enter the salary:"))
emp.set_details(name,eid,sal)
emp.get_details()
print("pf:",emp.get_pf())
if sal>=12000.00:
    print("bouns:",emp.get_bonus())
else:
    print("no bonus")
