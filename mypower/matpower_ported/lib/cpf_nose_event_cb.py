def cpf_nose_event_cb(*args,nout=7,oc=None):
	if oc == None:
		from ...oc_api import oc_matpower
	oc = oc_matpower()
	return oc.cpf_nose_event_cb(*args,nout=nout)
