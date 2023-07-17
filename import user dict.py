from collections import UserString

class MyString(UserString):
    def append(self, str):
        self.data=self.data+str
    def remove(self,str):
        self.data=self.data.replace(str,"")
str=MyString("This is String")
print(str)
str.append(" Hello")
print("after Append:",str)
str.remove("String")
print("After Remove:",str)
