duplicateList=[1,2,3,4,5,1,2,3]
uniqueList=[duplicateList[i] for i in range(len(duplicateList)) if i==duplicateList.index(duplicateList[i])]

print(uniqueList)