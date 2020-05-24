#Refrences:-https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
#References:-https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
def Encryption(plain_text,key):

    Cipher=''

    for char in plain_text:

        if char == '':

          Cipher=Cipher+char


        elif char.isupper():

            index=ord(char) - ord('A')

            Cipher= Cipher+chr((index+key) % 26 + ord('A'))


        else:

            index=ord(char) - ord('a')

            Cipher= Cipher+chr((index+key) %26 +ord('a'))


    return  Cipher



text=input("Enter the plain text:")
s=int(input("Enter the key:"))

print("Plain Text:" ,text)
print("Cipher Text:" ,Encryption(text,s))



        
