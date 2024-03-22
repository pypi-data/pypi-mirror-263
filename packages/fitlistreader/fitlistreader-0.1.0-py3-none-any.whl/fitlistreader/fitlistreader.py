import sys

from .fitlist import Fitlist
from .peak import Peak
from .fitintegral import FitIntegral

usefile_path = f"fitlistreader"
helptext = f"""
Displays information saved in fitlist.xml files as generated from HDTV. 

Usage: $ {usefile_path} [-h] [-I] [-C] [--noheader] [-l args] path/to/fitlist.xml

Options:
-I --Integrals       Switches to integral mode. Only the recorded integrals are listed. 
                      This is different from the int_* options for -l, as all integrals are listed 
                      and not only the ones belonging to peaks.
-C --Calibrations    Switches to read out the calibrations of respective spectra contained in the fitlist
-h --help            Displays this help text and exits. 
   --noheader        Ommit printing the header line
-l --labels [args]   Change printed values to those specified in labels arg (see below)


Labels:	
With the -l/--labels option, the values which are extracted from the fitlist.xml file can be changed. 
The values  will be printed in order of specification. Available labels are:
Label       Meaning
pos         Peak position
dpos        Uncertainty in peak position
vol         Peak volume
dvol        Uncertainty in peak volume
width       Peak width
dwidth      Uncertainty in peak width
bg          Background volume under the peak
dbg         Uncertainty in background volume under peak
bg_model    Background model used in fitting
spc         Spectrum name from which the peaks were fitted
cal         Calibration coefficients (polynomial, 0 order first) of the spectrum 
int_id      ID of corresponding Integral
int_pos     Position of corresponding Integral
int_dpos    Uncertainty in position of corresponding Integral
int_vol     Volume of corresponding Integral
int_dvol    Uncertainty in volume of corresponding Integral
int_width   Width of corresponding Integral
int_dwidth  Uncertainty in width of corresponding Integral
int_skew    Skew of corresponding Integral
int_dskew   Uncertainty in skew of corresponding Integral
"""

fmt_name = {
			"pos": " Position", 
			"dpos": " Δ Pos",
			"vol": " Volume",
			"dvol": " Δ Vol",
			"width": "  Width",
			"dwidth": "  Δ Wid",
			"bg": " Background",
			"dbg": "Δ BG",
			"bg_model": "\bBG Model", # highly cursed, but makes it line up almost every time!
			"spc": " Spectrum",
			"cal": " Calibration Coeffs",
			"int_id": "Int. ID",
			"int_pos": "Int. Pos",
			"int_dpos": "Int. Δ Pos",
			"int_vol": "Int. Vol",
			"int_dvol": "Int. Δ Vol",
			"int_width": "Int. Width",
			"int_dwidth": "Int. Δ Wid",
			"int_skew": "Int. Skew",
			"int_dskew": "Int. Δ Skew",
			"int_type": "Int. Type"
		}

