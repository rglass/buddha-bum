# Copyright (c) 2007 Roman Glass
# See LICENSE for details.


"""
Base classes for functional recursive sorting algorithms.
"""



class ListD:
    """
    Data-Type which asks for the service of a visitor class.
    """
    def accept(self, ask):
        """Asks for an accepted service"""
        raise NotImplementedError("Subclasses must implement this method")

    def null(self):
        raise NotImplementedError("Subclasses must implement this method")
        

class NullList(ListD):
    def accept(self, ask):
        return ask.forNullList(self)

    def null(self):
        return True


class NonNull(ListD):
    def __init__(self, first, rest):
        self.first = first
        self.rest = rest

    def accept(self, ask):
        return ask.forNonNull(self)

    def null(self):
        return False
