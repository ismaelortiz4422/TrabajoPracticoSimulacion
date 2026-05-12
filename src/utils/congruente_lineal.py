class CongruenteLineal:
    def __init__(self, a, c, m, seed):
        self.a = a
        self.c = c
        self.m = m
        self.semilla_inicial = seed
        self.ultima_semilla = seed
        
    def generar_siguiente_numero(self):
        #Primero toma el valor de la semilla actual, 
        #luego calcula el siguiente número pseudoaleatorio usando la fórmula del congruente lineal 
        #y finalmente devuelve un valor entre 0 y 1, acutalizando la semilla para la próxima generación.
        self.ultima_semilla = (self.a * self.ultima_semilla + self.c) % self.m
        return self.ultima_semilla / self.m # Valor entre [0, 1)

if __name__ == "__main__":
    """Prueba del generador de números pseudoaleatorios utilizando el método del congruente lineal.
    Una forma de probar fue viendo el ultimo número generado en el for para ver si siempre era el mismo
    bajo la misma semilla."""
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = int(input("Ingrese la semilla inicial: "))
    congruente = CongruenteLineal(a, c, m, seed)
    randoms_llegada_buques = []
    for _ in range(1000000):
        randoms_llegada_buques.append(congruente.generar_siguiente_numero())
    print(randoms_llegada_buques)
    print(len(randoms_llegada_buques))