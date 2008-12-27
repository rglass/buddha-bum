# Copyright (c) 2007 Roman Glass
# See LICENSE for details.


"""Play around with different SortingAlgorithms"""

from zope.interface import Interface, implements
from interfaces import IListManager
from baselist import *
from sortingalgorithms import *
from help import *


class ListM:
    implements(IListManager)
    
    def __init__(self):
        self.n = NullList()
        self.sort = SelectionSortV

    def add(self, o):
        self.n = NonNull(o, self.n)

    def diff(self, o):
        self.n = self.n.accept(DiffV(o))

    def parse(self):
        return self.n.accept(ParseV())

    def sort(self):
        self.n = self.n.accept(self.sort())

    def changeSort(self, o):
        self.sort = o
