#Documentación del módulo os: https://docs.python.org/3/library/os.html

#Documentación del módulo sys: https://docs.python.org/3/library/sys.html

#Documentación del módulo platform: https://docs.python.org/3/library/platform.html

# import the module
import os

#trace to where python project actually is 
print(os.getcwd()) #Get Current Working Directory

os.chdir("..") #Change Directory
             # ..\ previous directory
print(os.getcwd())

print(os.listdir()) #List Directory (prints all files in location)

os.chdir("/Users/nicol/OneDrive/Documentos/VScode/Proyecto/Git/DAY 12")
print(os.getcwd())
os.mkdir("New_Direct") #generates a new directory in actual location
print(os.listdir())

os.chdir("/Users/nicol/OneDrive/Documentos/VScode/Proyecto/Git/DAY 12/New_Direct")
print(os.getcwd())

os.chdir("..")
print(os.getcwd())

os.rmdir("New_Direct") #removing a directory
print(os.listdir())