def detConfigNum(filename) 
 with open(filename, "r") as file:
		for line in file:
			configNum = len(line.split())
 return  configNum
		
def readTxtFile (filename, **kwargs)
   with open(filename, "r") as txtFile:
		columnNum = len(next(file).split())
		file.seek(0)
		lineNum= (txtFile.readlines())
		txtFile.seek(0)
		data = np.array(txtFile.read.split(), **kwargs).reshape(lineNum,columnNum)
		
   return data

def readNthDataCol(filename , N, **kwargs)
	with open(filename, "r") as file:
		columnNum = len(next(file).split())
		file.seek(0)
		lineNum = (file.readlines())
		file.seek(0)
	        data = np.array(file.read.split(), **kwargs).reshape(lineNum, columnNum)
 return data[..., N]

			
	
	
	
	
	
	
	
	
	
