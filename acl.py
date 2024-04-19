acl=int(input("Ingrese numero de la ACL: "))
if acl >= 1 and acl <= 99 :
	print("Es una ACL estandar")
else:
	if acl >= 100 and acl <= 199 :
		print("Es una ACL extendida")
	else:
		print("ACL fuera de rango")
