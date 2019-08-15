import argparse
import readwrite as rw
import functions as fncs
import numpy as np
import physQuants as pq

#PARSING#
parser = argparse.ArgumentParser(description= "Singular Value Decomposition")

parser.add_argument( "ratio_err_filename", action= 'store', type= str)
#ratio_err_filename contain two columns- first column is label number(1,2,3...)#
#the second column is the corresponding ratio error value)#

parser.add_argument("mEff_filename", action= 'store', type= str)
#contains the (three) effective mass values#

parser.add_argument("momList_filename", action= 'store', type= str)
#contains the permutations of momenta in 3D starting from 000#

args= parser.parse_args()



#ASSIGNING#
ratio_err_filename= args.ratio_err_filename

mEff_filename = args.effective_mass_filename

momList_filename= args.momList_filename

L= 64
#L defines the number of lattice points#

ratioNum= 10



#READING#
binNum= rw.detbinNum( mEff_filename )
#calculaitions are averaged over the number of effective masses provided, which is thus the bin size for jacknifing#

momList = rw.readTxtFile(momList_filename, dtype= int)
#stores momList as an array#

momNum= len(momList)

Qsq,Qsq_s,Qsq_e = fncs.processMomList (momList)
#groups each Q-squared value (vector magnitude) of the momenta list permutations alongwith the indices of its start and end points#

QsqNum = len(Qsq)

ratio_err = rw.readNthDataCol(ratio_err_filename, 2).reshape(ratioNum,momNum).T   

mEff = rw.readNthDataCol (mEff_filename, 1)

#calculating kinematic factors#
kinefactors= pq.kineFactor_GE_GM(ratio_err, mEff, momList, L)



#PERFORM SVD(to calculate psedoinverse of kinefactor matrix)#
inverse = [ [] for qsq in range(QsqNum)]

for qsq in range(QsqNum):
#svd done seperately for each q-squared value#
#??why is the kinefactor matrix for each qsq value getting the same ratioNum to expand with???#
    kinefactor_qsq = kinefactor[ :, Qsq_s[qsq]:Qsq_e[qsq] + 1, ...]\
                                                      .reshape[binNum, (Qsq_s[qsq]-Qsq_e[qsq]+1) * ratioNum, 2]
    u, s, vT = np.linalg.svd[kinefactor_qsq,full_matrices=False]
                                              
    uT = np.transpose(u,(0,2,1))
    v = np.transpose(vT,(0,2,1))
    
    s_mat= np.zeros((u.shape[-1],vT.shape[-2]))
    s_mat_inv= np.zeros((binNum,) +  np.transpose(s[b]).shape
    
    for b in range binNum
        s_mat[:min(u.shape[-1],vT.shape[-2]),:min(u.shape[-1],vT.shape[-2])] = np.diag(s[b])
        s_mat_inv[b] = np.linalg.pinv[s_mat]
         
    inv_mat = v @ s_mat_inv @ uT
     
    inverse[qsq] = np.average(inv_mat, axis=0).T
                        
rw.writeSVDOutputFile( output_filename, inverse, Qsq )
