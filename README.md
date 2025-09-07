# 🎮 Quiz Game

A **socket-based multiplayer quiz game** built with **Python 3** and **SSL** for secure communication.  
Up to **4 players** can join and compete in a fast-paced buzzer-style quiz.  

---

## 📖 Project Overview
- The **host (server)** maintains a large set of questions and answers.
- A **random question** is sent to all players.
- Players hit the **buzzer** by pressing the `Enter` key.  
  - The first to buzz within **10 seconds** gets a chance to answer.
- The chosen player has **10 seconds** to respond.  
  - ✅ Correct answer → +1 point  
  - ❌ Wrong/invalid/timeout → -0.5 points
- The game ends when any player scores **5 or more points**, and that player is declared the **winner**.

---

## ✨ Features
- 👥 Supports **up to 4 players**.
- 📝 Custom player names.
- 🎲 **Randomized questions** – no repetition in a session.
- 🔀 **Shuffled options** – choices are never in the same order.
- 📊 Real-time display of scores and buzzer status after each question.
- 🔒 **SSL/TLS secured sockets** for encrypted communication.

---

## 🔒 SSL Setup
The game uses **SSL certificates** for secure communication.

### Generate SSL Certificate & Key (using OpenSSL)
```bash
openssl req -new -x509 -days 365 -nodes -out server.crt -keyout server.key
```

##Instructions to run the code
```
python3 ippserver.py <IP_address> <Port_Number>
```
```
python3 ippclient.py <IP_address> <Port_Number>
```
Change the ip address in the ippserver.py and ipp.py as well.





