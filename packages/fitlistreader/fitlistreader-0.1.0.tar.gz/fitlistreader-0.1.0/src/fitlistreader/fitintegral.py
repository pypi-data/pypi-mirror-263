#!.venv/bin/python3
import xml.etree.cElementTree as ET

# TODO this could be a dataclass, maybe try some standard implementation with decorators for easier readability
class FitIntegral:
    """"
    Represents an individual integral, saved in the <integral> tag in a fitlist. 
    """

    __slots__ = ('pos', 'dpos', 'width', 'dwidth', 'vol', 'dvol', 'skew', 'dskew')

    def __init__(self, fint, use_val="cal"):
        xint = fint.find(use_val) or fint.find("uncal")
        self.pos    = float(xint.find('pos').find('value').text)
        self.dpos   = float(xint.find('pos').find('error').text)
        self.vol    = float(xint.find('vol').find('value').text)
        self.dvol   = float(xint.find('vol').find('error').text)
        self.width  = float(xint.find('width').find('value').text)
        self.dwidth = float(xint.find('width').find('error').text)
        if not fint.find(use_val): # skew is only saved for uncalibrated Integrals, idk why...
            self.skew   = float(xint.find('skew').find('value').text)
            self.dskew  = float(xint.find('skew').find('error').text)
        else:
            self.skew = float('nan')
            self.dskew = float('nan')

    def __repr__(self):
        return f"FitIntegral at {self.pos: 4.0f} with V={self.vol:2.1e}, w={self.width:2.1e}, s={self.skew:2.1e}"

    @classmethod
    def is_valid_fitintegral(cls, obj):
        return type(obj) is FitIntegral