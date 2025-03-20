file = open("output.txt", 'w')
line1 = input("Enter text to write to the file: ")
write = file.write(line1)
print("Data successfully written to output.txt.")
file.close()

file1 = open("output.txt", 'a')
file1.write("\n")
line2 = input("Enter additional text to append: ")
append = file1.writelines(line2)
print("Data successfully appended.")
file1.close()

file2 = open("output.txt", 'r')
print("Final content of output.txt: ")
read = file2.readlines()
for i in read:
    print(i.strip())
    file2.close()
