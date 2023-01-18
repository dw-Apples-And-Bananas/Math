def Multiples_Of(arg:str):
    arg = arg.lower()
    if arg.find("in") != -1:
        multiple, inside = arg.split("in")
        inside = set([int(i) for i in inside.split(" ") if i != ""])
        multiplesDict = {int(m):[i for i in inside if i%int(m)==0] for m in multiple.split(" ") if m!=""}
    elif arg.find("between") != -1:
        multiple, between = arg.split("between")
        between = [int(i) for i in between.split(" ") if i != ""]
        between = range(between[0],between[1])
        multiplesDict = {int(m):[i for i in between if i%int(m)==0] for m in multiple.split(" ") if m!=""}
    else:
        return
    for array in multiplesDict: multiplesDict[array].sort()
    if len(multiplesDict) > 1:
        multiples = ""
        for m in multiplesDict: multiples += f"{m}: {multiplesDict[m]}\n"
        multiples = multiples[:-1]
    else:
        for m in multiplesDict: multiples = multiplesDict[m]
    return multiples


def Common_Multiples_Of(arg:str):
    arg = arg.lower()
    if arg.find("in") != -1:
        multiple, inside = arg.split("in")
        inside = set([int(i) for i in inside.split(" ") if i != ""])
        multiplesDict = {int(m):[i for i in inside if i%int(m)==0] for m in multiple.split(" ") if m!=""}
        common = {i:True for i in inside}
        for i in inside:
            for m in multiplesDict:
                if not i in multiplesDict[m]:
                    common[i] = False
        common = [c for c in common if common[c]]
    elif arg.find("between") != -1:
        multiple, between = arg.split("between")
        between = [int(i) for i in between.split(" ") if i != ""]
        between = range(between[0],between[1])
        multiplesDict = {int(m):[i for i in between if i%int(m)==0] for m in multiple.split(" ") if m!=""}
        common = {i:True for i in between}
        for i in between:
            for m in multiplesDict:
                if not i in multiplesDict[m]:
                    common[i] = False
        common = [c for c in common if common[c]]
    else:
        return
    return common


    # inside = list(set([int(i) for i in input("In: ").split(" ")]))
    # multiples = {m: [] for m in [int(m) for m in multiple.split(" ")]}
    # for m in multiples:
    #     for i in inside:
    #         if i % m == 0:
    #             multiples[m].append(i)
    # notCommon = []
    # for i in inside:
    #     for m in multiples:
    #         if not i in multiples[m]:
    #             notCommon.append(i)
    # common = [i for i in inside if not i in notCommon]
    # return common