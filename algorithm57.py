########
# Find all elements in a fiber pi^{-1}(b). (See Algorithm 5.7 in [Stu92])
#
# Input: An initial vector $u\in pi^{-1}(b)$, A matrix G where each row denotes each binomial element of Groebner Basis.
#        Note that $G_{i}^{+} > G_{i}^{-}$ where $>$ denotes term order for the Basis.
#
# Just note that you can calculate such $u$ and $G$ using Macaulay2.
#
# Output= Passive: All elements in a fiber $pi^{-1}(b)$.
#
#######

import numpy as np


u= [[0,0,0,40]];
G = [[0,2,-1,0],[0,-1,3,-1],[0,1,2,-1],[5,-1,0,0]];

u= set(tuple(i) for i in u)
G = set(tuple(i) for i in G)

# Initialize
Active = u;
Passive =set();
hundred_Passive =set();

#Choose any element in Active.
while len(Active)>0:
    previous_size_Active = len(Active);
    preActive =set();

    for u in Active:
        for v in G:
            np_v = list(v);
            # Make vminus
            
            vminus=np.zeros((1,len(np_v)), dtype=np.int8)
            vminus=vminus.tolist()
            vminus=vminus[0]
            for idx, val in enumerate(np_v):
                if val<0:
                    vminus[idx]=-val
            
            temp = np.array(u) - np.array(vminus);
            positive_test = 1
            # Positive test
            for i in temp.tolist():
                if i<0:
                    positive_test = 0
            uplusv = np.array(u)+np.array(v);
            #Membership test
            if tuple(uplusv.tolist()) in Passive:
                membership_test = 1;
            else:
                membership_test =0;
            if (positive_test == 1) and (membership_test ==0):
                preActive.add(tuple(uplusv.tolist()))
    Passive = Passive | Active;
    Active = preActive;
    preActive = set();
    #print "Attempt! Active len:"+str(len(Active))+" Passive len:"+str(len(Passive))
    #print Active
    #print Passive

print len(Active) #This should be zero.
print len(Passive) # This gives the cardinality of the fiber.


