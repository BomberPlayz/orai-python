homerseklet=float(input("hőfok: "))
print(homerseklet <= 0 and ("A víz "+str(homerseklet)+" °C-n szilárd.") or homerseklet >= 100 and ("A víz "+str(homerseklet)+" °C-n gőz.") or homerseklet > 0 and ("A víz "+str(homerseklet)+" °C-n folyékony."))
