from controlador import controlador

class Televisao(controlador):

	#construtor
	def __init__(self):
		self._ligado = False
		self._volume = 0
		self._canal = 1
		self._modo = 0
		self._modos = ["TV", "AV", "HDMI", "USB"]
		
	#getters e setters	
	def getLigado(self):
		return self._ligado

	def getVolume(self):
		return self._volume

	def getCanal(self):
		return self._canal

	def getModo(self):
		return self._modo

	def getModos(self):
		return self._modos[self._modo]

	def setLigado(self, l:bool):
		self._ligado = l

	def setVolume(self, v:int):
		self._volume = v

	def setCanal(self, c:int):
		self._canal = c

	def setModo(self, m:int):
		self._modo = m

	#métodos especiais
	def ligar(self):
		self.setLigado(True)
		print("TV ligada")
		
	def desligar(self):
		self.setLigado(False)
		print("Tv Desligada")

	def exibirLigado(self):
		if(self.getLigado()):
			print("TV Ligada")
		else:
			print("TV Desligada")
		
	def exibirVolume(self):
		print(f"Volume = {self.getVolume()}")

	def exibirCanal(self):
		print(f"Canal = {self.getCanal()}")

	def exibirModo(self):
		print(f"Modo = {self.getModos()}")

	def aumentarVolume(self):
		if (self.getVolume() < 100):
			self.setVolume(self.getVolume()+1)
			self.exibirVolume()
		else:
			print("Volume MAX")

	def diminuirVolume(self):
		if (self.getVolume() > 0):
			self.setVolume(self.getVolume()-1)
			self.exibirVolume()
		else:
			print("Volume MIN")

	def avancarCanal(self):
		self.setCanal((self.getCanal()+1)%101)

	def diminuirCanal(self):
		if (self.getCanal() > 1):
			self.setCanal(self.getCanal()-1)
		else:
			self.setCanal(100)

	def mudarCanal(self, c:int):
		if (0 < self.getCanal() <= 100):
			self.setCanal(c)
			self.exibirCanal()
		else:
			print("Canal não existe")

	def mudarModo(self):
		self.setModo((self.getModo()+1)%4)
		self.exibirModo()

	def exibirEstado(self):
		print("="*45)
		self.exibirLigado()
		self.exibirCanal()
		self.exibirVolume()
		self.exibirModo()
		print("="*45)
		print()
		

	