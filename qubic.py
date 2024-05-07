import numpy as np
import math
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

def intQubic(value): 
    return int((value+0.5) ** (1./3))

def intQubic_ok_for_small_vcalues(value): 
    for v in range(1,value):
        if (v*v*v)>value:
            return v-1

def qubic_list(value):
    qubicList=[]
    while value>0:
        v=intQubic(value)
        qubicList.append(v)
        value -= v*v*v
    return qubicList

class QubicList:
    def __init__(self,value):
        self.value=abs_int(value)
        self.qubicList=qubic_list(self.value) # Brute force solution
        self.len=len(self.qubicList)
        self.numEvaluated=0

    def set(self,value):
        self.value=value
        self.qubicList=qubic_list(self.value) # Brute force solution
        self.len=len(self.qubicList)
        self.numEvaluated=0

    def scan(self,verbose=False):
        if self.len<=1:
            return False
        for factor in range(self.qubicList[0],1,-1):
            remain=int(self.value-factor*factor*factor)
            if verbose:
                print(f"{self.numEvaluated}:[{factor}, .... ]")
            self._scan(factor,[factor],remain,intQubic(remain),verbose)
        if verbose:
            print(f"Summary: # evaluated = {self.numEvaluated}")
    
    def _scan(self,factorAcceptUpTo,factors,remain,nextFactor,verbose):
        newLen=len(factors)+1
        if remain==0 or newLen>=self.len:
            return
        factor=nextFactor
        if factor>factorAcceptUpTo:
            factor=factorAcceptUpTo
        while factor > 0:
            newRemain=remain-factor*factor*factor
            newFactors=factors+[factor]            
            if newRemain==0:
                if verbose:
                    self.numEvaluated+=1
                    print(f"{self.numEvaluated}:{newFactors}")
                self.qubicList=newFactors
                self.len=newLen
                break
            nextFactor=intQubic(newRemain)
            if nextFactor>factor:
                break
            self._scan(factor,newFactors,newRemain,nextFactor,verbose)            
            factor-=1

    def _scan_old(self,factorAcceptUpTo,factors,remain,nextFactorNotUsed,verbose):
        newLen=len(factors)+1
        if remain==0 or newLen>=self.len:
            return
        factorBegin=intQubic(remain,1/3)
        if factorBegin>factorAcceptUpTo:
            factorBegin=factorAcceptUpTo
        for factor in range(factorBegin,0,-1):
            newRemain=remain-factor*factor*factor
            newFactors=factors+[factor]            
            if newRemain==0:
                if verbose:
                    self.numEvaluated+=1
                    print(f"{self.numEvaluated}:{newFactors}")
                self.qubicList=newFactors
                self.len=newLen
                break
            self._scan_old(factor,newFactors,newRemain,nextFactorNotUsed,verbose)            

def main(args):
    if len(args)==0:
        print("No value to calculate")
        return
    verboseFlag=False
    for arg in args:
        value=abs_int(arg)
        if value==None:
            verboseFlag=not verboseFlag
        else:
            ql=QubicList(value)                        
            print(f"Brute force: {ql.value} : {ql.qubicList}")            
            ql.scan(verboseFlag)
            print(f"Best match: {ql.value} : {ql.qubicList}")            
            
if __name__ == "__main__":
    main(sys.argv[1:])