def Factors_Of(arg:str):
    factor = [int(i) for i in arg.split(" ") if i!=""]
    factorsDict = {f:[i for i in range(1,f+1) if f%i==0] for f in factor}
    if len(factorsDict) > 1:
        factors = ""
        for f in factorsDict: factors += f"{f}: {factorsDict[f]}\n"
        factors = factors[:-1]
    else:
        for f in factorsDict: factors = factorsDict[f]
    return factors


def Common_Factors_Of(arg:str):
    factor = [int(i) for i in arg.split(" ") if i!=""]
    factorsDict = {f:[i for i in range(1,f) if f%i==0] for f in factor}
    factor.sort()
    common = {i:True for i in range(1,factor[-1]+1)}
    for i in range(1,factor[-1]+1):
        for f in factorsDict:
            if not i in factorsDict[f]:
                common[i] = False
    common = [c for c in common if common[c]]
    return common

