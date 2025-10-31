# Choix de l'image python
FROM python:3.13.7-slim

# Répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers de l'application
COPY . .

# Commande pour lancer l'application
CMD ["python", "-u", "main.py"]