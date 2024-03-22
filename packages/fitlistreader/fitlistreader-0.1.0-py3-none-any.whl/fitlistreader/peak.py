#!.venv/bin/python3

import xml.etree.cElementTree as ET
from dataclasses import dataclass

import numpy as np
import scipy.interpolate

class BackgroundColl: 
	"""
	Container class to order attributes more nicely. 
	"""

	__slots__ = ('regions', 'model', 'nparams', 'params', 'vol', 'dvol')

	def __init__(self):
		pass

class Peak:
	"""
	Supply a sub-xml tree element <fit> and which peak in that fit you want to extract, ennumerated top-down via 0-indexing. 
	use_val is an internal devision between "cal" and "uncal" for all  marker-values, which will be different if the spectrum was calibrated by HDTV. 
		Usually you are interested in the "cal" version, which is the default. 
	"""
	def __init__(self, fit, peak_index, spc, ID, use_val="cal", binwidth = 1):
		self.ID = ID
		self.binwidth = binwidth
		self.model = fit.attrib['peakModel']
		self.spc_name = spc[0]
		self.calibration = spc[1]
		self.chi = float(fit.attrib['chi'])
		self.bg = BackgroundColl()
		self.region_of_interest = {'start':float('nan'), 'stop':float('nan')}
		for region in fit.iter('regionMarker'):
			a = float(region.find('begin').find(use_val).text)
			b = float(region.find('end').find(use_val).text)
			self.region_of_interest['start'] = min(a, b)
			self.region_of_interest['stop'] = max(a, b)
		self.bg.regions = []
		for bg_region in fit.iter('bgMarker'):
			start = bg_region.find('begin').find(use_val).text
			stop = bg_region.find('end').find(use_val).text
			self.bg.regions.append((start, stop))
		for i, xpc in enumerate(fit.iter('peak')): # iter is the fastest method to get elements of sub-xml tree, but it must be iterated through to get benefits...
			if i < peak_index: 		continue
			elif i == peak_index: 	xpeak = xpc.find(use_val)
			else: 					break
		# streamlined loading. Does the same as the following expression, only faster
		# xpeak = next( xpc for i, xpc in enumerate(fit.iter('peak')) if i == peak_index).find(use_val)
		self.pos = float(xpeak.find('pos').find('value').text)
		self.dpos = float(xpeak.find('pos').find('error').text)
		self.vol = float(xpeak.find('vol').find('value').text)
		self.dvol = float(xpeak.find('vol').find('error').text)
		self.width = float(xpeak.find('width').find('value').text) # Tipp: width = 3.33*sigma
		self.dwidth = float(xpeak.find('width').find('error').text)

		bg_xml = fit.find('background')
		self.build_bg(bg_xml)
		#self.range.region = 
	
	def build_bg(self, bg_xml):
		width_mod = 2 # the width over which we integrate the background should be the same as the region described by the peak.width parameter. This is the FWHM, we thus need to half the value here, leading to width_mod = 2, as it devides by the integer here. 
		self.bg.model = bg_xml.attrib['backgroundModel']
		
		nparams = int(bg_xml.attrib['nparams'])
		self.bg.nparams = nparams
		lst = [0]*nparams
		err = lst.copy()
		for p in bg_xml.iter('param'):
			lst[int(p.attrib['npar'])] = float(p.find('value').text)
			err[int(p.attrib['npar'])] = float(p.find('error').text)
		self.bg.params = lst

		if self.bg.model == 'polynomial':
			start, stop = self.region_of_interest['start'], self.region_of_interest['stop'] # self.pos-self.width/width_mod, self.pos+self.width/width_mod
			self.bg.vol = self._better_vol_poly(self.bg.params, start, stop)/(self.binwidth)
			if nparams == 2: # TODO: Add Covariance approximation. Too complicated for n>2
				err_c0 = (stop-start)*err[0]
				err_c1 = (stop**2 /2-start**2 /2)*err[1]
				err_a  = (-lst[0]-lst[1]*start)*(self.dpos+self.dwidth)
				err_b  = ( lst[0]+lst[1]*start)*(self.dpos+self.dwidth)
				self.bg.dvol = np.sqrt(err_c0**2+err_c1**2+err_a**2+err_b**2)/(self.binwidth)
			else:
				self.bg.dvol = self._general_poly_vol_err_indep(lst, err, start, self.dpos+self.dwidth, stop, self.dpos+self.dwidth)/(self.binwidth)
				print(f"Warning: Polynomial background of order >2 cannot approximate covariance of error parameters. BG errors are likely too small.")

		elif self.bg.model == 'interpolation': # Model: BG(x) -> cubic spline with points {(p[0],p[1]) , (p[2],p[3]) , ... , (p[n-1],p[n])}
			pairs = sorted([(self.bg.params[i], self.bg.params[i+1]) for i in range(0, len(self.bg.params), 2)], key=lambda x:x[0])
			x, y = [[a[0] for a in pairs], [b[1] for b in pairs]]
			cspline = scipy.interpolate.CubicSpline(x, y)
			start, stop = self.region_of_interest['start'], self.region_of_interest['stop']

			self.bg.vol = cspline.integrate(start, stop)/self.binwidth
			self.bg.dvol = np.sqrt(self.bg.vol) # TODO: Fix this, this is not strictly the error

		elif self.bg.model == 'exponential': # Model: BG(x) = exp(p[n]*x^n + p[n-1]*x^(n-1) + ... + p[1]*x + p[0])
			def f(x):
				tot = self.bg.params[0]
				for i, p in enumerate(self.bg.params[1:]):
					tot += p*x**(i+1)
				return np.exp(tot)
			start, stop = self.region_of_interest['start'], self.region_of_interest['stop']
			# determine volume numerically, as the model has no analytical Integral...
			vol = 0
			for x in np.linspace(start, stop+self.binwidth, int(np.floor((stop - start)/self.binwidth) + 1)):
				vol += f(x)
			
			self.bg.vol = vol*self.binwidth
			self.bg.dvol = np.sqrt(self.bg.vol) # TODO: Fix this, this is not strictly the error
		else:
			print(f"Error: Background model '{bg_xml.attrib['backgroundModel']}' not supported!")
	
	def _poly(self, coeff):
		"""returns polinomial function with coefficients as python function of signature f(x::float)=>poly(x)::float"""
		def f(x):
			tot = 0
			for i, c in enumerate(coeff):
				tot+= c*x**i
			return tot
		return f
	
	def _vol_from_poly(self, coeff, a, b):
		"""computes area under polinomial with coefficients coeff between x=a and x=b analytically"""
		mod_coeff = [0]
		for i, c in enumerate(coeff):
			mod_coeff.append(1/(i+1)*c)
		f = self._poly(mod_coeff)
		return f(b)-f(a)

	def _better_vol_poly(self, coeff, a, b):
		"""more efficient implementation of `_vol_from_poly`. Does not require re-building of coefficients. Independant of `_poly`"""
		tot = 0
		for i, c in enumerate(coeff):
			tot += c/(i+1)*(b**(i+1)-a**(i+1))
		return tot

	def _general_poly_vol_err_indep(self, coeff, dcoeff, a, da, b, db):
		"""general formula for the uncertainty in the volume determination of a polynomial with coefficients coeff between x=a and x=b. 
		The single uncertainties dcoeff, da and db are assumed to be independant. 
		dcoeff must have the same dimension as coeff."""
		tot = 0
		for i, dc in enumerate(dcoeff): # error terms in coefficients
			tot += (dc/(i+1)*(b**(i+1)-a**(i+1)))**2
		tot += (self._poly(coeff)(b)*db)**2 # error terms in stop-variable
		inv_coeff = [] # because `int f(x) dx from a to b = F(b)-F(a)`, the '-' before 'F(a)' can instead be applied to all coefficients in F and then be replaced by a '+', which is easier here. 
		for c in coeff: inv_coeff.append(-c)
		tot += (self._poly(inv_coeff)(a)*da)**2 # thus, error in start-variable
		return np.sqrt(tot)

	@classmethod
	def build_empty(cls):
		"""generates a valid Peak object with all filds containing None values or similar"""
		self = cls.__new__(cls)
		self.binwidth = None
		self.model = None
		self.chi = None
		self.pos = None
		self.dpos = None
		self.vol = None
		self.dvol = None
		self.width = None
		self.dwidth = None
		self.bg = BackgroundColl()
		self.bg.model = None
		self.bg.nparams = None
		self.bg.params = []
		self.bg.vol = None
		self.bg.dvol = None

		return self

	def dummy(self):
		pass
