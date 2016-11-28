ans = []

def mySort(tupledArray):
    return sorted(tupledArray, key=lambda element: element[0])

N = int(input())
Arr = [input() for x in range(N)]
tupledArray = []
for pos in range(N):
    theInt, theString = Arr[pos].split(' ')
    tupledArray.append((int(theInt), theString, pos,))
sortedArray = mySort(tupledArray)
print(sortedArray)

for element in sortedArray:
    if element[2] >= N/2:
        ans.append(element[1])
    else:
        ans.append('-')
print(' '.join(ans))