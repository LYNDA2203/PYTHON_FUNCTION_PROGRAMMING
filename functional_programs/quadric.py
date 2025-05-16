
import math

#declaring and initializing values of a,b,c
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))

#calculating the value of delta
delta=b*b-4*a*c

#checking the delta by conditional statement
if delta > 0:#delta is less than zero
    
    root1=(-b + math.sqrt(delta))/(2*a)
    root2=(-b - math.sqrt(delta))/(2*a)

    #printing the values of root1 and root2
    print("Two real and  distinct roots are....")
    print(f"The value of Root 1:",root1)
    print(f"The value of Root 2:",root2)

elif delta == 0:
    root=-b/(2*a)
    
    #printing the values of roots
    print("Two real and equal roots are.....")
    print(f"the value of Root1:",root)

else:
    real_part=-b/(2*a)
    img_part= math.sqrt(-delta)/(2*a)
    
    #printing the values of real and imaginary part of roots
    print("Two Complex roots..")
    print("Root1: {} + {}i".format(real_part,img_part))
    print("Root2: {} - {}i".format(real_part,img_part))
     
'''output:
PS C:\princy study\python\com.bridgelabz.functionalPrograms> py quadric.py
Enter the value of a:2
Enter the value of b:-4
Enter the value of c:1
Two real and  distinct roots are....
The value of Root 1: 1.7071067811865475
The value of Root 2: 0.2928932188134524
PS C:\princy study\python\com.bridgelabz.functionalPrograms> py quadric.py
Enter the value of a:-1
Enter the value of b:-2
Enter the value of c:-1
Two real and equal roots are.....
the value of Root1: -1.0
PS C:\princy study\python\com.bridgelabz.functionalPrograms> py quadric.py
Enter the value of a:-1
Enter the value of b:0
Enter the value of c:-1
Two Complex roots..
Root1: 0.0 + -1.0i
Root2: 0.0 - -1.0i'''