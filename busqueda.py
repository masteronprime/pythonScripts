from googlesearch import search

busqueda=input("Que desea buscar :")
for m in search(busqueda,num_results=10,lang="es"):

 print(m)
