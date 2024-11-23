# UE19 Lab 05: API Jokes App

## Description

Cette application Python interroge l'API publique JokesAPI pour obtenir une blague et l'afficher à l'utilisateur. Le programme utilise la bibliothèque `requests` pour envoyer des requêtes HTTP à l'API.

## Fonctionnalités

- Interroge l'API JokesAPI pour obtenir une blague.
- Affiche une blague aléatoire dans le terminal.

## Prérequis

Avant de commencer, assurez-vous d'avoir :  
- **Python 3.7 ou une version supérieure**  
- La bibliothèque Python `requests` (si elle n'est pas déjà installée, voir ci-dessous).

## Installation

### 1. Cloner le dépôt

Clonez ce repository en exécutant la commande suivante dans votre terminal :

```bash
git clone https://github.com/Aniskhal25/ue19-lab-05.git
```

### 2. Accédez au répertoire cloné

Une fois le dépôt cloné, accédez au dossier du projet :

```bash
cd ue19-lab-05
```

### 3. Installez la dépendance requise

Installez la bibliothèque `requests` nécessaire au bon fonctionnement de l'application :

```bash
pip install requests
```

## Exécution du projet via Docker

Si vous préférez exécuter ce projet dans un conteneur Docker, voici les étapes :

1. **Clonez le dépôt :**

   ```bash
   git clone https://github.com/Aniskhal25/ue19-lab-05.git
   cd ue19-lab-05
   ```

2. **Construisez l'image Docker :**

   Pour construire l'image Docker, exécutez la commande suivante :

   ```bash
   docker build -t api-jokes-app .
   ```

3. **Exécutez le conteneur Docker :**

   Une fois l'image construite, lancez le conteneur avec la commande suivante :

   ```bash
   docker run --rm api-jokes-app
   ```

Cela démarrera l'application dans un conteneur Docker et affichera une blague aléatoire dans le terminal.

## Utilisation

Pour exécuter l'application et afficher une blague aléatoire, lancez la commande suivante si vous n'utilisez pas Docker :

```bash
python app.py
```

Chaque exécution de la commande affichera une nouvelle blague tirée de l'API publique JokesAPI.

## À propos

Ce projet a été développé dans le cadre du laboratoire 5 de l' **UE19** et a pour but d'illustrer l'utilisation d'une API publique en Python.

