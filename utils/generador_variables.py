import random
import math

class GeneradorVariables:
    def exponencialNegativa(self, media, rndgenerado):
        return - (media) * math.log(1 - rndgenerado)
    
    def uniforme(self, a, b, rndgenerado):
        return a + rndgenerado * (b - a)
    