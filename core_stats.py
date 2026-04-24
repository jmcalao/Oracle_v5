import requests

class OracleCore:
    # ... (aquí mantén tus funciones de poisson y analizar_partido) ...

    def obtener_datos_equipo(self, team_id, api_key):
        """
        Consulta los últimos 10 partidos y devuelve el 
        promedio de goles anotados y recibidos.
        """
        url = "https://v3.football.api-sports.io/fixtures"
        headers = {
            'x-rapidapi-key': api_key,
            'x-rapidapi-host': 'v3.football.api-sports.io'
        }
        
        # Pedimos los últimos 10 partidos terminados
        params = {"team": team_id, "last": 10, "status": "FT"}
        
        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            
            goles_anotados = 0
            goles_recibidos = 0
            
            for partido in data['response']:
                # Verificamos si el equipo era local o visitante para sumar bien
                if partido['teams']['home']['id'] == team_id:
                    goles_anotados += partido['goals']['home']
                    goles_recibidos += partido['goals']['away']
                else:
                    goles_anotados += partido['goals']['away']
                    goles_recibidos += partido['goals']['home']
            
            # Calculamos el Lambda (promedio)
            return {
                "lambda_ataque": goles_anotados / 10,
                "lambda_defensa": goles_recibidos / 10
            }
        except Exception as e:
            print(f"Error extrayendo datos: {e}")
            return None
