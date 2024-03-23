#!.venv/bin/python3
import xml.etree.cElementTree as ET
from collections.abc import Sequence

import numpy as np

from .peak import Peak
from .fitintegralcoll import FitIntegralCollection

class Fitlist(Sequence):
	"""
	Representation of a Fitlist as a Sequence of Peaks, grouped in Fits. 
	
	Encompasses all neccessary information which is saved in a fitlist, 
	most importantly the peak information. Those can be accessed as a 
	flattened array via their consecutive indices. As a Sequence, 
	Fitlists can be accessed backwards via negative-Indexing, 
	just like standard python Lists.  
	Calibrations and integrals are saved in separate structures and accessed 
	through object methods. 

	Methods
	-------
	 - get_integral_by_peakID
	 - get_integral_list_by_type
	 - get_all_integrals
	 - closest
	"""

	def __init__(self, path: str):
		"""
		Create Fitlist instance from a path to the fitlist.xml file. 

		Parses the xml-tree and flattens the created objects to 
		a one dimensional list. 

		Parameters
		----------
		path : str
			   a relative or absolute path to the fitlist.xml file. 
		"""
		if not isinstance(path, str):
			raise TypeError("'path' attribute expects a string (of a path)")
		try:
			self.tree = ET.parse(path)
			self.root = self.tree.getroot()
		except:
			raise ValueError(f"Could not read xml-file at {path}.")
		# len(Fitlist) should enumerate peaks, but the xml-file groups a different 
		# number of peaks in a fit (it has to if you think about it). 
		# So its structure is roughly: 
		#{xml: [fit0: (p0), (p1) ], [fit1: (p0), (p1), (p2) ], [fit2: (p0) ], [fit3: (p0) ], [fit4: (p0), (p1) ], ... }
		# We Iterate simply through each fit and total all occurences of "peak" 
		# to get the total length. But for indexing each peak, we have to know in 
		# which fit the peak is contained. For easier indexing, we build a list 
		# where each consequtive peak-index maps to a tuple of the index of its 
		# encompassing fit and the offset in this fit.
		# So the structure of this list (from the above example) looks like this: 
		#[(0,0), (0,1), (1,0), (1,1), (1,2), (2,0), (3,0), (4,0),  (4,1), ...]
		# In general, the subindexer looks like this: 
		#[(fitID(p0),Offset(p0)), (fitID(p1),Offset(p1)), (fitID(p2),Offset(p2)), (fitID(p3),Offset(p3)), ...]
		self.__subindexer = []
		self.__spectra_collection = []
		self.__integral_collection = FitIntegralCollection()
		self.__length = 0
		index = 0
		for fit in self.root:
			if fit.tag == "fit":
				spc = fit.find("spectrum").attrib
				self.__spectra_collection.append((spc["name"], spc["calibration"]))
				self.__integral_collection.create_new_integral(fit)
				offset = 0
				for child in fit:
					if child.tag == "peak":
						self.__subindexer.append((index, offset))
						self.__length += 1
						offset += 1
				index += 1
		self.__peakcache = [False]*self.__length # once generated, Peak-object overwrites the 'False' entry
		super().__init__()
	
	def __len__(self):
		return self.__length
	
	def __getitem__(self, i):
		if i >= self.__length or i < -self.__length:
			raise IndexError(f"{i} is out of range for Fitlist (len={self.__length})")
		if i<0:
			i = self.__length + i
		if self.__peakcache[i]: # caching
			return self.__peakcache[i]
		else:
			p = Peak(self.root[self.__subindexer[i][0]], self.__subindexer[i][1], self.__spectra_collection[self.__subindexer[i][0]], i) 
			self.__peakcache[i] = p
			return p
	
	def get_integral_by_peakID(self, peakID:int) -> FitIntegralCollection:
		"""
		returns the FitIntegralCollection for a given peakID. 

		Each Fit contains a collection of integrals, regardless whether it was 
		created because of a peakfit of an integration. With a peakfit it is 
		needed for the background determination. 

		Parameters
		----------
		peakID : int
				 ID of the peak 
				 (NOT the index in this Fitlist object, but the Peak.ID property)
		"""
		# the integral belonging to peakid is the one with the index stored in the first element in the subindexer belonging to the peakid
		return self.__integral_collection[self.__subindexer[peakID][0]]

	def get_integral_list_by_type(self, int_type:str, include_ids:bool=False)->list:
		"""
		Returns all FitIntegrals of a given type as a list. 

		Parameters
		----------
		int_type : str
				   Selects which type of integrals to return. 
				   Possible Types: sub, bg, tot
		include_ids : bool
					  If True, populates list with tuples of 
					  (FitIntegral, integralID:int)
		"""
		int_lst = []
		for id, int_dict in enumerate(self.__integral_collection.to_list()):
			if int_type in int_dict.keys():
				if include_ids:
					int_lst.append((int_dict[int_type], id))
				else:
					int_lst.append(int_dict[int_type])
		return int_lst

	def get_all_integrals(self) -> list:
		"""
		Returns all FitIntegralCollection objects in a List, ordered by integralID. 
		"""
		return self.__integral_collection.to_list()

	def closest(self, pos):
		"""Returns the peak with the best matching position to the argument pos"""
		closest_dist = [Peak.build_empty(), 10**10]
		for elem in self:
			vgl = np.abs(elem.pos - pos)
			if vgl<closest_dist[1]:
				closest_dist = [elem, vgl]
		return closest_dist


	def debug(self):
		print("Fitlist object summary:")
		print("")
		print(f"length: {self.__length}")
		print(f"subindexer:")
		for i, p in enumerate(self.__subindexer):
			print(f"{i:>5}: {p}")
		print(f"Integral Collection:")
		for index, fint_dict in enumerate(self.__integral_collection):
			print(f"Index {index}:")
			for key in fint_dict:
				print(f"\t {key}: {repr(fint_dict[key])}")
		print("----------------------------------------------------------------------")
		print(f"__subindexer")