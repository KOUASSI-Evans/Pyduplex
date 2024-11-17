import cv2
import numpy as np
import pyaudio
import socket
import struct
import tkinter as tk
from PIL import Image, ImageTk
import threading
import logging
import json  # Importer la bibliothèque json
import time
from collections import deque
import queue

# Configuration du logging pour le débogage
logging.basicConfig(level=logging.DEBUG)

chat_message_queue = queue.Queue()
audio_buffer = deque(maxlen=10)  # Tampon circulaire avec une taille fixe
p = pyaudio.PyAudio()

# Dimensions de l'affichage vidéo
VIDEO_WIDTH = 400
VIDEO_HEIGHT = 375
FRAME_SIZE = VIDEO_WIDTH * VIDEO_HEIGHT * 3

# Paramètres pour la capture audio
CHUNK = 256
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

# Adresse IP de l'autre Raspberry Pi
REMOTE_IP = '10.42.0.147'
SECONDARY_IP = '10.42.0.1'  # Adresse IP du Raspberry Pi secondaire

# Ports pour la communication
VIDEO_PORT = 5005
AUDIO_PORT = 5006
COMMAND_PORT = 5007  # Port pour les commandes


# Initialiser la connexion vidéo
video_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
video_socket.bind(('', VIDEO_PORT))

# Initialiser la connexion audio
audio_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
audio_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024*4)
audio_socket.bind(('', AUDIO_PORT))

# Initialiser la connexion de commande
command_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
command_socket.bind(('', COMMAND_PORT))

# Variables pour les threads
stop_video_event = threading.Event()
stop_secondary_video_event = threading.Event()
stop_audio_event = threading.Event()
video_buffer = {}
current_frame_id = 0
expected_frame_size = FRAME_SIZE

# Variable pour le volume audio
volume = 0.5  # Volume par défaut à 50%

# Fonction pour afficher une frame vidéo
def display_video(frame):
    global video_label
    image = Image.fromarray(frame)
    image_tk = ImageTk.PhotoImage(image)
    video_label.config(image=image_tk)
    video_label.image = image_tk
# Fonction pour recevoir la vidéo du Raspberry Pi secondaire
def receive_video_from_secondary():
    global video_socket, video_buffer, current_frame_id, expected_frame_size
    while not stop_secondary_video_event.is_set():
        try:
            segment, addr = video_socket.recvfrom(65507)
            frame_id = struct.unpack('I', segment[:4])[0]
            segment_data = segment[4:]

            if frame_id not in video_buffer:
                video_buffer[frame_id] = bytearray()
            video_buffer[frame_id].extend(segment_data)

            if len(video_buffer[frame_id]) >= expected_frame_size:
                frame_data = video_buffer.pop(frame_id)
                frame = np.frombuffer(frame_data, dtype=np.uint8).reshape((VIDEO_HEIGHT, VIDEO_WIDTH, 3))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                display_video(frame)
                logging.debug(f"Frame {frame_id} from secondary displayed.")
        except Exception as e:
            logging.error(f"Erreur de réception vidéo secondaire: {e}")
    reset_video_display()





# Fonction pour envoyer la vidéo à l'autre Raspberry Pi
def send_video():
    global video_socket
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    frame_id = 0
    while not stop_video_event.is_set():
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (VIDEO_WIDTH, VIDEO_HEIGHT))
            data = frame.tobytes()
            for i in range(0, len(data), 60000):  # Split data into chunks
                segment = struct.pack('I', frame_id) + data[i:i+60000]
                video_socket.sendto(segment, (REMOTE_IP, VIDEO_PORT))
            frame_id += 1
    cap.release()
    
# Fonction pour recevoir l'audio de l'autre Raspberry Pi
def receive_audio():
    global audio_socket, volume, audio_buffer
    p = pyaudio.PyAudio()
    audio_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True)
    while not stop_audio_event.is_set():
        try:
            data, addr = audio_socket.recvfrom(CHUNK*10)
            if not data:
                logging.warning("Aucune donnée reçue")
                continue
            audio_data = np.frombuffer(data, dtype=np.int16)
            audio_data = (audio_data * volume).astype(np.int16)
            audio_buffer.append(audio_data.tobytes())
            logging.debug(f"Données audio reçues: {len(data)} octets")
            if len(audio_buffer) > 0:
                audio_stream.write(audio_buffer.popleft())
        except Exception as e:
            logging.error(f"Erreur de réception audio: {e}")
    audio_stream.stop_stream()
    audio_stream.close()
    p.terminate()

