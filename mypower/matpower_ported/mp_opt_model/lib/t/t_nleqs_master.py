def t_nleqs_master(*args,nout=3,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_nleqs_master(*args,nout=nout)
