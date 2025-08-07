import pickle
listvalues=[1,"Amit",'M',28]
fileobject=open("mybinary.dat","wb")
pickle.dump(listvalues,fileobject)
fileobject.close()
