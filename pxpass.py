import os
os.system('clear')  
hh = " \033[1;37m "
print ( hh )
print ("""..... .J#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#7 ......
.... .P&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&7 .....
.... Y@&&&@&&&&&@@&&&&&&&&&&&&&&&&####&&&&&#: ....
... ^#&&#PJ7!~~!?YG&@&&&&&&&&#GJ!~^^^!?JP#&&? ....
... ?@&P5PGP7!~^^:.^?G&&&&&B?^.:^^!7JP#BGPB&P ....
... P@##&&&&&&#GJ!~~^7&&&&&5^~~~?P#&&&&&&&#&B: ...
....B&&&&@&&&&&@@#5^~P&&&&&&Y!Y#@&#BBB#&&&&&&~ ...
.. :#&&@BJ7~~^~!?P#B: 5&&&&#5##5?^:...:~?P##&7 ...
.. ^#&57.        .^G7 ~&&&&&&&?::^^^^^^^^7Y5P7 ...
.. :#&Y?Y5PPPGGGBB#&7 ^#&&&&&&&#########&&&#&Y ...
....G@&@@&&&&&&&&&&&^ ^&&&&&&&&&&&&&&&&&&&&&&Y ...
... :5@&&&&&&&&&&&@G. !&&&&&&&&&&&&&&&&&&&&&B~ ...
... !~YB&&&&&&&#&#P^  7&&&&&#PG&&&#&&&&&&#GY~ ....
... !B^.!!JPPPPBP:.7: Y&&&&&#GYY&&PY55J7?!.5! ....
.... 7B~7!.5&&&&B!Y&^.G&&&&&&&&B&&&##5:^P^?P......
..... ?#??!.^JP#&&&&Y.YBB#BYG&&&&&#P~ ~G7?B^ .....
...... 7&5!7!: .^!7!:  ^?!. .!77!~: ^?J^JB~ ......
....... !#B!^J5J!^:...!PBG?.  ..^!JG#7:PB^ .......
........ ^G&J.^JG##BBBBGPGGPPGB##&&&5?#P: ........
......... .J&P. JGGPGGPPPP5G#&&&&&#JY#J. .........
..........  !#G:5&&&##5.  .5#&&&&#JG#! ...........
............ ^PPY&&&&&P.. ^#&&&&&##G^ ............
.............  !P&&&&B: .. J&&&&&&J. .............
............... .J#&&#^ .. J&&&&G!  ..............
................  !G&&Y . ^#&&B?. ................""")
print ( """
""")
n = " \033[1;31m "
print ( n )
print ( " ~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~`~")
from colorama import init, Fore


init()


print(Fore.LIGHTBLACK_EX + "")
print ( " -*this tool was made by 'BOYARB'")
print ( " -*The tool is not located on any repository")
print ( " -*The tool is not open source")
print ( n )
print ( " ~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~¬~")
m = " \033[1;36m "
print ( m )


import base64


def encode_base64(message):
    message_bytes = message.encode('utf-8')  
    encoded_message = base64.b64encode(message_bytes)  
    return encoded_message.decode('utf-8')  


def decode_base64(encoded_message):
    encoded_bytes = encoded_message.encode('utf-8')  
    decoded_bytes = base64.b64decode(encoded_bytes)  
    return decoded_bytes.decode('utf-8')  


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
    
    
    if choice == "1 ":
        message = input("Enter text to encrypt it : ")
        encoded_message = encode_base64(message)  
        pp =  " \033[1;33m "
        print ( pp )
        print(f"The text has been encrypted : [{encoded_message}]")
    
    elif choice == "2 ":
        encoded_message = input("Enter the ciphertext : ")
        decoded_message = decode_base64(encoded_message)  
        
        
        tt = " \033[1;33m " 
        print ( tt )
        print(f"Decrypted : [{decoded_message}]")
    
    else:
        print("")
        return


if __name__ == "__main__":
    main()
    
    
    
