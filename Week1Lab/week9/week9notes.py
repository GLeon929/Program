#learn how to write, read, and edit files using python
# #common modes when using files
# "r" - read only
#you can read this file but cannot change it 

# "w"- write only
#you can write to this file but cannot read it
#create a file and write to it, if the file already exists it will overwrite it
#will create one if one doesnt exist 

# "a"- append only
#adds new content to the end of the file, if the file does not exist it will create one
#Does not delete any existing content in the file

#open with ("Foldername/filename","mode")
#with open("week9/stuff.txt", "r") as file:
  #  content = file.read()
   # print(content)


#with open("week9/stuff.txt", "w") as file:
    #content = file.write("This is a new line of text that will be written to the file.\n")
   # print(content) #this will print the number of characters written to the file


#with open("week9/stuff.txt", "a") as file:
    #content = file.append
    #print(content) #append will not return anything, it will just add to the end of the file
