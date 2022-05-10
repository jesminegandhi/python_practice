# Python program to demonstrate
# Creation of List
# Adding items to a List
# Knowing the length of the list
# Removing items from the List by name and index

#Creating an empty list to store AWS Services
services = []
print("Blank List : ")
print(services)

#Creating another list with the desired AWS Services
service_list = ["EC2", "Lambda", "CloudFront", "S3", "Xray", "CloudWatch", "ElastiCache", "DynamoDB"]

#Variable used for counting index
i=0

#Loop to append the services list 
for a in service_list:
  services.append(service_list[i])
  i = i + 1

#Printing the list after the services are appended
print("New Service List after adding items is :", services)

#Printing the length of the services list
print("Length of the AWS Service Inventory is :", len(services))

#Removing an AWS service by name and printing the new service list
services.remove("ElastiCache")
print("New Service List after removing 1 item by name :", services)

#Removing an AWS service by index and printing the new list
services.pop(2)
print("New Service List after removing 1 item from 3rd position is :", services)

#Printing the new length of the services list
print("Updated length of the AWS Service Inventory is :", len(services))