def dSbr_dV(*args,nout=6,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.dSbr_dV(*args,nout=nout)
