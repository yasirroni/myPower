def t_most_3b_3_1_2(*args,nout=1,oc=None):
	if oc == None:
		from .....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_most_3b_3_1_2(*args,nout=nout)
