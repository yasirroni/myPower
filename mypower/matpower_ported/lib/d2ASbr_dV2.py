def d2ASbr_dV2(*args,nout=4,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.d2ASbr_dV2(*args,nout=nout)
