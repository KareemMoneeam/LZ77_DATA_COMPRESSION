
def compress(myText):
    t_position = []
    t_length = []
    t_nextSymbol = []
    i=0
    while i<len(myText):
        p=0;l=0;s=myText[i];seq=""
        seq+= myText[i]
        j=myText.rfind(seq, 0, i)
        while(j!=-1 and i<len(myText)):
            p=(i-l)-j
            l+=1
            i+=1
            if(i<len(myText)):
                s=myText[i]
                seq+=myText[i]
                j=myText.rfind(seq,0,i-l)
            else:
                s="NULL"
        t_position.append(p)
        t_length.append(l)
        t_nextSymbol.append(s)
        i+=1
    for x in range(len(t_position)):
        print("<"+str(t_position[x])+","+str(t_length[x])+","+t_nextSymbol[x]+">")


myText = input("Enter the text: ")
compress(myText)
