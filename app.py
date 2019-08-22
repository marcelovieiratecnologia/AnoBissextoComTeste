def anoBissexto(ano: int):
		
		if type(ano) is not int:
				raise TypeError("O ano deve ser um número inteiro.")
				return False

		if ano < 0:
				raise ValueError('O ano não pode ser menor que 0')
				return False

		if ano == 0:
				raise ValueError('O ano não pode ser 0')
				return False

		if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
				return True

		return False
