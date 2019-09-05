import numpy as np

def detbinNum(filename):
	with open(filename, "r") as file:
			for line in file:
				binNum = len(line.split())
	return  binNum
		
def readTxtFile (filename, **kwargs):
	with open(filename, "r") as txtFile:
		columnNum = len(next(txtFile).split())
		file.seek(0)
		lineNum= (txtFile.readlines())
		txtFile.seek(0)
		data = np.array(txtFile.read.split(), **kwargs).reshape(lineNum,columnNum)	
	return data

def readNthDataCol(filename , N, **kwargs):
	with open(filename, "r") as file:
		columnNum = len(next(file).split())
		file.seek(0)
		lineNum = (file.readlines())
		file.seek(0)
	        data = np.array(file.read.split(), **kwargs).reshape(lineNum, columnNum)
	return data[..., N]

			
def writeSVDOutputFile( filename, data, Qsq ):	
	with open( filename, "w" ) as output:
		for q in range( len( data ) ):
			for r in range( data[ q ].shape[ 0 ] ):
				output.write("{:<10}{:<10}{:<20.10}{:<.10}\n".format(r, \
                                                                     Qsq[q], \
                                                                     data[q][r,0], \
                                                                     data[q][r,1]))
	print( "Wrote " + filename )
	

	
	
	
