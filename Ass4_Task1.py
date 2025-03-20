import os.path

path = "C:/Users/Lenovo/PycharmProjects/PythonProject/sample.txt"
if os.path.exists(path):
    file = open('sample.txt', 'r')
    print("Reading file content:")
    read = file.readlines()
    n=0
    for i in read:
        n+=1
        print("Line", n, ":", i.strip())
        file.close()
else:
    print("Error: The file 'sample.txt' was not found.")