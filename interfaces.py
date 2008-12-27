# Copyright (c) 2007 Roman Glass
# See LICENSE for details.


"""A functional sorting library."""

from zope.interface import Interface, implements


class IListVisitor(Interface):
    def forNullList(self, that):
        """Returns a new Null-Object."""

    def forNonNull(self):
        """Returns a new NonNull-Object and applies
        recursively the method to the rest of the list."""

class IListManager(Interface):
    def add(self, o):
        """Add a new Item"""

    def diff(self, o):
        """Difference... Remove Item"""

    def parse(self):
        """Get a list-type back"""

    def sort(self):
        """Sort the list"""

    def changeSort(self, o):
        """Avaible Visitors for Sorting the List:
        -- SelectionSortV
        -- InsertionSortV
        -- MergeSortV
        -- QuickSortV
        Use
        ListM().changeSort(v)
        where v is ie. InsertionSortV() to change."""