def get_fmt_val_from_key(fitlist:Fitlist, peak:Peak, key:str, _fint:FitIntegral=None)->str:
	"""Get formatted string representation of a named value from a fitlist. 

	Returns a formatted string, tuned for printing tables, of a requested value 
	from a specific Peak in a fitlist. When printing values from a fitlist, 
	these values can have different datatypes and format requirements when 
	printing them in a fixed space to the terminal. This function returns a 
	string representation of a named value in  an appropriate and human-readable
	format. 

	Parameters
	----------
	fitlist : Fitlist
	          The `Fitlist` object containing the requested peak and value. 
	          Needed to link to the `FitIntegralCollection`
	peak : Peak
	       `Peak` object containing the requested value
	key : string
	      Identifier for which value to retrieve. See `fmt_name.keys()` to
	      get valid keys, or the help text for their meaning
	_fint : FitIntegral
	        Instance of the valid `FitIntegral`for the queried value. Needed for
			certain 'int_*' keys. Will be inferred via fitlist if not given. 
			Caution: Implicitly skips checking for correctness regarding 
			the linking with the peak via the fitlist if supplied.  
	"""
	if key == "pos":
		return f"{peak.pos : 4.2f}"
	elif key == "dpos":
		return f"{peak.dpos : 4.2f}"
	elif key == "vol":
		return f"{peak.vol : 4.2e}"
	elif key == "dvol":
		return f"{peak.dvol : 4.2e}"
	elif key == "width":
		c = f"{peak.width : 4.2f}"
		return f"{c: >6}"
	elif key == "dwidth":
		c = f"{peak.dwidth : 4.2f}"
		return f"{c: >6}"
	elif key == "bg":
		return f"{peak.bg.vol : 4.2e}"
	elif key == "dbg":
		return f"{peak.bg.dvol : 4.2e}"
	elif key == "bg_model":
		return f"{peak.bg.model[:4]} deg:{peak.bg.nparams :1d}"
	elif key == "spc":
		return f"{peak.spc_name}"
	elif key == "cal":
		lst = peak.calibration.split()
		if not lst: return ""
		s = []
		for v in lst:
			s.append(f"{float(v): 2.1e},")
		s[-1] = s[-1][:-1]
		return ''.join(s)
	# for integral properties, we first have to retrieve the integral object (if not given by internal argument _fint)
	# this needs to be done via the peakID. We take the 'sub' integral by default and fall back to the 'tot' integral if sub doesn't exist. 
	elif key == "int_id": 
		return f"{peak.ID: 03.0f}"
	elif key == "int_pos": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.pos: 4.2f}"
	elif key == "int_dpos": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.dpos: 4.2f}"
	elif key == "int_vol": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.vol: 4.2e}"
	elif key == "int_dvol": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.dvol: 4.2e}"
	elif key == "int_width": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.width: 4.2e}"
	elif key == "int_dwidth": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.dwidth: 4.2e}"
	elif key == "int_skew": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.skew: 4.2e}"
	elif key == "int_dskew": 
		if _fint is None:
			_fint = fitlist.get_integral_by_peakID(peak.ID)["sub"] or fitlist.get_integral_by_peakID(peak.ID)["tot"]
		return f"{_fint.dskew: 4.2e}"
	elif key == "int_type":
		if _fint is not None:
			return " None"
		return " sub" if "sub" in fitlist.get_integral_by_peakID(peak.ID).keys() else " tot"
	else:
		raise RuntimeError(f"Supplied Key '{key}' is not a valid identifier of a named value")

def print_header(labels:list, sep_len:int)->None:
	"""Prints a formatted table header to std_out if permitted. 
	
	Printed tables should have equidistant labels in the header which exactly 
	line up with the content of the table for each row. Tuned together with the 
	`get_fmt_val_from_key` method. 

	Parameters
	----------
	labels : list[str]
	         List of strings to be printed in the header
	sep_len : int
			  separation between the labels (in spaces).
	
	Returns
	-------
	len_lim : int
	          Length of maximum permittable string representation of a value 
			  to be printed in the table. 
	"""
	char_len = len(max(labels, key=len))-1
	if "--noheader" not in sys.argv:
		s = ""
		for st in labels:
			s = s + f"{st:<{char_len}}{' '*sep_len}"
		print(s)
		print("─"*(len(s)-1)) 
	return char_len + sep_len

def integral_printer(fitlist:Fitlist, int_type:str, labels:list, iter_labels:list, sep_len:int)->None:
	"""Prints out all stored integrals of a given type for a supplied fitlist, 
	formatted as a table. 
	
	Prints Integral information to std_out. Available types of integral are 'tot' 
	for total integrated area, bg for the area of the background in tot, and 'sub' 
	for the subtracted rest of the volume. The values to be extracted can be 
	specified in iter_labels, labels are what are printed in the header to describe 
	the values. Only prints header when allowed by CMD line option. Separation between 
	entries is always at least the minimum sufficient amount, but can be increased with 
	sep_len. 
	
	Parameters
	----------
	fitlist : Fitlist
	          The `Fitlist` object containing the requested integrals.
	int_type : str
	           Type of integrals to extract. Possible: 'tot', 'bg' or 'sub'
	labels : list[str]
	         List of strings describing the requested values. Printed in header.
	iter_labels : list[str]
	              List of keys with which to retrieve the actual values. 
				  See `get_fmt_val_from_key`
	sep_len : int
	          Additional separation between table columns. 
	"""
	len_lim = print_header(labels, sep_len)
	for fint, fid in fitlist.get_integral_list_by_type(int_type, include_ids=True):
		s = [f" {str(fid):<{len_lim}}"]
		for label in iter_labels[1:]:
			s.append(f"{get_fmt_val_from_key(fitlist, None, label, _fint=fint):<{len_lim}}")
		print(''.join(s))


