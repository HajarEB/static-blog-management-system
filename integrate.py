import update
import os


fileName = input("Please Enter the New File Name\n")
# filePath= "./Content/"+fileName
filePath=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Content')
filePath=os.path.join(filePath,fileName)
print(filePath)
if os.path.exists(filePath):
    update.readFile(fileName)
    print("Done")
else:
    print("******** Please Make Sure the File: "+ fileName +" Exists in the Right Directory './Content' ********\n")


