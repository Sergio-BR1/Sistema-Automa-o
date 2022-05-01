from tv import Televisao
from iluminacao import Iluminacao
from alarme import Alarme

if __name__ == "__main__":
	Tv = Televisao()
	Tv.exibirEstado()
	Tv.ligar()
	print()
	for i in range(10):
		Tv.aumentarVolume()

	Tv.diminuirCanal
	print()
	Tv.mudarCanal(25)
	print()
	Tv.mudarModo()
	print()
	Tv.exibirEstado()

	Tv.desligar()
	print()
	
	luz = Iluminacao()
	luz.exibirEstado()
	luz.ligar()
	print()
	for i in range(5):
		luz.aumentarIntensidade()
	print()

	luz.mudarCor()
	print()

	luz.desligar()
	
	
	al = Alarme()
	al.exibirEstado()

	al.ligar()
	print()
	for i in range(3):
		al.aumentarIntensidade()
	print()

	al.ligarSensor()
	print()

	al.apitar()
	print()

	al.desligar()
