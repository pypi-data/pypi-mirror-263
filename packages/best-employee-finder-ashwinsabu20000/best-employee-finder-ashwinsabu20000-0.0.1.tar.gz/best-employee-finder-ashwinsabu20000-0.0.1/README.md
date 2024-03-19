This is a package which actually determines the best employee in any firm based on the parameters
1. Total Hours
2. Rating
3. Total Orders

To use this function

Step 1 :
Call the class

x = BestEmployee()

Step 2:
Add the employee details

a.add_employee("Rahul",160,1.5,10)
a.add_employee("Sam",100,4.5,10)
a.add_employee("John",180,3.5,10)

Step 3:
Call the evaluate function

result=a.evaluate()

Step 4:
Print the Best Employee
print(result['best_emp'])