def contab_ACTIVSg2000(*args,nout=1,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.contab_ACTIVSg2000(*args,nout=nout)
