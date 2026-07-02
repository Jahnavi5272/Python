class Demo:
    a=4

object = Demo()
print(object.a) #prints the class attribute because instance attribute is not present.
object.a=0      #instance attribute is set
print(object.a) #prints instance attribute because instance attribute is present.
print(Demo.a)   #prints the class attribute.