# Fonction pour envoyer l'audio à l'autre Raspberry Pi
def send_audio():
    global audio_socket
    p = pyaudio.PyAudio()
    input_device_index = 2  # Choisissez dynamiquement l'index du périphérique
    try:
        audio_stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, input_device_index=input_device_index, frames_per_buffer=256)
        while not stop_audio_event.is_set():
            try:
                data = audio_stream.read(CHUNK, exception_on_overflow=False)
                audio_socket.sendto(data, (REMOTE_IP, AUDIO_PORT))
            except IOError as e:
                logging.error(f"Erreur de lecture audio: {e}")
    finally:
        audio_stream.stop_stream()
        audio_stream.close()
        p.terminate()

def stop_audio():
    stop_audio_event.set()

# Fonction pour ajuster le volume audio
def adjust_volume(val):
    global volume
    volume = float(val) / 100



# Fonction pour arrêter la capture vidéo
def stop_video():
    logging.debug("Arrêt de la video.")
    stop_video_event.set()
    send_command({'action': 'stop_video'})
    
            
def stop_secondary_video():
    stop_secondary_video_event.set()
    send_command({'action': 'stop_video2'})

# Fonction pour envoyer une commande au Raspberry Pi secondaire
def send_command(command):
    message = json.dumps(command).encode('utf-8')
    print('sending ' + str(command))
    command_socket.sendto(message, (REMOTE_IP, COMMAND_PORT))

# Fonction pour démarrer la capture et l'envoi vidéo
def start_video():
    stop_video_event.clear()
    threading.Thread(target=send_video, daemon=True).start()
    send_command({'action': 'start_video'})

# Fonction pour réinitialiser l'affichage vidéo à un état neutre
def reset_video_display():
    black_frame = np.zeros((VIDEO_HEIGHT, VIDEO_WIDTH, 3), dtype=np.uint8)
    display_video(black_frame)
    
# Fonction pour demander au Raspberry Pi secondaire de démarrer l'envoi vidéo
def start_video2():
    stop_secondary_video_event.clear()
    threading.Thread(target=receive_video_from_secondary, daemon=True).start()
    send_command({'action': 'start_video2'})
    
    
# Fonction pour démarrer la capture et l'envoi audio
def start_audio():
    threading.Thread(target=receive_audio, daemon=True).start()
    threading.Thread(target=send_audio, daemon=True).start()
    send_command({'action': 'start_audio'})

def handle_command(command):
    print('handle lancé')
    action = command.get('action')
    if action == 'alert':
        print("c'est appuyé")
        show_alert()
    elif action == 'chat':
        receive_chat_message(command)
    
def receive_command():
    print('reçu')
    while True:
        message, addr = command_socket.recvfrom(1024)
        command = json.loads(message.decode('utf-8'))
        handle_command(command)

def show_alert():
    alert_label = tk.Label(root, text="URGENCE", fg='red', bg='black', font=('Helvetica', 290 , 'bold'))
    alert_label.place(relx = 0.5, rely = 0.5, anchor = 'center')

def close_interface():
    root.destroy()

def on_closing():
    stop_video_event.set()
    stop_audio_event.set()
    root.destroy()

def scroll_to_bottom():
    chat_display.see(tk.END)

# Fonction pour envoyer un message de chat
def send_chat_message(event=None):
    message = chat_entry.get()
    if message:
        chat_display.insert(tk.END, "Vous: " + message + "\n")
        chat_entry.delete(0, tk.END)
        send_command({'action': 'chat', 'message': message})
        scroll_to_bottom()
        # Ici vous pouvez ajouter le code pour envoyer le message de chat à l'autre Raspberry Pi

def receive_chat_message(command):
    message = command.get('message', '')
    if message:
        chat_display.insert(tk.END, "Client: " + message + "\n")
        scroll_to_bottom()
        


# Création de l'interface utilisateur Tkinter
root = tk.Tk()
root.title("Interface de capture vidéo et audio")
root.config(bg='#C5DFFF')

# Configurer la fenêtre pour le plein écran
root.attributes('-fullscreen', True)

# Créer un cadre pour le rendu de la caméra au centre
camera_frame = tk.Frame(root, bg='#2E2E2E')
camera_frame.place(relx=0.5, rely=0.5, anchor='center', width=VIDEO_WIDTH, height=VIDEO_HEIGHT)
    
