# password = "Dess"

# while password == "Dess1":
#     print("Access Granted")
#     password != "Dess1"
# print("Error. Try Again")

# count = 0
# while count < 10:
#     print("Condition is True")
#     count = count + 1
# print("After the loop")    

password = str(1234)

UI = input("Enter your password")
if UI == password:
    print("Access Granted")

elif UI != password:
    print("Password is wrong")
else:
    print("Access Denied")