#  with open("FilesLab/stuff.txt", "w") as file:
#      file.write("Line 1: Hello world!\n")
#      file.write("Line 2: This is a new line of text.\n")
#     #Task 1 
#  with open("FilesLab/stuff.txt", "r") as file:
#      content = file.read()
#      print(content)
# #task 2
#      file_handle = open("FilesLab/stuff.txt", "r")
#      content = file_handle.read()
#      print(content)
#      file_handle.close()
# #task 3
#  with open("FilesLab/stuff.txt", "a") as file:
#          file.write("\n\n")
#          file.write("Line 4: This is another appended line.\n")

#  with open("FilesLab/stuff.txt", "r") as file:
#              print(file.read())
# #task 4
#  user_input = input("Enter something to save:")
#  with open("FilesLab/stuff.txt", "w") as file:
#      file.write(f"user entered: {user_input}\n")
#      file.write("program succefull,\n")
#  print("user input saved to file")
# #Challenge