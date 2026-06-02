#  2.A Python program to create three variables:
Name ="Divya"
Age =18
City ="Pilani"
print("Name :",Name)
print("Age :",Age)
print("City :",City)

# 3.A Python program that: 
# Takes a user's name as input.  
# Prints the name in uppercase.  
# Prints the total number of characters in the name. 
name = input("Enter user name :")
print( "upper_case :",name.upper())
print("Total characters:",len(name))

#  4.five commonly used string methods in Python
address = "alwar"
print(address.upper()) 
a = "DIVYA"
print(a.lower()) 
intro ="I love java" 
print(intro.replace("java","Python")) 
text = " hello  " 
print(text.strip()) 
Temp = "python"
print(Temp.startswith("py"))

# 5.Create a list containing the names of five fruits. 
# • Print the complete list.  
# • Print the first and last element.  
# • Print the total number of items in the list. 
fruits =["apple","mango","litchi","orange","banana"]
print("This is my list :",fruits)
print("First element:",fruits[0])
print("Last element:",fruits[-1])
print("Total number of items in the list :",len(fruits))

# 6. Write a Python program to: 
# • Create a list of numbers [10, 20, 30, 40, 50]  
# • Add 60 to the list.  
# • Remove 20 from the list.  
# • Print the updated list. 
lst =[10, 20, 30, 40, 50] 
lst.append(60)
print("Add 60 to the list:",lst)
lst.remove(20)
print("Remove 20 from the list:",lst)
print("Updated list:",lst)