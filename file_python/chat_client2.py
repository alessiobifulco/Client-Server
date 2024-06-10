import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

# Funzione per ricevere messaggi dal server
def handle_incoming_messages(client_socket, display_area):
    connected = True
    while connected:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if not msg:
                connected = False
            display_area.config(state=tk.NORMAL)
            display_area.insert(tk.END, msg + '\n')
            display_area.config(state=tk.DISABLED)
            display_area.yview(tk.END)
        except Exception as e:
            print(f"Errore nella ricezione del messaggio: {e}")
            connected = False

# Funzione per inviare messaggi al server
def submit_message(client_socket, input_field, display_area, username):
    msg = input_field.get()
    if msg:
        complete_msg = f"{username}: {msg}"
        try:
            client_socket.sendall(complete_msg.encode('utf-8'))
        except Exception as e:
            print(f"Errore nell'invio del messaggio: {e}")
        input_field.delete(0, tk.END)
        display_area.config(state=tk.NORMAL)
        display_area.insert(tk.END, complete_msg + '\n')
        display_area.config(state=tk.DISABLED)
        display_area.yview(tk.END)

# Configurazione della GUI del client
def initialize_client_gui():
    # Finestra principale per chiedere l'username
    root = tk.Tk()
    root.withdraw()  # Nasconde la finestra principale temporaneamente

    username = simpledialog.askstring("Username", "Inserisci il tuo username:", parent=root)
    if not username:
        return  # Esci se l'utente non fornisce un username

    root.deiconify()  # Mostra la finestra principale
    root.title(username)
    root.geometry("450x500")

    # Connessione al server
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('127.0.0.1', 54000))
    except ConnectionRefusedError as e:
        print(f"Errore di connessione: {e}")
        return

    # Configurazione dell'area di testo per visualizzare i messaggi
    display_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="light grey")
    display_area.config(state=tk.DISABLED)
    display_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Configurazione del frame di input per l'invio dei messaggi
    input_frame = tk.Frame(root, bg="light blue")
    input_frame.pack(padx=10, pady=5, fill=tk.X)

    input_field = tk.Entry(input_frame, font=("Arial", 12))
    input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

    send_button = tk.Button(input_frame, text="Invia", font=("Arial", 12), bg="blue", fg="white", command=lambda: submit_message(client_socket, input_field, display_area, username))
    send_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Thread per gestire la ricezione dei messaggi dal server
    thread = threading.Thread(target=handle_incoming_messages, args=(client_socket, display_area))
    thread.start()

    # Avvio della GUI
    root.mainloop()

if __name__ == "__main__":
    initialize_client_gui()
