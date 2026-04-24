import math

class OracleCore:
    def __init__(self):
        # Por ahora no pedimos API Key para probar la lógica pura
        pass

    def poisson(self, k, lamb):
        """Calcula la probabilidad de que ocurran exactamente k eventos"""
        return (lamb**k * math.exp(-lamb)) / math.factorial(k)

    def analizar_partido(self, lambda_local, lambda_visitante):
        """
        Calcula las probabilidades de Gana/Empata/Pierde 
        basado en los promedios de goles (Lambdas).
        """
        prob_local = 0
        prob_empate = 0
        prob_visitante = 0
        
        # Analizamos un rango de hasta 5 goles por equipo (lo más común)
        for goles_l in range(6):
            for goles_v in range(6):
                p = self.poisson(goles_l, lambda_local) * self.poisson(goles_v, lambda_visitante)
                
                if goles_l > goles_v:
                    prob_local += p
                elif goles_l == goles_v:
                    prob_empate += p
                else:
                    prob_visitante += p
                    
        return {
            "Gana Local": round(prob_local * 100, 2),
            "Empate": round(prob_empate * 100, 2),
            "Gana Visitante": round(prob_visitante * 100, 2)
        }

# --- PRUEBA DE FUEGO ---
# Supongamos que Nacional (local) promedia 1.8 goles y Millonarios (visita) 1.2
oracle = OracleCore()
resultado = oracle.analizar_partido(1.8, 1.2)

print(f"Probabilidades calculadas:")
for clave, valor in resultado.items():
    print(f"{clave}: {valor}%")
