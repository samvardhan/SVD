def processMomList (momList)

Qsq_s= []
Qsq_e= []
Qsq = np.round((np.apply_along_axis(np.linalg.norm, 1, np.array(momList)))**2)

q_last = Qsq[0]
Qsq_s.append(0)
Qsq_e.append(0)

for q in Qsq[1:]:
   if q!= q_last:
      assert q > q_last, "Momentum list not in ascending order"
      Qsq_s.append(np.where(Qsq == q)[0][0])
      Qsq_e.append(np.where(Qsq == q)[0][-1])
      q_last = q; 
   
   Qsq = sorted(list(set(Qsq)))
   
return np.array(Qsq, dtype= int), np.array(Qsq_s), np.array(Qsq_e)
