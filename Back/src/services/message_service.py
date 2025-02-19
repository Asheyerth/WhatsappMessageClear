
def procesarMsg2(msg):
    #Una linea
    pmsg = msg[(msg.find(':',msg.find(']')+1)+2):]
    newLine(msg)
    
    #print(msg)
    return pmsg

def procesarMsg(msg):
    #Validación inicial
    import re #Expresiones regulares
    #[0-9]+ Números de 0-9 en una o más repeticiones
    #[ \t\n\r\f] Espacio en blanco
    #[a-zA-Z_] Cualquier letra
    #\\ Para validar los caracteres literales de [ y ]
    #El resto son caracteres plenos -> :.,/

    #Encontrar el formato inicial de hora+fecha
    p = re.compile('[0-9]+:[0-9]+[ \t\n\r\f][a-zA-Z_].[a-zA-Z_].,[ \t\n\r\f][0-9]+/[0-9]+/[0-9]+\\][ \t\n\r\f]')
    m = p.findall(msg) #Sacar en listas las coincidencias
    cant = len(m) #Cantidad de mensajes presentes

    #División por lineas
    txts = msg.split('\n[',cant) #Texts

    #Procesamiento cada linea
    #Retirar la parte inicial
    lista = []
    for x in txts:
        smsg = p.search(x)
        lista.append(x[smsg.end():]) #Splitted Messages
    return lista #Retorna lista sin retirar los usuarios

def procesarMsgBasic(msg):
    pmsg = '' #processed messages
    msgs = procesarMsg(msg) #Messages with user

    #Retiro del user
    for x in msgs:
        linea = x[x.find(':')+2:] #Se retira el user
        pmsg = pmsg + '\n' + linea #Se concatena todo

    return pmsg

def procesarMsgUserSender(msg,user):
    pmsg = '' #processed messages
    msgs = procesarMsg(msg) #Messages with user

    #Retiro del user
    for x in msgs:
        linea = x.removeprefix(user+': ') #Se retira el user dado por el usuario
        pmsg = pmsg + '\n' + linea #Se concatena todo

    return pmsg

def procesarMsgUserReplace(msg,user,replace):
    pmsg = '' #processed messages
    msgs = procesarMsg(msg) #Messages with user

    #Retiro del user
    for x in msgs:
        linea = x.removeprefix(user) #Se retira el user dado por el usuario
        linea = replace + linea
        pmsg = pmsg + '\n' + linea #Se concatena todo

    return pmsg



def newLine(linea):
    resultado=linea.splitlines()
    print(len(resultado)-1)