def t_begin(*args,nout=2,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_begin(*args,nout=nout)
