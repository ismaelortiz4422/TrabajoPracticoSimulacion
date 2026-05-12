class Buque:
    def __init__(self, id_buque, estado):
        self.id_buque = id_buque
        self.estado = estado
        self.hora_limite_espera = 18
        self.hora_inicio_entrada= None
        self.hora_inicio_fondeo = None
        self.hora_inicio_mantenimiento = None
        self.hora_fin_atencion = None
       
    def atracar(self, hora_inicio):
        if self.hora_inicio_entrada is None:
            self.hora_inicio_entrada = hora_inicio
        self.estado = "en_atraque"
        
    def fin_atencion(self, hora_fin):
        if self.hora_inicio_entrada is None:
            raise ValueError("El buque no ha comenzado su entrada, no se puede finalizar la atención.")
        self.hora_fin_atencion = hora_fin
        self.estado = "fin_atencion"
        
    def en_fondeo(self, hora_inicio):
        if self.hora_inicio_entrada is None:
            self.hora_inicio_entrada = hora_inicio
        self.hora_inicio_fondeo = hora_inicio
        self.estado = "en_fondeo"
        
    def esperando_mantenimiento(self, hora_inicio):
        if self.hora_inicio_entrada is None:
            self.hora_inicio_entrada = hora_inicio
        self.estado = "esperando_mantenimiento"
        self.hora_inicio_mantenimiento = hora_inicio