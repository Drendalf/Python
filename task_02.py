def thesaurus(*args):
    dic_1 = {}
    for i in args:
        f = i[0]
        if f not in dic_1:
            dic_1[f] = []
        dic_1[f].append(i)
    return dic_1


print(thesaurus("иван", "игорь", "илья", "елена"))
