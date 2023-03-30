
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Digite 'encode' para Criptografar, digite 'decode' para Descriptografar:\n")
text = input("Digite a mensagem:\n").lower()
shift = int(input("Digite o número de substituição:\n"))

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

        else:
            print("Senha Inválida")

    elif user_choice == "n":
        print("Obrigado por usar o código ;D")

elif direction == "decode":
    encrypt(plain_text = text, shift_amount = - shift)

else:
    print("Opção Inválida")
