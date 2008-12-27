# Copyright (c) 2007 Roman Glass
# See LICENSE for details.


"""Helper Functions"""

from zope.interface import implements
from interfaces import IListVisitor
from baselist import NonNull, NullList
from basesort import SortD



class AtomInit:
    def __init__(self, a):
        self.a = a


class ParseV:
    implements(IListVisitor)

    def __init__(self):
        self.lat = []

    def forNullList(self, that):
        return self.lat

    def forNonNull(self, that):
        if not isinstance(that.first, NonNull):
            self.lat.append(that.first)
            return that.rest.accept(self)

        that.first.accept(self)
        that.rest.accept(self)
        
        return self.lat


class MinV:
    implements(IListVisitor)

    def forNullList(self, that):
        pass #Not reached!

    def forNonNull(self, that):
        if that.rest.null():
            return that.first
        
        m = that.rest.accept(self)

        return that.first <= m and that.first or m


class DiffV(SortD, AtomInit):
    def forNonNull(self, that):
        if that.first == self.a:
            return that.rest.accept(self)

        that.rest = that.rest.accept(self)

        return that


class MergeV(AtomInit):
    implements(IListVisitor)
    
    def forNullList(self, that):
        return self.a.null() and that or self.a

    def forNonNull(self, p):
        if self.a.null():
            return p
    
        if p.first < self.a.first:
            return NonNull(p.first,
                           p.rest.accept(self))
    
        return NonNull(self.a.first,
                       self.a.rest.accept(MergeV(p)))


class HalfV:
    implements(IListVisitor)
    
    def forNullList(self, that):
        self.o = that
        return self.__fn()

    def forNonNull(self, that):
        self.o = that
        return self.__fn()

    def __fn(self):
        return self.o.accept(HalfAdapterV(NullList(), NullList(), True))


class HalfAdapterV:
    implements(IListVisitor)
    """Visitor for splitting 2 lists.
    """

    def __init__(self, p, q, b):
        self.p = p
        self.q = q
        self.b = b

    def forNullList(self, that):
        return NonNull(self.p, self.q)

    def forNonNull(self, that):
        if self.b:
            return that.rest.accept(HalfAdapterV(NonNull(that.first,
                                            self.p),
                                    self.q,
                                    not self.b))

        return that.rest.accept(HalfAdapterV(self.p,
                                    NonNull(that.first,
                                            self.q),
                                    not self.b))


class EqualityAdapter(SortD):
    def __init__(self, a, eq):
        self.a = a
        self.eq = eq

    def forNonNull(self, that):
        if self.eq(that.first, self.a):
            return NonNull(that.first,
                           that.rest.accept(self))
        
        return that.rest.accept(self)



    
class LowerThanV(SortD, AtomInit):
    def forNonNull(self, that):
        return that.accept(EqualityAdapter(self.a, lambda x, y: x < y))

        
class GreaterorEqualV(SortD, AtomInit):
    def forNonNull(self, that):
        return that.accept(EqualityAdapter(self.a, lambda x, y: x >= y))
