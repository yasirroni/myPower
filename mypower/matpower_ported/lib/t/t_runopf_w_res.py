def t_runopf_w_res(*args,nout=1,oc=None):
	if oc == None:
		from ....oc_api import oc_matpower
	oc = oc_matpower()
	return oc.t_runopf_w_res(*args,nout=nout)
