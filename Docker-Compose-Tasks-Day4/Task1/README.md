
---

```markdown
# 🗳️ Voting App - Microservices Project

This project is a simple microservices-based application built using Docker Compose. It consists of the following services:

- `vote`: A Python Flask web app where users can vote between two options.
- `redis`: A Redis queue that stores the votes temporarily.
- `worker`: A .NET Core service that processes the votes from Redis and stores them in PostgreSQL.
- `db`: A PostgreSQL database that persists the vote counts.
- `result`: A Node.js web app that displays real-time voting results.

---

## 📦 Technologies Used

- **Python + Flask** for the voting frontend
- **Redis** as a message broker
- **.NET Core** for the background worker
- **PostgreSQL** as the database
- **Node.js + Express** for the result dashboard
- **Docker + Docker Compose** for container orchestration

---

## 🧱 Architecture Overview

![Architecture diagram](architecture.excalidraw.png)

---

## 🚀 Getting Started

### 1. Prerequisites

Download [Docker Desktop](https://www.docker.com/products/docker-desktop) for Mac or Windows. [Docker Compose](https://docs.docker.com/compose/) will be automatically installed.  
On Linux, install the latest version of [Docker Compose](https://docs.docker.com/compose/install/).

---

### 2. Run the Application

In the root directory of the project, run:

```bash
docker compose up --build
```

### 3. Access the Applications

| Service   | URL                      | Description           |
|-----------|---------------------------|-----------------------|
| `vote`    | http://localhost:8080     | Voting UI (Python)    |
| `result`  | http://localhost:8081     | Results UI (Node.js)  |

---

## 📌 Notes

- The voting application only accepts **one vote per client browser**.
- This is a simple example of how distributed systems and services interact using **Docker Compose**.
- It demonstrates different service layers (frontend/backend/database/queue) in action using multiple languages.

---

## 🎥 Demo Video

> Below is a demo video showcasing the full functionality of the voting app:

🎬 [Click here to watch the demo](vote-example.webm)

---

## 🙌 Author

**Amir Ebrahem**  
A passionate DevOps Engineer focused on backend systems, DevOps tools, and microservice architecture.

---