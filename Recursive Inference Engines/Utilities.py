#! /bin/python3
# vim: set fileencoding=utf-8
#
# (c) March 1st, 2019, July 20, 2022, José Martinez, Polytech Nantes, University of Nantes
#
# Licence:  proprietary
# The use of this library is not authorised outside the Polytechnic School of the University of Nantes.
#


__all__ = [ 'splits', 'splits_2', 'splits_3' ]


from typing import Tuple, List, Any
from itertools import dropwhile


def splits (X:  List[Any]) -> List[Tuple[List[Any], List[Any]]]:
    """
    A utility function that splits a lists into two sub-lists at each possible index.

    :param X:  A list of any kind of elements.
    :return:  A couple with two lists that, when concatenated, give back X.
    """
    return ([]                 if len(X) == 0 else
            [([], X), (X, [])] if len(X) == 1 else
            [([], X)] + list(map(lambda YZ:  ([X[0]] + YZ[0], YZ[1]), splits(X[1:]))))


def splits_2 (X:  Any) -> List[Tuple[List[Any], Any, Any, List[Any]]]:
    """
    An extension of the function 'splits' that splits a lists into two sub-lists but with two elements in the middle.

    :param X:  A list of any kind of elements.
    :return:   A quadruplet with two sub-lists and two elements in the middle that, when concatenated in order, give back X.
    """
    return [ (Y, Z[0], Z[1], Z[2:])
             for (Y, Z) in splits(X)
             if len(Z) >= 2 ]


def splits_3 (X:  List[Any]) -> List[Tuple[List[Any], Any, Any, Any, List[Any]]]:
    """
    A variant of the function 'splits_3' that extract three elements in the middle.

    :param X:  A list of any kind of elements.
    :return:   A quintuplet with two sub-lists and three elements in the middle that, when concatenated in order, give back X.
    """
    return [ (Y, Z[0], Z[1], Z[2], Z[3:])
             for (Y, Z) in splits(X)
             if len(Z) >= 3 ]


if __name__ == "__main__":
    pass

