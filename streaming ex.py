
f=open("thenna kk.txt","r")
data=f.read()
print(type(data))
print(data)
f.close()
'''

f=open("hello thenna.txt","r")
print(f.readline())
print(f.readline())



f=open("hello thenna.txt","r")
data=f.readlines()
print(data)
print(data[1])
print(type(data))



f=open("hello thenna.txt","r")
while True:
    data=f.read(25)
    print(data)
    if not data:
        break
f.close()



#writting file

f=open("hello.txt","w")
f.write("thennarasu\n")
f.write("devilliers")
f.flush()
f.close()



f=open("hello.txt","w")
f.write("\n also scripting")
f.write("\n"+input("enter the text:"))
f.flush()
f.close()


#example for seek()

f=open("hello.txt","r")
f.seek(8)
data=f.read()
print(data)
f.close()

f=open("hello.txt","w")
f.seek(6)
f.write("python programming")
f.flush()
f.close()


#file attributes:
    name-returns the name of the file
    mode-returns the mode of operation
    closed-returns true if file is closed. otherwise false

exmple:

f=open("hello.txt","r")
print("name:",f.name)
print("mode:",f.mode)
print("before closed:",f.closed)
f.close()
print("after closed:",f.closed)



reading and writting object


import pickle
l=[100,"hello",10.5]
f=open("objex.dat","wb")
pickle.dump(l,f)
f.flush()
f.close()


import pickle
f=open("objex.dat","rb")
l=pickle.load (f)
print(l)
f.close()


class student:
    name=""
    regno=1
    def get_details(self):
        print("name:",self.name)
        print("Regno:",self.regno)
s=student()
s.name="aaa"
s.regno=123
s.get_details()

import pickle
f=open("oops.dat","wb")
pickle.dump(s,f)
f.flush()
f.close()

f=open("oops.dat","rb")
s1=pickle.load(f)
s1.get_details()


'''




''
