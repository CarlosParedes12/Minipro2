const int leds[] = {2, 3, 4, 5, 6};  // Pines conectados a los LEDs
int num_leds = sizeof(leds) / sizeof(leds[0]);

void setup() {
  for (int i = 0; i < num_leds; i++) {
    pinMode(leds[i], OUTPUT);
  }
  Serial.begin(9600);  // Comunicación con Python
}

void loop() {
  if (Serial.available() > 0) {
    char dato = Serial.read();  // Leer el dato enviado
    int dedos = dato - '0';     // Convertir de char a int

    // Encender LEDs según número de dedos
    for (int i = 0; i < num_leds; i++) {
      if (i < dedos) {
        digitalWrite(leds[i], HIGH);
      } else {
        digitalWrite(leds[i], LOW);
      }
    }
  }
}
