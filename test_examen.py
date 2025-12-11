import requests

# URL de tu servidor (según lo que configuramos en __init__.py)
url = 'http://127.0.0.1:5000/api/v1/scda/importar/alumnos'

# Abrimos el archivo ALUMNOS.TXT que acabas de crear
files = {'file': open('ALUMNOS.TXT', 'rb')}

try:
    print(f"Enviando archivo a {url}...")
    response = requests.post(url, files=files)
    
    print(f"Estado: {response.status_code}")
    print("Respuesta del Servidor:", response.json())
    
    if response.status_code == 201:
        print("\n✅ ¡ÉXITO TOTAL! El sistema procesó el archivo correctamente.")
    else:
        print("\n❌ Algo falló. Revisa el mensaje de error arriba.")

except Exception as e:
    print(f"\n❌ Error de conexión: {e}")
    print("Asegúrate de que el servidor (boot.ps1) siga corriendo en la otra terminal.")