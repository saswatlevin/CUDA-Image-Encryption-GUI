	
def getFileNameFromPath(filePath):
	fileName = ""
	for i in range(len(filePath) - 2,0,-1):
		fileName = fileName + filePath[i + 1]
		if filePath[i] == "/" or filePath[i] == "\\":
			break

	# Backward slice
	return fileName[::-1]

def getExecutableName(fileName):
	executableName = ""
	for i in range(0,len(fileName)):

		if fileName[i] == ".":
			break
		executableName = executableName + fileName[i]
		
	return executableName

def removeFileNameFromPath(filePath,fileName):
	filePath = list(filePath)
	newFilePath = "" 
	for i in range( len(filePath) - 1, len(filePath) - len(fileName) - 1 , -1):
		if filePath[i] != "/":
			filePath[i] = ""
		filePath[i - 1] = ""

	for i in range(0,len(filePath)):
		if filePath[i] != "":
			newFilePath = newFilePath + filePath[i]
	
	return newFilePath

#print(removeFileNameFromPath("home/saswat/CUDA-Image-Encryption/src/make_serial.mk","make_serial.mk"))
#print((getExecutableName("def.mk")))
#print(getFileNameFromPath("/s/abcd.mk"))
#print(getExecutableName("abc.mk"))



