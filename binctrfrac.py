fstr = []
for i in range(102857600):
    s = str(format(i,'b')) 
    s += ((20 - len(s))*"0")
    fstr.append(s + "\n")
file1 = open("binfrac.txt","w")
file1.writelines(fstr)
file1.close()
