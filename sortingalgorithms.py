# Copyright (c) 2007 Roman Glass
# See LICENSE for details.


"""Sorting Algorithms"""

from zope.interface import implements
from interfaces import IListVisitor
from baselist import NullList, NonNull
from basesort import SortD
from help import *



class SelectionSortV(SortD):
    def forNonNull(self, o):
        m = o.accept(MinV())
        self.l = NonNull(m, (o.accept(DiffV(m))).accept(self))

        return self.l


class InsertionSortV(SortD):
    def forNonNull(self, o):
        if o.rest.null():
            return o

        if o.first < o.rest.first:
            return NonNull(o.first,
                           o.rest.accept(self))

        if o.rest.rest.null():
            return NonNull(o.rest.first,
                           NonNull(o.first,
                                   NullList()))

        return NonNull(o.rest.first,
                       NonNull(o.first, o.rest.rest).accept(self))


class MergeSortV(SortD):
    def forNonNull(self, o):
        if o.rest.null():
            return o
        
        h = o.accept(HalfV())
        
        return h.first.accept(self).accept(MergeV(h.rest.accept(self)))


class QuickSortV(SortD):
    def forNonNull(self, o):
        if o.rest.null():
            return o
        
        lt = o.accept(LowerThanV(o.first))
        ge = o.accept(GreaterorEqualV(o.first))

        if lt.null():
            return ge

        if ge.null():
            return lt

        return NonNull(lt.accept(self),
                       ge.accept(self)).accept(ParseV())

