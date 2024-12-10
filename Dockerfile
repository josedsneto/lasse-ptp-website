# Use uma imagem base oficial do Python
FROM python:3.11-slim

# Defina variáveis de ambiente para evitar problemas com buffers e logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Defina o diretório de trabalho no container
WORKDIR /app

# Instale dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copie o arquivo de requisitos e instale as dependências
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY . .

# Exponha a porta que o Streamlit usará
EXPOSE 8501

# Comando para rodar a aplicação Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
