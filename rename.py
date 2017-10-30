import os
import string
def RenameFiles():
	FileList=os.listdir(r"C:\Users\asus\Desktop\python\prank\prank")
	print(FileList)
	SavedPath=os.getcwd()
	print("current working directory is " + SavedPath )
	os.chdir(r"C:\Users\asus\Desktop\python\prank\prank")
	
	for FileName in FileList:
		print("oldName "+FileName)
		print("newName "+FileName.strip('0123456789'))
		os.rename(FileName,FileName.strip('0123456789'))
	os.chdir(SavedPath)	

RenameFiles()	
