// ==========================================================
// CÓDIGO ARDUINO (C++) PARA RECEBER COMANDOS SERIAIS
// ==========================================================

// Define os pinos para os LEDs
const int led1Pin = 7; // LED Verde
const int led2Pin = 8; // LED Vermelho

void setup() {
    // Inicia a comunicação serial com a mesma velocidade do Python (9600)
    Serial.begin(9600);

    // Define os pinos dos LEDs como saída
    pinMode(led1Pin, OUTPUT);
    pinMode(led2Pin, OUTPUT);
}

void loop() {
    // Verifica se há algum dado disponível para ser lido na porta serial
    if (Serial.available() > 0) {
        // Lê o caractere recebido
        char command = Serial.read();

        // Executa a ação baseada no comando
        switch (command) {
            case 'A': // Comando para Ligar o LED 1 (Verde)
                digitalWrite(led1Pin, HIGH); // Liga o LED 1
                break;
            case 'a': // Comando para Desligar o LED 1 (Verde)
                digitalWrite(led1Pin, LOW); // Desliga o LED 1
                break;
            case 'B': // Comando para Ligar o LED 2 (Vermelho)
                digitalWrite(led2Pin, HIGH); // Liga o LED 2
                break;
            case 'b': // Comando para Desligar o LED 2 (Vermelho)
                digitalWrite(led2Pin, LOW); // Desliga o LED 2
                break;
        }
    }
}