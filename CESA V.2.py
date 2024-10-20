def cifradoCesar(pCadena):
    pCadena=pCadena.upper()
    cesar={'A':'D','B':'E','C':'F','D':'G','E':'H','F':'I','G':'J','H':'K','I':'L',
           'J':'M','K':'N','L':'O','M':'P','N':'Q','O':'R','P':'S','Q':'T',
           'R':'U','S':'V','T':'W','U':'X','V':'Y','W':'Z','X':'A','Y':'B','Z':'C',' ':' '}
    cifrado=''
    while(pCadena!=''):
        letra=cesar[pCadena[0]]
        cifrado+=letra
        pCadena=pCadena[1:]
    return cifrado
#print(cifradoCesar("tarea programada criptografia de datos"))




def contarEspacios(pCadena):
    contador = 0
    for caracter in pCadena:
        if(caracter == " "):
            contador += 1
    return contador 
#print(contarEspacios("Ho la Mun d o"))


def numerarApariciones(c,b):
    a = 0
    while(c != ""):
        if(c[0] == b[0]):
            indiceC = 0
            indiceB = 0
            contador = 0
            while(indiceC < len(c) and indiceB < len(b)):
                if(c[indiceC] == b[indiceB]):
                    contador += 1
                indiceC += 1
                indiceB += 1
            if(contador == len(b)):
                a += 1
        c = c[1:]
    return a

x = "Es muy tarde"
y = "muy" 
print(numerarApariciones(x,y))