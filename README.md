# FlareAssistant

![Discord](https://discord.com/api/guilds/513855202797813791/embed.png)

### Features
- Conversational support and Q&A for general or server-specific queries
- Can chat with multiple users at once
- Music player
- Imagine (text-to-image)

### Requirements
The bot uses a Python Flask backend. Additional AI model weights are required for the chat feature.

First, clone or download the repository. Then, install the packages in a virtualenv:
```bash
pip install requirements.txt
```

For chatting, the recommended LLM to use is OpenHermes-2.5-Mistral-7B. The project uses the 6-bit quantized GGUF, but depending on the GPU other levels of quantization might be more suitable. The full list of options and download links is [here](https://huggingface.co/TheBloke/OpenHermes-2.5-Mistral-7B-GGUF)

Once downloaded, place the .gguf file in the models folder.

### Usage
Activate the virtualenv and run app.py
```bash
py app.py
```
