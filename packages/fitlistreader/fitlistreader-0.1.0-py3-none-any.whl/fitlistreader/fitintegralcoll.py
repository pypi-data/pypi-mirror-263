#!.venv/bin/python3
import xml.etree.cElementTree as ET
from collections.abc import MutableSequence
from warnings import catch_warnings, simplefilter, warn
from copy import deepcopy

from .fitintegral import FitIntegral

class FitIntegralCollection(MutableSequence):
    """
    Acts as a container class holding all integrals of a fit. Also constructs the integral objects and manages them. 

    an integral 
    """

    def __init__(self):
        self.__int_list = []

    def __setitem__(self, index, value):
        if self.check_valid_element(value):
            self.__int_list[index] = value
        else : 
            raise ValueError("Value to be set is not in a valid format. ")
        warn(RuntimeWarning("Items from a FitIntegralCollection are managed internally and should not be changed manually"))

    def __getitem__(self, index):
        return self.__int_list[index]

    def __delitem__(self, index):
        self.__int_list.remove(index)
        warn(RuntimeWarning("Items from a FitIntegralCollection are managed internally and should not be deleted manually"))

    def __len__(self):
        return len(self.__int_list) # maybe change to reflect multiple integrals in single fit?
    
    def insert(self, index, value):
        if self.check_valid_element(value):
            self.__int_list.insert(index, value)
        else:
            raise ValueError("Value to insert is not a valid element. ")
        warn(RuntimeWarning("Items from a FitIntegralCollection are managed internally and should not be inserted manually"))

    
    def append(self, value):
        if self.check_valid_element(value):
            self.__int_list.append(value)
        else:
            raise ValueError("Appended value is not a valid element. ")

    def reverse(self): 
        self.__int_list =  reversed(self.__int_list)
        warn(RuntimeWarning("Items from a FitIntegralCollection are managed internally and should not be reversed manually"))

    def extend(self, iterable):
        for element in iterable:
            self.append(element)
        pass

    def __iadd__(self, other): # if this is not called with a sequence of dicts (i.e. FIC += {"tot":FitIntegral()}), this implementation might not work
        with catch_warnings():
            simplefilter("ignore") # maybe remove the filter?
            for element in reversed(other):
                self.insert(0, element)
        warn(RuntimeWarning("Items from a FitIntegralCollection are managed internally and should not be added manually"))

    def check_valid_element(self, elem):
        """
        checks if elem is of a valid form to add to the integralcollection. 
        
        Elements of the FitIntegralCollection are dicts which contain one or 
        three valid FitIntegrals. 
        In the case of only a single entry, the key must be named "tot". 
        For three entries, the two additional keys are "bg" and "sub". 
        Parameters
        ----------
        elem : Any
               To pass the check, elem must be an object as described above. 
        """
        if type(elem) is dict and 'tot' in elem.keys():
            if len(elem.keys()) == 1:
                return FitIntegral.is_valid_fitintegral(elem['tot'])
            elif len(elem.keys()) == 3 and \
                'bg' in elem.keys() and \
                'sub' in elem.keys():
                return FitIntegral.is_valid_fitintegral(elem['tot']) and \
                    FitIntegral.is_valid_fitintegral(elem['bg']) and \
                    FitIntegral.is_valid_fitintegral(elem['sub'])
        return False
    
    def create_new_integral(self, fit) -> None:
        """
        Creates and adds a new FitIntegral object to this collection. 

        Parameters
        ----------
        fit : cElementTree: xml-subtree 
              The subtree must contain the <integral> tag as a first-level element. 
              Can also contain other first-level elements.
        """
        part_ints = {}
        for f_int in fit.iter('integral'):
            part_ints[f_int.attrib['integraltype']] = FitIntegral(f_int)
        self.append(part_ints)
    
    def to_list(self):
        """
        Returns a deepcopied List object representing the FitIntegralCollection.
        """
        return deepcopy(self.__int_list)