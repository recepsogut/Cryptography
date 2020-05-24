#Refrences:-https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
#References:-https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/

def Encryption(plain_text,key):

    Encrypt=''

    for char in plain_text:

        if char == '':

            Encrypt=Encrypt+char

        elif char.isupper():

            index=ord(char) - ord('A')

            Encrypt=Encrypt+chr((index+key) % 26 + ord('A'))

        else:

            index=ord(char) - ord('a')

            Encrypt=Encrypt+chr((index+key) % 26 + ord('a'))

    return Encrypt 



def Decryption(cipher_text,ke):

  
    Decrypt=''

    for ch in cipher_text:

        if ch == '':

            Decrypt=Decrypt+ch

        elif ch.isupper():

            index=ord(ch) - ord('A')

            Decrypt=Decrypt+chr((index-ke) % 26 + ord('A'))

        else:

            index=ord(ch) - ord('a')

            Decrypt=Decrypt+chr((index-ke) % 26 + ord('a'))

    return Decrypt





s=input("Select 1.Encryption\n 2.Decryption\n choose(1,2) :")

if s == "1":        
    w=input("Enter the Plain text:")
    x=int(input("Enter the key:"))  

    print("Cipher:",Encryption(w,x))

elif s == "2":

    q=input("Enter the Cipher text:")
    a=int(input("Enter the key:"))  

    print("Plain text:" ,Decryption(q,a))

else:

     print("wrong choice")  



  
            
            

            

               
                

    
