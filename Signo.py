
dia = int(input("Digite o dia do seu aniversário: "))
mes = int(input("Digite o mês do seu aniversário: "))

signo = ""

def signos():

      if dia >=1 or dia >= 31 and mes >=1 or mes <=12:
            print("Data Inválida")
      if dia >= 21 and mes == 3 or dia <= 20 and mes == 4:
            signo = "Áries"
            print(f"Seu signo é {signo}")
      elif dia >= 21 and mes == 4 or dia <= 20 and mes == 5:
            signo = "Touro"
            print(f"Seu signo é {signo}")
      elif dia >= 21 and mes == 5 or dia <= 20 and mes == 6:
            signo = "Gêmeos"
            print(f"Seu signo é {signo}")
      elif dia >= 21 and mes == 6 or dia <= 21 and mes == 7:
            signo = "Câncer"
            print(f"Seu signo é {signo}")
      elif dia >= 22 and mes == 7 or dia <= 22 and mes == 8:
            signo = "Leão"
            print(f"Seu signo é {signo}")
      elif dia >= 23 and mes == 8 or dia <= 22 and mes == 9:
            signo = "Virgem"
            print(f"Seu signo é {signo}")
      elif dia >= 23 and mes == 10 or dia <= 21 and mes == 11:
            signo = "Escorpião"
            print(f"Seu signo é {signo}")
      elif dia >= 22 and mes == 11 or dia <= 21 and mes == 12:
            signo = "Sagitário"
            print(f"Seu signo é {signo}")
      elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
            signo = "Capricórnio"
            print(f"Seu signo é {signo}")
      elif dia >= 21 and mes == 1 or dia <= 19 and mes == 2:
            signo = "Aquário"
            print(f"Seu signo é {signo}")
      elif dia >= 20 and mes == 2 or dia <= 20 and mes == 3:
            signo = "Peixes"
            print(f"Seu signo é {signo}")
      else:
            print("Data Inválida")
signos()