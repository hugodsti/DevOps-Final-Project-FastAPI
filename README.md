DevOps Project — User API

Ce projet est une application web/API simple, capable d'ajouter des utilsateurs et les stocker dans une base de donnée, leurs emails, et leurs mots de passes. Il y a egalement la possibilté de modifier les données des utlisateurs. Enfin, il est egalement possibe de suprimer les utilsateurs.
Elle inclut le développement, l'IAC, l'image Docker, l’intégration continue, et l'orchestration des contenrus garce a kubernites.


1. Travaux Réalisés


1)  Application

Développement d’une API utilisateur simple(ajouter/supprimer/modifier)
Creation d'une base de donnée MariaDB
Tests unitaires et fonctionnels (tester les conditions)

2) CI/CD

Pipeline GitHub Actions :

Tests pour proteger l'integrite du code de la branche main 

3) Oj

4) Conteneurisation

Image docker :

- elle pemet que tout le monde puisse lancer l'application sur sa machine 

- ![alt text](image.png)
- le premier docker est celui utilser pour faire touner l'application localement 
- le deuxieme conteneur contient le dockerFile (les commentaires sont dedans)

Les commandes utiles pour monter le dockerFile:


- docker build -t devopsapp . (construit une image Docker à partir du Dockerfile)
- docker run --rm --env DEVOPS_DB_HOST=host.docker.internal -p 5000:5000 devopsapp (lance un conteneur basé sur l’image devopsapp, en lui passant une variable d’environnement, en exposant le port 5000, puis supprime automatiquement le conteneur lorsqu’il s’arrête)
- docker login (se connecter a Docker Hub)
- docker build -t hmorais1001/devopsapp:latest . (construit une image Docker à partir du dossier courant et la nomme en utilisant le dépôt Docker Hub)
- docker push hmorais1001/devopsapp:latest ( publie l'image Docker vers le depot)
![alt text](image-1.png)

5) Rachid


Points Bonus :

- developpment de l'application en python 
- Base de donnes utilise : MariaDb
- Docker Hub

2 Captures d’Écran

Les captures sont disponibles dans le dossier :

Elles incluent notamment :

L’API en fonctionnement

Docker build / run

Docker Hub

Kubernetes Dashboard (oj rajoute ca stv )

GitHub Actions (CI/CD pipeline)
