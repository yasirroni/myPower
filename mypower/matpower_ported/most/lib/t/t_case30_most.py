def t_case30_most(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_case30_most(*args,nout=nout)
