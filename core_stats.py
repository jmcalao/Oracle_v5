import requests

class OracleCore:
    # ... (mantén tus funciones def poisson y def analizar_partido intactas) ...

    def obtener_datos_equipo(self, team_id, api_key):
        """
        Consulta los últimos 10 partidos y devuelve el 
        promedio de goles anotados y recibidos (Conexión Directa API-Sports).
        """
        url = "https://v3.football.api-sports.io/fixtures"
        
        # ¡OJO AQUÍ! Cambiamos los headers para la conexión directa
        headers = {
            'x-apisports-key': api_key
        }
        
        # Pedimos los últimos 10 partidos terminados del equipo
        params = {"team": team_id, "last": 10, "status": "FT"}
        
        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            
            # Verificamos si la API nos devolvió un error de autenticación
            if "errors" in data and data["errors"]:
                print(f"Error de la API: {data['errors']}")
                return None

            goles_anotados = 0
            goles_recibidos = 0
            
            for partido in data['response']:
                if partido['teams']['home']['id'] == team_id:
                    goles_anotados += partido['goals']['home']
                    goles_recibidos += partido['goals']['away']
                else:
                    goles_anotados += partido['goals']['away']
                    goles_recibidos += partido['goals']['home']
            
            return {
                "lambda_ataque": goles_anotados / 10,
                "lambda_defensa": goles_recibidos / 10
            }
        except Exception as e:
            print(f"Error extrayendo datos: {e}")
            return None
