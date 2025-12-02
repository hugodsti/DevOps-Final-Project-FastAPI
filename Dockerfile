# Importer  python image slim
FROM python
#Définir le répertoire de travail dans le conteneur
WORKDIR /app



# Étape 4 : Copier les dépendances
COPY requirements.txt .


# Installer les dépendances restantes du fichier requirements.txt
RUN pip install -r requirements.txt

# Copier le code de l'application
COPY devopsproject /app/devopsproject

ENV DEVOPS_APP_HOST=0.0.0.0

EXPOSE 5000

CMD ["python", "./devopsproject/app.py"]