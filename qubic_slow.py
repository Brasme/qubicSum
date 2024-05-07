import numpy as np
import sys

def abs_int(value):
    if isinstance(value, int):
        return abs(value)        
    if isinstance(value, float):
        return abs(int(value))
    if (isinstance(value, str) and value.isdigit()):
        return abs(int(value))
    return None

def intQubic_root_has_rounding_error_np(value): 
    return int(np.power(value,1./3))

def intQubic_root_has_rounding_error_math(value): 
    return int(value ** (1./3))

def intQubic_ok(value): 
    return int((value+0.5) ** (1./3))

def intQubic(value): # Fastest..?
    for v in range(1,value):
        if (v*v*v)>value:
            return v-1
    
def qubic_list(value):
    qubicList=[]
    while value>0:
        v=intQubic_ok(value)
        qubicList.append(v)
        value -= v*v*v
    return qubicList

def qubic_list_best(value,stopAt=0,maxSeed=0,bestLen=10000): # returns only a best mactch 
    best=None
    qubicList=qubic_list(value) # Gives alternative with highest qubic alternative first
    n=len(qubicList)
    if n==0:
        return None
    if stopAt>=qubicList[0]:
        return None
    if maxSeed==0:
        maxSeed=qubicList[0]
    if qubicList[0]<=maxSeed:
        if n<bestLen:
            bestLen=n
            best=qubicList
    seed=qubicList[0]-1
    if seed>maxSeed:
        return best    
    if len(qubicList)>1 and seed>qubicList[1] and seed>stopAt:
        if qubicList[1]>stopAt:
            stopAt=qubicList[1] 
    else:
        stopAt=seed
    while seed>stopAt :                
        subValue=int(value-seed*seed*seed)
        solution=qubic_list_best(subValue,stopAt,seed,bestLen-1)
        if solution!=None:
            best=[seed]
            best.extend(solution)
            bestLen=len(best)           
        seed=seed-1    
    return best

def main(args):
    if len(args)==0:
        print("No value to calculate")
        return
    for arg in args:
        value=abs_int(arg)
        if value!=None:
            qubicList=qubic_list(value)    
            sumList=[v*v*v for v in qubicList]
            print(f"Brute force: {arg} : {qubicList} : {sumList}")
            
            qubicBest=qubic_list_best(value)    
            sumList=[v*v*v for v in qubicBest]
            print(f"Scan best: {arg} : {qubicBest} : {sumList}")
    
if __name__ == "__main__":
    main(sys.argv[1:])