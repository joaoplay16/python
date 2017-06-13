def median(lista):
	lista.sort()
	print lista
	med = 0
	if len(lista) % 2 ==0:
		med = (float(lista[(len(lista)/2) - 1]) + lista[(len(lista)/2)])/2
	else:
		med = lista[(len(lista)/2)]
	return med
	
print median([4,5,5,4])

