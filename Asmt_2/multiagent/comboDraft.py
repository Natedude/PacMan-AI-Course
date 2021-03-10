listA = ['1', '2', '3']
listB = ['A', 'B']
listC = ['!', '@', '#', '$']
listList = [listA, listB, listC]

import itertools
final = list(itertools.product(*listList))
for c in final:
    print(c)
print(3 * 2 * 4)
print(str(len(final)))