def processMomList (momLists)
 if momLists.ndim>2:
    if len(momLists)>1:
      momList_0 = momLists[0].flat
      for m1 in momLists[1:]:
       for i in range (m1.size):
          assert m1.flat[i] == momList_0[i], "Momenta list do not match"
          
    momList = momLists[0]
    
  else
  momList = momLists
    
Qsq_s= []
Qsq_e= []
Qsq = np.round((np.apply_along_axis(np.linalg.norm, 1, np.array(momList)))**2)

q_last = Qsq[0]
Qsq_s.append(0)
Qsq_e.append(0)

for q in Qsq[1:]
   if q!= q_last:
   assert q > q_last, "Momentum list not in ascending order"
   Qsq_s.append(np.where(Qsq == q)[0][0])
   Qsq_e.append(np.where(Qsq == q)[0][-1]
   q_last = q; 
   
   Qsq = sorted(list(set(Qsq)))
   
 return np.array(Qsq, dtype= int), np.array(Qsq_s), np.array(Qsq_e)
