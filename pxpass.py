#اسم الاداه PxPass
import os
os.system('clear')  # لمسح محتوى الشاشة في Termux
hh = " \033[1;37m "
print ( hh )

import pyfiglet
print ( pyfiglet.figlet_format ( ' PXPASS ' ))

n = " \033[1;31m "
print ( n )
print ( " ~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~")
from colorama import init, Fore

# تفعيل مكتبة colorama
init()

# طباعة النص باللون الرمادي
print(Fore.LIGHTBLACK_EX + "")
print ( " -*this tool was made by 'BOYARB🍷'")

print ( " -*The tool is open source!!")
print ( n )
print ( " ~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~")
m = " \033[1;36m "
print ( m )


import base64

# دالة لتشفير النص باستخدام Base64
def encode_base64(message):
    message_bytes = message.encode('utf-8')  # تحويل النص إلى بايتات
    encoded_message = base64.b64encode(message_bytes)  # تشفير النص إلى Base64
    return encoded_message.decode('utf-8')  # تحويل النتيجة إلى نص قابل للطباعة

# دالة لفك تشفير النص المشفر باستخدام Base64
def decode_base64(encoded_message):
    encoded_bytes = encoded_message.encode('utf-8')  # تحويل النص المشفر إلى بايتات
    decoded_bytes = base64.b64decode(encoded_bytes)  # فك تشفير النص من Base64
    return decoded_bytes.decode('utf-8')  # تحويل النتيجة إلى نص قابل للطباعة

# واجهة المستخدم
def main():
    print("")
    print("1 : Text encryption")
    print ( """
    """)
    print("2 : To decrypt text")
    print ( """
    """)
    print ( "3 : exit ")
    print ( """
    """)
    o = " \033[1;34m  "
    print ( o )
    
    choice = input("Enter the number : ")
    lm = " \033[1;37m "
    print ( lm )
    
    
    if choice == "1":
        message = input("Enter text to encrypt it : ")
        encoded_message = encode_base64(message)  # تشفير النص
        pp =  " \033[1;33m "
        print ( pp )
        print(f"Text encryption : [{encoded_message}]")
    
    elif choice == "2":
        encoded_message = input("Enter the ciphertext : ")
        decoded_message = decode_base64(encoded_message)  # فك تشفير النص
        
        
        tt = " \033[1;33m " 
        print ( tt )
        print(f"Decryption : [{decoded_message}]")
    
    else:
        print("")
        return

# تشغيل الأداة
if __name__ == "__main__":
    main()
    
