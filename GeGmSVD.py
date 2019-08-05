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
inverse = [ [] for qsq in range(QsqNum)]

for qsq in range(QsqNum):

    kinefactor_qsq = kinefactor[ :, Qsq_s[qsq]:Qsq_e[qsq] + 1, ...]\
                                                      .reshape[binNum, (Qsq_s[qsq]-Qsq_e[qsq]+1) * ratioNum, 2]
    u, s, vT = np.linalg.svd[kinefactor_qsq, full_matrices =False]
                                              
    uT = np.transpose(u,(0,2,1))
    v = np.transpose(vT,(0,2,1))
    
    temp_s= np.zeros((u.shape[-1],vT.shape[-2]))
    



