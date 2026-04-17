class First:
    a=55
    def method1(self):
        print("Method1")
        
o1=First()
print(o1.a)
o1.a=80
print(o1.a)
o1.method1()

class Second(First):
    b=45
    def Method2(self):
        print("method2")

s1=Second()
print(s1.a)
print(s1.b)

#print(o1.b)