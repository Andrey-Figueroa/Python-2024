from Crypto.Cipher import AES 
from secrets import token_bytes  #Generador de claves aleatorias

key = token_bytes(16) #16 bytes por lo que seran 128 bits

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode("ascii"))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce = nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode("ascii")
    except:
        return False
    
nonce, ciphertext, tag = encrypt(input("Ingresa un mensaje: "))
plaintext = decrypt(nonce, ciphertext, tag)
print(f"Cipher text: {ciphertext}")
if not plaintext:
    print("El mensaje esta dañado")
else:
    print(f"Plain text: {plaintext}")









#CODIGO MORSE
def codigoMorse(pCadena):
    codificado=''
    morse = {'A':'.-','B':'-...','C':'-.-.','CH':'----','D':'-..','E':'.','F':'..-.','G':'--.',
        'H':'....','I':'..','J':'.---','K':'-.-','L':'.-..','M':'--','N':'-.','Ñ':'--.--','O':'---',
        'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-','U':'..-','V':'...-','W':'.--','X':'-..-',
        'Y':'-.--','Z':'--..','0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
        '6':'-....','7':'--...','8':'---..','9':'----.','.':'.-.-.-',',':'--..--','?':'..--..','"':'.-..-.'}
    pCadena=pCadena.upper()
    while(pCadena != ""):
        if(len(pCadena) >= 2):
            if(pCadena[0] == "C" and pCadena[1] == "H"):
                codificado += morse["CH"] + "*"
                pCadena = pCadena[2:]
            else:
                codificado += morse[pCadena[0]] + "*"
                pCadena = pCadena[1:]
        else:
            codificado += morse[pCadena[0]] + "*"
            pCadena = pCadena[1:]
    return codificado.strip('*')
print(codigoMorse("sac"))