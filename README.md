# Chat Client-Server in Python

Progetto per il corso di Programmazione di Reti che implementa un sistema di chat multi-client basato su un'architettura client-server.

---

## Obiettivo del Progetto

L'obiettivo è sviluppare un'applicazione di chat funzionante che permetta a più utenti di comunicare simultaneamente all'interno di una stanza di discussione condivisa. Il sistema è composto da un server centralizzato in grado di gestire connessioni multiple e da client dotati di interfaccia grafica per l'interazione.

## Architettura del Sistema

L'applicazione si basa su una classica architettura **client-server**:

* **Server:** È il componente centrale che gestisce la logica della chat. Il suo compito è accettare le connessioni dai client, ricevere i messaggi e inoltrarli a tutti gli altri partecipanti connessi, agendo come un hub di comunicazione.
* **Client:** È l'applicazione con cui l'utente interagisce. Permette di connettersi al server, inviare messaggi alla chatroom e visualizzare in tempo reale i messaggi provenienti dagli altri utenti.

Per gestire la concorrenza e la comunicazione asincrona, il sistema fa largo uso del **multithreading**.

## Funzionamento

### Server
Il server, una volta avviato, si mette in ascolto di nuove connessioni in entrata. Per ogni client che si connette, il server crea un **thread dedicato** per gestire la comunicazione con quel client specifico. Questo approccio permette di servire più client contemporaneamente senza che uno blocchi gli altri. Quando un messaggio viene ricevuto da un client, il server lo ritrasmette a tutti gli altri client presenti nella sua lista di connessioni attive.

### Client
Il client, dotato di un'interfaccia grafica, stabilisce una connessione con il server. La comunicazione è gestita da due thread principali:
1.  Un **thread principale** per l'interfaccia grafica e l'invio dei messaggi scritti dall'utente.
2.  Un **thread secondario** che si mette costantemente in ascolto di messaggi in arrivo dal server, permettendo di ricevere e visualizzare i messaggi degli altri utenti in modo asincrono, senza bloccare l'interfaccia.

## Tecnologie Utilizzate

* **Linguaggio:** Python 3.x
* **Comunicazione di Rete:** Modulo `socket` (Socket Programming) per la gestione della comunicazione a basso livello su protocollo TCP.
* **Concorrenza:** Modulo `threading` per la gestione di connessioni e processi multipli sia sul server che sul client.
* **Interfaccia Grafica (GUI):** Libreria `Tkinter`, inclusa nella distribuzione standard di Python, per la creazione dell'interfaccia utente del client.

## Contatti
* Alessio Bifulco: `alessio.bifulco@studio.unibo.it`
