class KgToPounds:
	def __init__(self, kg = 0):
		self.__kg = kg

	def get_kg(self):
		return self.__kg

	def set_kg(self, new_kg):
		self.__kg = new_kg

	def to_pounds(self):
		return self.__kg*2.205

	kgg = property(get_kg, set_kg)


first = KgToPounds()
first.kgg = 35
print(first.to_pounds())
getKg = first.kgg
print(getKg)