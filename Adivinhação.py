import random

def main():
	nome = input("[+] Me diga o seu nome> ")
	decisao = input(f"[+] Olá {nome} você vai querer jogar? ").lower()
	if decisao == "não" or decisao == "nao":
		print("[!] Poxa que triste :( ")
	elif decisao == "sim":
		print("Me diga um começo e fim inteiro e eu irei escolher um número pra você tentar adivinhar")
		while True:
			inicio = int(input("Me diga o número de inicio> "))
			fim = int(input("Me diga o número de fim> "))
			if fim < inicio:
				print("[!] O número escolhido para ser fim não pode ser menor que o de inicio")
			elif fim == inicio or inicio == fim:
				print("[!] Os números escolhidos para fim e inicio não podem ser iguais")
			elif (fim-inicio)==1:
				print("[!] É preciso que exista pelo menos 1 numero inteiro entre o inicio e fim")
			else:
				break
		numero_computador = random.randint(inicio,fim)
		count = 0
		tentativas = []
		while True:
			if numero_computador == fim or numero_computador == inicio:
				numero_computador = random.randint(inicio,fim)
			else:
				break
		while True:
			numero_jogador=int(input("[+] Me diga o seu numero> "))
			if numero_jogador > numero_computador and numero_jogador < fim:
				print("[!] O número que pensei é menor")
				count+=1
				tentativas.append(numero_jogador)
			elif numero_jogador < numero_computador and numero_jogador > inicio:
				print("[!] O número que pensei é maior")
				count+=1
				tentativas.append(numero_jogador)
			elif numero_jogador > fim:
				print("[!] Você precisa colocar um numero menor que o seu fim")
				count+=1
				tentativas.append(numero_jogador)
			elif numero_jogador < inicio:
				print("[!] Você precisa colocar um numero menor que o seu inicio")
				count+=1
				tentativas.append(numero_jogador)
			elif numero_jogador == numero_computador:
				print(f"Parabéns {nome} o seu numero de tentativas foi {count}!!")
				tentativas.append(numero_jogador)
				print(f"Suas tentativas foram = {tentativas}")
				break
			elif numero_jogador == inicio or numero_jogador == fim:
				print("[!] Coloque um valor inteiro dentro do limite estabelecido por você")
				count+=1
				tentativas.append(numero_jogador)
	else:
		print(f"[!] {nome}, você precisa responder com sim ou não")
if __name__ == "__main__":
	main()
