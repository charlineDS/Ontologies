#La class sommet un id qui sera utilisé pour l'algorithme et la valeur pour l'utilisateur
class sommet:
    def __init__(self, id, value):
        self.id = id
        self.value = value
		
    def getId(self):
        return self.id
		
    def getValue(self):
        return self.value
