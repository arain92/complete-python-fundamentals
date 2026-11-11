# import os

# # with open("C:\\Users\\Lenovo\\Documents\\GitHub\\complete-python-fundamentals\\Data_Engineering_python\\hello.txt", "r") as f:
# #     data = f.read()
# #     print(data)

# # with open("C:\\Users\\Lenovo\\Documents\\GitHub\\complete-python-fundamentals\\Data_Engineering_python\\hello.txt", "w") as f:
# #     data = f.write("\nThis is a new line added to the file.")
# #     print(data)
# os.remove("C:\\Users\\Lenovo\\Documents\\GitHub\\complete-python-fundamentals\\Data_Engineering_python\\hello.txt")   

# Question Solve
# with open("practice.txt", "w") as f:
#     f.write("This is a practice file.\n")
#     f.write("We are learning file handling in Python.\n")
#     f.write("This is the third line of the file.\n")


# with open("practice.txt", "r") as f:
#     data = f.read()
#     print(data)

# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


with open("practice.txt", "r") as f:
    data = f.read()
    print(data)
    if(data.find("learning") != -1):
        print("Found")
    else:
        print("Not Found")    