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

def qubic_list_alternatives(value,stopAt=0,maxSeed=0): 
    alternatives=[]
    qubicList=qubic_list(value) # Gives alternative with highest qubic alternative first
    if len(qubicList)==0:
        return []
    if stopAt>=qubicList[0]:
        return []
    if maxSeed==0:
        maxSeed=qubicList[0]
    if qubicList[0]<=maxSeed:
        alternatives.append(qubicList)
    seed=qubicList[0]-1
    if seed>maxSeed:
        return alternatives    
    if len(qubicList)>1 and seed>qubicList[1] and seed>stopAt:
        if qubicList[1]>stopAt:
            stopAt=qubicList[1] 
    else:
        stopAt=seed
    while seed>stopAt :                
        subValue=int(value-seed*seed*seed)
        subSulutions=qubic_list_alternatives(subValue,stopAt,seed)
        for subSolution in subSulutions:
            if subSolution[0]<seed:
                alternative=[seed]
                alternative.extend(subSolution)
                alternatives.append(alternative)
        seed=seed-1    
    return alternatives

def main(args):
    if len(args)==0:
        print("No value to calculate")
        return
    for arg in args:
        qubicList=[]
        value=abs_int(arg)
        alternatives=[]
        if value!=None:
            qubicList=qubic_list(value)    
            alternatives=qubic_list_alternatives(value)    
        sumList=[v*v*v for v in qubicList]
        print(f"{arg} : {qubicList} : {sumList}")
        # print(f"{arg} : {alternatives}")
        
        bestIdx=0
        bestLen=len(alternatives[0])
        for idx in range(1,len(alternatives)):
            n=len(alternatives[idx])
            if n<bestLen:
                bestIdx=idx
                bestLen=n
        
        print(f"Evaluated {len(alternatives)} alternatives")
        qubicList=alternatives[bestIdx]
        print(f"Best = {bestIdx}({bestLen}) = {qubicList}")
        sumList=[v*v*v for v in qubicList]
        print(f"{arg} : {qubicList} : {sumList}")
        
    
if __name__ == "__main__":
    main(sys.argv[1:])