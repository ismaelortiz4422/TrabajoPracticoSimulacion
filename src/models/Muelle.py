class Muelle:
    def __init__(self, id_muelle, estado):
        self.id_muelle = id_muelle
        self.estado = estado

    def ocupar(self):
        self.estado = "En descarga"
        
    def liberar(self):
        self.estado = "Libre"
        
    def mantener(self):
        self.estado = "Mantenimiento"
