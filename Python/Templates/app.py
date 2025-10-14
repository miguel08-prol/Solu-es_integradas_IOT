# Importa as bibliotecas necessárias
from flask import Flask, render_template
import serial
import time

# Bloco para tentar conectar com o Arduino via porta serial
# ==========================================================
# ATENÇÃO: Verifique a porta COM correta no seu IDE do Arduino (em Ferramentas > Porta)
# No Windows, será algo como 'COM3', 'COM4', etc.
try:
    # Tenta estabelecer a conexão serial
    arduino = serial.Serial('COM3', 9600, timeout=1)
    # Um tempo para a porta serial se estabilizar
    time.sleep(2) 
except serial.SerialException as e:
    print(f"Erro ao conectar com o Arduino: {e}")
    arduino = None

# Inicializa o aplicativo Flask
app = Flask(__name__)

# Rota principal que renderiza a página HTML (index.html)
@app.route('/')
def index():
    # Isso assume que você tem um arquivo chamado 'index.html' na pasta 'templates'
    return render_template('index.html')

# Rota que recebe os comandos do HTML e os envia para o Arduino
# Exemplo de URL: /control/1/on ou /control/2/off
@app.route('/control/<led_num>/<action>')
def control(led_num, action):
    command = ''

    # Verifica qual LED e qual ação foi solicitada
    if led_num == '1':
        # 'A' para ligar (on), 'a' para desligar (off)
        command = 'A' if action == 'on' else 'a'
    elif led_num == '2':
        # 'B' para ligar (on), 'b' para desligar (off)
        command = 'B' if action == 'on' else 'b'

    # Se o objeto arduino estiver conectado e um comando for definido
    if arduino and command:
        # Envia o comando para o Arduino (precisa ser codificado para bytes)
        arduino.write(command.encode())
        return f"Comando '{command}' enviado para o LED {led_num}."
    
    # Se o comando for inválido (led_num errado)
    elif arduino:
        return "Comando inválido."
    
    # Se o Arduino não estiver conectado
    else:
        return "Arduino não conectado."

# Bloco principal que executa o servidor web
if __name__ == '__main__':
    # Inicia o servidor Flask. Host 0.0.0.0 permite acesso externo.
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)