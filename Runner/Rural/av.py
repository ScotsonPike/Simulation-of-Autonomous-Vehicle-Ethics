from os import walk
def main():
    f = []
    numArr = []
    mypath = "Data"
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(dirnames)
        break
        
    for x in f:
        mypath = "Data"+"/"+x
        fileList = []
        for (dirpath, dirnames, filenames) in walk(mypath):
            fileList.extend(filenames)
            break
        sim = ""
        for y in fileList:
            if y.find("sim") != -1:
                sim = y
                               
        mypath =mypath+"/"+sim 
        file = open(mypath)
        line = ""
        for z in file:
            if z.find("Fitness") != -1:
                line = z
        for z in line:
            z.split(":", 1)[-1]
            z.split()
        
        arr = []
        print(line)
        for a in line:
            print(a)
            try:
                str(a)
                arr.extend(a)
            except:
                print("Exception")
                continue
        num = 0
        #for fit in arr:
        #    print(fit)
        #    num += str(fit)
        #num = num/len(line)
        #print(str(num))
            
        
main()