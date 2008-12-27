from zope.interface import Interface, implements
from interfaces import IListVisitor



class SortD:
    implements(IListVisitor)

    def forNullList(self, that):
        return that
