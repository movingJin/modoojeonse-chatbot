# Modoojeonse Chatbot

A Python Flask web-socket chatbot service for the **Modoojeonse** platform.

## Installation / Quick Start 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

### Project Structure
```
modoojeonse-frontend/
├── build/
├── dis/
├── src/
├── model/
├── hooks/
├── main.py
└── ...
```

### 1. Download a llm model

Download a [llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M.gguf](https://huggingface.co/Bllossom/llama-3.2-Korean-Bllossom-3B-gguf-Q4_K_M) file on the project ./model directory to running:


### 2. Deploy with Docker

Use Docker Compose to build and run the deployment:

```
$ docker-compose build
$ docker-compose up -d
```
