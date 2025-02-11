import re
import sqlite3

# Texto de la señal
signal_text = """
¡ShifuX New Signal Detected! 

 Curve Gateway (Curve)
AEimEqQaD1y1wtyDy6qjmKZe8fLACmLaW3LNrsu7pump

💰 Marketcap: $93.15K
👥 Holders: 37 | T10 68.69%  | T25 78.98% | T50 79.31%
💼 Dev Holds: 0

Special Remarks:
🫣 Dev bought 400.00M tokens with 17.83 SOL or 40% (50% of curve)
🤔 Dev created 1 other tokens
🤔 This name is the same as 255 other tokens
🤔 This website is the same as 270 other tokens
🤔 This telegram is the same as 469 other tokens
🤔 This twitter is the same as 404 other tokens

Twitter | Website

(Esta señal llego 1 minuto después que el grupo privado)
"""


# Expresiones regulares para extraer los datos
name_pattern = r"([\w\s\$\d\.'\-]+)\s\(([\w]+)\)"  # Más flexible para nombres con números y símbolos
contract_pattern = r"([A-Za-z0-9]{40,})"
marketcap_pattern = r"Marketcap:\s(\$\d+\.?\d*[KMB]?)"

# Extraer el nombre de la moneda
name_match = re.search(name_pattern, signal_text)
if name_match:
    coin_name = name_match.group(1).strip()
    coin_symbol = name_match.group(2).strip()
else:
    coin_name = "No encontrado"
    coin_symbol = "No encontrado"

# Extraer el contrato
contract_match = re.search(contract_pattern, signal_text)
contract_address = contract_match.group(1) if contract_match else "No encontrado"

# Extraer el marketcap
marketcap_match = re.search(marketcap_pattern, signal_text)
marketcap = marketcap_match.group(1) if marketcap_match else "No encontrado"

# Mostrar los resultados
print(f"Nombre de la moneda: {coin_name} ({coin_symbol})")
print(f"Contrato: {contract_address}")
print(f"Marketcap: {marketcap}")

# Conectar a la base de datos SQLite (o crearla si no existe)
conn = sqlite3.connect('cryptos1.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS cryptos1 (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    symbol TEXT NOT NULL,
    contract_address TEXT NOT NULL,
    marketcap TEXT NOT NULL,
    mc_ath INTEGER NOT NULL DEFAULT 0
)
''')

# Insertar los datos en la tabla
cursor.execute('''
INSERT INTO cryptos1 (name, symbol, contract_address, marketcap)
VALUES (?, ?, ?, ?)
''', (coin_name, coin_symbol, contract_address, marketcap))

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos guardados en la base de datos.")