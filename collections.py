#counter
'''
from Collection import Counter

list = [1,2,3,4,1,2,6,7,3,8,1]
print(counter(list))
cnt=Counter(list)
print("cnt[3]:",cnt[3])

from collection import defultdict
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(num['three'])

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
count = defultdict(int)
names_list = "Mike John Mike anna Mike jhon mike mike britney smith Anna Smith".split()
for names in names_list:
    count[name] +=1
print(count)


from collection import orderedDict
od = OrderedDict()
od['a'] = 1
od['10'] = 2
od['c'] = 3
print (od)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collection import deque
list = ["a","b","c"]
deq = deque(list)
print(deq)
deq.append("d")
deq.appendleft("e")
print(deq)

deq.pop()
deq.popleft()
print(deq)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collection import ChainMap
dict = {'a' : 1, 'b' : 2}
dict = {'c' : 3, 'b' : 4}
chain_map = ChainMap(dict1, dict2)
print (list(chain_Map.keys()))
print (list(chain_Map.Values()))
dict3 = {'e' : 5, 'f' : 6}
new_chain_map = chain_map.new_child(dict3)
print(new_Chain_map)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collection import namedtuple
student = namedtuple('student', 'fname, lname, age')
s1 = Student('john', 'clarke', '13')
s2 = Student('smith','Clarke', '15')
print(S1.fname)
#s1['fname']="Ricky"
print(S1)
print(S2)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


from collection import userDict
ud=userDict({'a':"apple",'b':"ball"})
print(ud.data)

ud=userDict()
print(ud.data)

class MyDict(UserDict):
    def __del__(self):
        raise RuntimeError("not allowed")
    def pop(self, key=None):
        raise RuntimeError("not allowed")
    def popitem(self):
        raise RuntimeError("Not allowed")
m=MyDict({'a':"apple",'b':"ball"})
print(m)
m.pop('b')
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from collections import UserList
ul=UserList([1,2,3,4])
print(ul.data)

ul=UserList()
print(ul.data)

class MyList (UserList):
    def remove(self, item):
        raise RuntimeError("not allowed")
    def pop(self, i=0):
        return UserList.pop(self, i=i) #it will remove the first element

m1=MyList([1,2,3,4])
print(m1)
print(m1.pop())
print("After pop:",m1)

------------------------------------------------------------------------------------------------------------------------------------------------------
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

'''
