def KK(mEff, Qsq, L):
  return np.sqrt( 2* energy(mEff,Q,L) * (energy(mEff, Q,L)+ mEff))

def energy(mEff, Q, L):
  return np.sqrt(mEff**2 + (2.0 *np.pi /L)**2 * Qsq)

def kineFactor(ratio_err, mEff, Q, L):
 momNum = ratio_err.shape[0]
 ratioNum = ratio_err.shape[-1] #multiple error ratios?#
 binNum = len(mEff)

 assert len(Q) == momNum, "Err(kineFactor): dimension of ratio errors and momentum transfers do not match"

 kineFactor= np.zeros((binNum, momNum, ratioNum, 2)) #4D?#

 for b in range(binNum)
    for q in range(momNum)
        Qsq = np.dot(Q[q], Q[q])
        
        kineFactor[b, q]= [[ (energy(mEff[b] ,Qsq, L) +mEff[b]), 0], \
                                   [ 2.0 * np.pi / L * Q[ q, 0 ], 0 ], \
                                   [ 2.0 * np.pi / L * Q[ q, 1 ], 0 ], \
                                   [ 2.0 * np.pi / L * Q[ q, 2 ], 0 ], \
                                   [ 0, 2.0 * np.pi / L * Q[ q, 2 ] ], \
                                   [ 0, -2.0 * np.pi / L * Q[ q, 1 ] ], \
                                   [ 0, -2.0 * np.pi / L * Q[ q, 2 ] ], \
                                   [ 0, 2.0 * np.pi / L * Q[ q, 0 ] ], \
                                   [ 0, 2.0 * np.pi / L * Q[ q, 1 ] ], \
                                   [ 0, -2.0 * np.pi / L * Q[ q, 0 ] ] ] \
                    / np.repeat[ ratio_err[q], 2).reshape(10,2) \
                    / KK(mEff[b], Qsq, L)
                                
return kineFactor

