import os
# Fichier de variables globales

# Version du bot
VERSION = "0.3"

# Développeurs du bot
DEVELOPPEURS = ("Ewen GADONNAUD", "Louis MEDO", "Amine KADA")

# ID du salon de veille
VEILLE_CHANNEL_ID = os.getenv("VEILLE_CHANNEL_ID")
print(f"VEILLE_CHANNEL_ID chargé : {VEILLE_CHANNEL_ID}")
