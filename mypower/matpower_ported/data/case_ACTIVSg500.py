def case_ACTIVSg500(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.case_ACTIVSg500(*args,nout=nout)