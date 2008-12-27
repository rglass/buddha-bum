from sortingalgorithms import *
from listman import ListM
import timeit
from random import random



l = ListM()
for i in range(1, 10000000):
    l.add(random())

statement = """from baselist import NullList, NonNull
from sortingalgorithms import QuickSortV
NonNull(23, NonNull(5, NonNull(7, NonNull(1, NullList())))).accept(QuickSortV())"""

statement2 = "[23, 5, 7, 1].sort()"

statement3 = """from baselist import NullList, NonNull
from sortingalgorithms import MergeSortV
NonNull(23, NonNull(5, NonNull(7, NonNull(1, NullList())))).accept(MergeSortV())"""

statement4 = """from baselist import NullList, NonNull
from sortingalgorithms import InsertionSortV
NonNull(23, NonNull(5, NonNull(7, NonNull(1, NullList())))).accept(InsertionSortV())"""

statement5 = """from baselist import NullList, NonNull
from sortingalgorithms import SelectionSortV
NonNull(23, NonNull(5, NonNull(7, NonNull(1, NullList())))).accept(SelectionSortV())"""

print "python's sort"
t = timeit.Timer(statement2)
print t.timeit(10)

print "quicksort"
t = timeit.Timer(statement)
print t.timeit(10)

print "mergesort"
t = timeit.Timer(statement3)
print t.timeit(10)

print "insertionsort"
t = timeit.Timer(statement4)
print t.timeit(10)

print "selectionsort"
t = timeit.Timer(statement5)
print t.timeit(10)

# macbook 2ghz intel core 2 duo
# python's sort
# 4.29153442383e-05
# quicksort
# 0.00210690498352
# mergesort
# 0.00174498558044
# insertionsort
# 0.00049090385437
# selectionsort
# 0.00108003616333
