from controlador import controlador

class Alarme(controlador):
	#construtor
	def __init__(self):
		self._ligado = False
		self._intensidade = 0
		self._sensor = False
		self._apitar = False

	#getters e setters
	def getLigado(self):
		return self._ligado

	def getIntensidade(self):
		return self._intensidade

	def getSensor(self):
		return self._sensor

	def getApitar(self):
		return self._apitar

	def setLigado(self, l:bool):
		self._ligado = l

	def setIntensidade(self, i:int):
		self._intensidade = i

	def setSensor(self, s:bool):
		self._sensor = s

	def setApitar(self, a:bool):
		self._apitar = a

	#Métodos especiais

	def ligar(self):
		self.setLigado(True)
		self.exibirLigado()

	def desligar(self):
		self.setLigado(False)
		self.exibirLigado()

	def aumentarIntensidade(self):
		if self.getIntensidade() < 100:
			self.setIntensidade(self.getIntensidade()+1)
			self.exibirIntensidade()

	def diminuirIntensidade(self):
		if self.getIntensidade() > 0:
			self.setIntensidade(self.getIntensidade()-1)
			self.exibirIntensidade()

	def apitar(self):
		if self.getSensor():
			self.setApitar(True)
		else:
			self.setApitar(False)

		self.exibirSensor()
		self.exibirApitar()

	def ligarSensor(self):
		self.setSensor(True)
		self.exibirSensor()

	def exibirLigado(self):
		if self.getLigado():
			print("Alarme Ligado")
		else:
			print("Alarme Desligado")

	def exibirIntensidade(self):
		print(f"Intensidade = {self.getIntensidade()}")

	def exibirSensor(self):
		if self.getSensor():
			print(f"Sensor detectando invasor...")
		else:
			print(f"Sensor não está detectando ninguém...")

	def exibirApitar(self):
		if self.getApitar():
			print("Alarme apitando")
		else:
			print("Alarme não está apitando")
		
	def exibirEstado(self):
		print("="*45)
		self.exibirLigado()
		self.exibirIntensidade()
		self.exibirSensor()
		self.exibirApitar()
		print("="*45)
		print()