def run()->None:
	"""Method called by CLI to print requested information from a fitlist file 
	to std_out, using `sys.argv`. """
	if len(sys.argv)<2 or "-h" in sys.argv or "--help" in sys.argv:
		print(helptext)
		sys.exit(0)
	fl = Fitlist(sys.argv[-1])

	do_print_header = "--noheader" not in sys.argv
	if "-C" in sys.argv or "--Calibrations" in sys.argv:
		# collect all calibrations for every spectrum in a dict, with the key equal to the spc name and the value equal a list of all saved calibrations
		coll = {}
		maxlen = [15, 10]
		for peak in fl:
			if len(peak.spc_name)>maxlen[0]+2: maxlen[0] = len(peak.spc_name)+2
			if len(peak.calibration)>maxlen[1]+2: maxlen[1] = len(peak.calibration)+2
			if peak.spc_name not in coll.keys():
				coll[peak.spc_name] = [peak.calibration]
			elif peak.calibration not in coll[peak.spc_name]: # if different peaks have been fit with differing calibrations
				coll[peak.spc_name].append(peak.calibration)
		# print a name <-> calibration pair for every CALIBRATION (name might not be sufficient for multiple calibrations)
		if do_print_header: print(f"{'spectrum name':<{maxlen[0]}} {'calibration':<{maxlen[1]}}")
		for key, val in coll.items():
			for v in val:
				print(f"{key:<{maxlen[0]}} {v:<{maxlen[1]}}")
	elif "-I" in sys.argv or "--Integrals" in sys.argv:
		# determine printed labels
		labels = ["Int. ID", " Pos", " Δ Pos", " Vol", " Δ Vol", " Width", " Δ Wid", " Skew", " Δ Skew"]
		iter_labels = ["int_id", "int_pos", "int_dpos", "int_vol", "int_dvol", "int_width", "int_dwidth", "int_skew", "int_dskew"]
		sep_len = 8
		# print to console
		if do_print_header: print("\nTotal Integrals:")
		integral_printer(fl, "tot", labels, iter_labels, sep_len)
		if do_print_header: print("\nBackground Integrals:")
		integral_printer(fl, "bg", labels, iter_labels, sep_len)
		if do_print_header: print("\nSubtracted Integrals:")
		integral_printer(fl, "sub", labels, iter_labels, sep_len)
	else:
		# determine printed labels
		if "-l" in sys.argv or "--labels" in sys.argv:
			labels = []
			iter_labels = []
			ini = sys.argv.index("-l")+1 or sys.argv.index("--labels")+1
			while ini<len(sys.argv)-1 and not sys.argv[ini].startswith('-'):
				try:
					labels.append(fmt_name[sys.argv[ini]])
					iter_labels.append(sys.argv[ini])
					ini += 1
				except KeyError:
					print(f"Invalid label '{sys.argv[ini]}' encountered in '-l' option! Refer to help page to display all valid keys.")
					sys.exit(-1)
			if not labels:
				print(f"At least one valid label has to be specified when using the '-l' option.")
				sys.exit(1)
		else:
			labels = [" Position", " Δ Pos", " Volume", " Δ Vol", " Width", "  Δ Wid", " Background", "Δ BG", "\bBG Model"]
			iter_labels = ["pos", "dpos", "vol", "dvol", "width", "dwidth", "bg", "dbg", "bg_model"]
		# determine table spacing for print-out
		sep_len = 8
		len_lim = print_header(labels, sep_len)
		for peak in fl:
			s = []
			for label in iter_labels:
				s.append(f"{get_fmt_val_from_key(fl, peak, label):<{len_lim}}")
			print(''.join(s))


if __name__ == "__main__":
	usefile_path = f"python3 {sys.argv[0]}"
	run()