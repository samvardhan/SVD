#parsing#
parser = argparse.ArgumentParser(description= "Perform SVD")

parser.add_argument( "ratio_err_filename", action= 'store', type= str)

parser.add_argument("mEff_filename", action= 'store', type= str)

parser.add_argument("momList_filename", action= 'store', type= str)

args= parser.parse_args()


#assigning#
ratio_err_filename= args.ratio_err_filename

mEff_filename = args.effective_mass_filename

momList_filename= args.momList_filename

L= 64
ratioNum= 10

#reading#
binNum= rw.detConfigNum( mEff_filename )

momList = rw.readTxtFile(momList_filename, dtype= int)

momNum= len(momList)

Qsq,Qsq_s,Qsq_e = fncs.processMomList (momList)

QsqNum = len(Qsq)

ratio_err = rw.readNthDataCol( ratio_err_filename, 2).reshape(ratioNum,momNum).T   

mEff = rw.readNthDataCol (mEff_filename, 1)


#calculating kinematic factors#
kinefactors= pq.kineFactor_GE_GM(ratio_err, mEff, momList, L)

#SVD#
u = np.zeros((binNum, QsqNum*ratioNum, 2))
s = np.zeros((binNum, QsqNum, 2))
vT= np.zeros((binNum, QsqNum, 2,2))



