Miniproyecto 2 – Visión por Computador: Contador de Dedos con Python y Arduino

Este proyecto implementa un sistema de visión artificial que cuenta los dedos levantados mediante una webcam y envía el número a un Arduino, que responde encendiendo LEDs como visualización.

---

Objetivo

- Detectar entre 0 y 5 dedos mediante MediaPipe.
- Enviar el número detectado al Arduino vía puerto serial.
- Visualizar el conteo mediante LEDs (uno por dedo).

---

Tecnologías utilizadas

### Software:
- Python 3.10
- OpenCV
- MediaPipe
- PySerial
- Arduino IDE

### Hardware:
- Arduino UNO
- 5 LEDs + resistencias (220Ω)
- Protoboard + cables jumper
- Webcam

---

## ⚙️ Estructura del proyecto

