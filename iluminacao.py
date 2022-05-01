from controlador import controlador

class Iluminacao (controlador):
	#construtor
	def __init__(self):
		self._ligado = False
		self._intensidade = 0
		self._cor = 0
		self._cores = ["branco", "verde", "azul", "rosa"]

	#getters e setters
	def getLigado(self):
		return self._ligado

	def getIntensidade(self):
		return self._intensidade

	def getCor(self):
		return self._cor

	def getCores(self):
		return self._cores[self._cor]

	def setLigado(self, l:bool):
		self._ligado = l

	def setIntensidade(self, i:int):
		self._intensidade = i

	def setCor(self, c:int):
		self._cor = c

	#Métodos especiais

	def ligar(self):
		self.setLigado(True)
		self.exibirLigado()

	def desligar(self):
		self.setLigado(False)
		self.exibirLigado()

	def aumentarIntensidade(self):
		if (self.getIntensidade() < 100):
			self.setIntensidade(self.getIntensidade()+1)
			self.exibirIntensidade()

	def diminuirintensidade(self):
		if (self.getIntensidade() > 0):
			self.setIntensidade(self.getIntensidade()-1)
			self.exibirIntensidade()
			
	def mudarCor(self):
		self.setCor((self.getCor()+1)%4)
		self.exibirCor()

	def exibirLigado(self):
		if self.getLigado():
			print("luz Ligada")
		else:
			print("luz Desligada")

	def exibirIntensidade(self):
		print(f"Intensidade = {self.getIntensidade()}")

	def exibirCor(self):
		print(f"Cor = {self.getCores()}")

	def exibirEstado(self):
		print("="*45)
		self.exibirLigado()
		self.exibirIntensidade()
		self.exibirCor()
		print("="*45)
		print()
