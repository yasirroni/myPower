def t_most_spuc(*args,nout=5,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_most_spuc(*args,nout=nout)
