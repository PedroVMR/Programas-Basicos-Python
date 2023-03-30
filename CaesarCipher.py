from replit import clear

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

code_on = True

while code_on:
    code_on = True

    clear()
    print(logo)
    direction = input("Digite 'encode' para Criptografar, digite 'decode' para Descriptografar:\n")
    text = input("Digite a mensagem:\n").lower()
    shift = int(input("Digite o número de substituição:\n"))

    def user_choiceEnd():
        global code_on
        user_choice_end = input("Você deseja rodar o código de novo [S/N]: ").lower()
        if user_choice_end == "n":
            code_on = False
        elif user_choice_end == "s":
            code_on = True

    def encrypt(plain_text, shift_amount):
        encrypt_text = ""
        for char in plain_text:
            if char in alphabet:
                char_index = alphabet.index(char)
                encrypt_text += alphabet[(char_index + shift_amount) % len(alphabet)]
            else:
                encrypt_text += char

        print(f"A mensagem é: {encrypt_text}")
        return encrypt_text
        
    if direction == "encode":
        encrypted_text = encrypt(plain_text=text, shift_amount=shift)
        user_choice = input("Você deseja descriptografar a mensagem [S/N]: ").lower()
        if user_choice == "s":
            cipher_password = int(input("Digite o número correto da cifra: "))
            if cipher_password == shift:
                encrypt(plain_text = encrypted_text, shift_amount = - shift)
                user_choiceEnd()

            else:
                print("Senha Inválida")
                user_choiceEnd()

        elif user_choice == "n":
            print("Obrigado por usar o código ;D")
            user_choiceEnd()

    elif direction == "decode":
        encrypt(plain_text = text, shift_amount = - shift)
        user_choiceEnd()

    else:
        print("Opção Inválida")
        user_choiceEnd()
