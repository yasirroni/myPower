def miqps_ot(*args,nout=5,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.miqps_ot(*args,nout=nout)
