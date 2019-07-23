def detTimestepAndConfigNum(filename) 
 
 tlast= -1
 timeStepNum = 0
 timeStepNum_last = -1
 configNum = 0
 
 with open ( filename, "r") as file:
    for line in file:
		t = int(line.split() [0])
		
		if t== (tlast+1):
		timeStepNum += 1
		tlast = t
		
		elif t==0:
		     if timeStepNum_last>=0
				 assert timeStepNum = timeStepNum_last, "Err(detTimestepAndConfigNum): No. of timesteps not consistent across configurations"
		timeStepNum_last = timeStepNum
		timeStepNum = 1
		configNum += 1
		tlast = t
		
		else:
		   print(:"Err(detTimestepAndConfigNum): timestep in 1st column does not behave as expected")
			 return -1
			 
 assert timeStepNum = timeStepNum_last, "Err(detTimestepAndConfigNum): No. of timesteps not consistent across configurations"
 return timeStepNum, configNum
		
def readTxtFile (filename, columnNum, **kwargs)
   with open(filename, "r") as txtFile:
		lineNum= (txtFile.readlines())
		txtFile.seek(0)
		data = np.array(txtFile.read.split(), **kwargs).reshape(lineNum,columnNum)
		
   return data

def readNthDataCol(filename , N)
	data = []
	with open(filename, "r") as file:
		for line in file:
			if line.split():
				data.append(line.split())
	data = np.array(data, dtype=float)
 return data[..., N]

			
	
	
	
	
	
	
	
	
	
