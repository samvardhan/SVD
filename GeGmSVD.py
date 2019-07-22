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



#reading#
dummy, binNum= rw.detTimestepAndConfigNum( mEff_filename )

momList = rw.readTxtFile(momList_filename, 3, dtype= int)

momNum= len(momList)

Q,Qs,Qe = fncs.processMomList (momList)

QsNum = len(Q)

ratio_err = rw.readNthDataCol( ratio_err_filename, 2).reshape(ratioNum,momNum).T   

mEff = rw.readNthDataCol (mEff_filename, 1)


#calculating#
kinefactors= pq.kineFactor_GE_GM(ratio_err, mEff, momList, L)
#SVD#


