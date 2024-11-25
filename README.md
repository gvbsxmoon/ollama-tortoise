# Story Generation API with Tortoise TTS and Ollama

This project provides an API to generate children's stories based on a character and environment, synthesize the story into speech, and return the resulting audio.

---

## Prerequisites

1. **Python 3.11**  
Ensure Python 3.11 is installed on your system.

2. **Virtual Environment Setup**  
Create and activate a virtual environment for the project:
  ```bash
  python3.11 -m venv .venv
  source .venv/bin/activate
  ```

## Installation

1. **Tortoise TTS Model**  
  ```bash
  pip install --upgrade pip
  pip install numba inflect psutil
  pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cpu
  pip install transformers
  pip install tortoise-tts
  ```

2. **Ollama**  
Download and install Ollama from [here](https://ollama.com/download/mac).
To run and pull models, use the following commands:

  ```bash
  ollama serve
  ollama pull <model_name>
  ```

3. **FastApi**  
  ```bash
  pip install fastapi uvicorn requests
  ```

## Usage

1. **Run the API**  
  ```bash
  uvicorn index:app --reload
  ```
