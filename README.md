## 🤖 - Bot Discord Paul Louis Courier (PLC-Bot)

## 🚀 - Présentation du Projet :
Le **PLC-Bot** est un projet collaboratif mené par les étudiants du **BTS Services Informatiques aux Organisations (SIO)** du **Lycée Paul-Louis Courier**.

Il a été conçu pour le serveur Discord du BTS afin d'**automatiser les tâches d'administration** et de relayer les dernières informations de Pronote directement sur le Discord (modifications d'emploi du temps, menu de la cantine, etc.).

***

## ✨ - Fonctionnalités Actuelles (Déployées) :

| Catégorie | Commande / Fonction | Description Détaillée |
| :---: | :--- | :--- |
| **Base** | `/help`, `/ping` | Commandes d'aide et de vérification de l'état du Bot. **Messages de bienvenue** automatiques aux nouveaux membres. |

***

## 🚧 - Fonctionnalités en Cours de Développement :

| Catégorie | Commande / Fonction | Description Détaillée |
| :---: | :--- | :--- |
| **Intelligence Artificielle** | `/ask` | Permettre de **poser une question à une IA** directement via le bot. |

***

## 💡 - Fonctionnalités Futures (Projets à venir) :

* **Intégration Pronote/Éléa** : Notification des **notes** ou des **devoirs** récents (nécessite une connexion API sécurisée et validée).
* **Administration** : Commandes avancées pour la **modération** et l'**organisation** du serveur.

## 📦 - Docker compose :

```yml
---
services:
  bot-plc:
    image: louismedo/plc-bot:0.1
    container_name: bot-plc
    restart: unless-stopped
    environment:
      - DISCORD_BOT_TOKEN=${DISCORD_BOT_TOKEN}
      - HF_TOKEN=${HF_TOKEN}
```


***

## 🤝 - Contribution :

Ce projet est la propriété et l'initiative des étudiants du BTS SIO du Lycée Paul-Louis Courier. Nous **encourageons la collaboration** et les suggestions.

Pour toute question, contribution ou opportunité de partenariat, veuillez contacter l'un des **responsables de projet** ou le **coordinateur de la filière**.

*💖 Développé avec passion par la promotion **2025** du BTS SIO.*
