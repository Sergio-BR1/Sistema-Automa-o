from abc import ABC, abstractmethod

class controlador(ABC):
	@abstractmethod
	def ligar(self):
		pass

	@abstractmethod
	def desligar(self):
		pass

	@abstractmethod
	def getLigado(self):
		pass
		
	@abstractmethod
	def exibirEstado(self):
		pass