# Créer une étiquette pour afficher la vidéo
video_label = tk.Label(camera_frame, bg='black', borderwidth=0, highlightthickness=0)
video_label.pack(expand=True, fill='both')

# Créer un cadre en bas pour les boutons 
control_frame = tk.Frame(root, bg='#2E2E2E')
control_frame.pack(side=tk.BOTTOM, fill='x')

# Créer un cadre intermédiaire pour centrer les boutons de contrôle
button_frame = tk.Frame(control_frame, bg='#2E2E2E')
button_frame.pack(expand=True)

def toggle_my_camera():
    if start_video_button.cget('text') == "Activer ma caméra":
        start_video()
        start_video_button.config(text="Arrêter ma caméra", bg='green')
    else:
        stop_video()
        start_video_button.config(text="Activer ma caméra", bg='#FF0000')

def toggle_secondary_camera():
    if request_secondary_video_button.cget('text') == "Activer la caméra du deuxième Raspberry":
        start_video2()
        request_secondary_video_button.config(text="Arrêter la caméra du deuxième Raspberry", bg='green')
    else:
        stop_secondary_video()
        request_secondary_video_button.config(text="Activer la caméra du deuxième Raspberry", bg='#FF0000')

def toggle_audio():
    if start_audio_button.cget('text') == "Démarrer audio":
        start_audio()
        start_audio_button.config(text="Arrêt de l'audio", bg='green')
    else:
        stop_audio()
        start_audio_button.config(text="Démarrer audio", bg='#FF0000')
        
    
# Remplacer les anciens boutons pour ma caméra
start_video_button = tk.Button(button_frame, text="Activer ma caméra", command=toggle_my_camera, bg='#FF0000', fg='white', font=('Helvetica', 12, 'bold'))
start_video_button.pack(side=tk.LEFT, padx=5, pady=5)

# Remplacer les anciens boutons pour la caméra secondaire
request_secondary_video_button = tk.Button(button_frame, text="Activer la caméra du deuxième Raspberry", command=toggle_secondary_camera, bg='#FF0000', fg='white', font=('Helvetica', 12, 'bold'))
request_secondary_video_button.pack(side=tk.LEFT, padx=5, pady=5)

start_audio_button = tk.Button(button_frame, text="Démarrer audio", command=toggle_audio, bg='#FF0000', fg='white', font=('Helvetica', 12, 'bold'))
start_audio_button.pack(side=tk.LEFT, padx=5, pady=5)

# Créer un cadre à droite pour le contrôle du volume
volume_frame = tk.Frame(root, bg='#2E2E2E')
volume_frame.place(relx=0.98, rely=0.5, anchor='e')

volume_label = tk.Label(volume_frame, text="Volume", bg='#2E2E2E', fg='white', font=('Helvetica', 12, 'bold'))
volume_label.pack(side='top', fill='x', pady=10)

# Ajouter un slider pour le contrôle du volume dans le cadre de volume
volume_slider = tk.Scale(volume_frame, from_=100, to=0, orient=tk.VERTICAL, command=adjust_volume, bg='#404040', fg='white', font=('Helvetica', 12, 'bold'))
volume_slider.set(50)  # Volume par défaut à 50%
volume_slider.pack(side='top', pady=(10, 10), expand=True)

# Ajouter le bouton de fermeture en haut à droite
close_button_top_right = tk.Button(root, text="❌", command=close_interface, bg='#FF0000', fg='white', font=('Helvetica', 12, 'bold'))
close_button_top_right.place(relx=1.0, rely=0, anchor='ne')

# Ajouter un cadre pour le chat
chat_frame = tk.Frame(root, bg='#2E2E2E')
chat_frame.pack(side=tk.LEFT, fill='x', padx=100)


# Ajouter une zone de texte pour afficher les messages de chat
chat_display = tk.Text(chat_frame, height=35, width=50, bg='#404040', fg='white', font=('Helvetica', 12))
chat_display.pack(side='top', fill='both', expand=True)


# Ajouter un champ de saisie pour écrire des messages de chat
chat_entry = tk.Entry(chat_frame, width=50, bg='#C5DFFF', fg='black', font=('Helvetica', 12))
chat_entry.pack(side='bottom', expand=True)

# Associer la touche "Entrée" à l'envoi du message
chat_entry.bind("<Return>", send_chat_message)

chat_entry.focus_set()  

root.protocol("WM_DELETE_WINDOW", on_closing)

threading.Thread(target=receive_command, daemon = True).start()

# Lancer la boucle principale de la fenêtre
root.mainloop()




