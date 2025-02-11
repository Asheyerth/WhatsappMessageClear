
def procesarMsg(msg):
    pmsg = msg[(msg.find(':',msg.find(']')+1)+2):]
    newLine(msg)
    
    #print(msg)
    return pmsg


def newLine(linea):
    resultado=linea.splitlines()
    print(len(resultado)-1)