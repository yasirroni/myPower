def bustypes(*args,nout=3,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.bustypes(*args,nout=nout)
