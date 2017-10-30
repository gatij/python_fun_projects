import os

def RenameFiles():
	FileList=os.listdir(r"C:\Users\asus\Desktop\python\alphabet\alphabet")
	print(FileList)
	SavedPath=os.getcwd()
	print("current working directory is " + SavedPath )
	os.chdir(r"C:\Users\asus\Desktop\python\alphabet\alphabet")
	
	
	for FileName in FileList:
		#print("oldName "+FileName)
		#print("newName "+FileName.strip('0123456789'))
		if FileName=="bristol.jpg":
			os.rename(FileName,"1")
		   

		elif  FileName=="athens.jpg":
		    os.rename(FileName,"2")
		    

		elif  FileName=="ithaca.jpg":
		    os.rename(FileName,"3")
		    

		elif  FileName=="beijing.jpg":
		    os.rename(FileName,"4")
		    

		elif  FileName=="madrid.jpg":
		    os.rename(FileName,"5")
		
		elif  FileName=="berkeley.jpg":
		    os.rename(FileName,"6")
		    

		elif  FileName=="istanbul.jpg":
		    os.rename(FileName,"7")
		    
		
		elif  FileName=="colombo.jpg":
		    os.rename(FileName,"8")
		                      

		    
	os.chdir(SavedPath)	

RenameFiles()	
