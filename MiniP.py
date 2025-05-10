import cv2
import mediapipe as mp

# Inicializar MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Iniciar captura de vídeo
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip para efecto espejo y conversión de color
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Procesar imagen
    results = hands.process(rgb)

    finger_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Lista de dedos: pulgar, índice, medio, anular, meñique
            finger_tips = [4, 8, 12, 16, 20]
            finger_folded = []

            # Coordenadas del punto base de cada dedo
            for tip in finger_tips:
                if tip != 4:  # Pulgar tiene otra lógica
                    if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
                        finger_count += 1
                else:
                    # Pulgar: comparar eje x
                    if hand_landmarks.landmark[tip].x > hand_landmarks.landmark[tip - 1].x:
                        finger_count += 1

            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Mostrar número de dedos
    cv2.putText(frame, f"Dedos: {finger_count}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Contador de Dedos", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Pulsa Esc para salir
        break

cap.release()
cv2.destroyAllWindows()
