import discord
import os
import asyncio
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

# NOUVEL IMPORT : La bibliothèque officielle Hugging Face
from huggingface_hub import AsyncInferenceClient
from huggingface_hub.utils import HfHubHTTPError

# --- 1. Configuration et Chargement ---

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
HF_TOKEN = os.getenv("HF_TOKEN")

# On définit le modèle qu'on veut utiliser
MODEL_ID = "meta-llama/Meta-Llama-3-8B-Instruct"

# --- 2. Initialisation du Bot et du Client IA ---

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# On initialise le client IA une seule fois
hf_client = AsyncInferenceClient(token=HF_TOKEN)

# --- 3. Événement de Démarrage ---


@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user.name}")

    # On passe à une synchronisation globale pour la production.
    # Les commandes seront disponibles sur tous les serveurs.
    # Note : La mise à jour peut prendre jusqu'à une heure.
    try:
        synced = await bot.tree.sync()
        print(f"Synchronisé {len(synced)} commande(s) globale(s)")
    except Exception as e:
        print(f"Erreur de synchronisation globale : {e}")


# --- 4. Les Commandes ---


@bot.command()
async def bonjour(ctx):
    response = "Bonjour, je suis Paul Louis Courier !"
    await ctx.send(response)


# Commande /ask réécrite avec la bibliothèque officielle
@bot.tree.command(name="ask", description="Pose une question à l'IA (Llama 3)")
@app_commands.describe(question="La question que tu veux poser")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.defer()

    # On définit une personnalité plus précise et professionnelle.
    messages = [
        {
            "role": "system",
            "content": "Tu incarnes Paul-Louis Courier. Tu es un expert érudit et un écrivain précis. Tes réponses sont claires, concises, bien structurées et rédigées dans un français soutenu mais accessible. Tu vas droit au but de manière professionnelle et efficace.",
        },
        {"role": "user", "content": question},
    ]

    try:
        print(
            f"--- Nouvelle requête /ask ---\nModèle utilisé : {MODEL_ID}\nQuestion : {question}"
        )

        # On appelle l'API via la méthode chat_completion
        response = await h_client.chat_completion(
            model=MODEL_ID,
            messages=messages,
            max_tokens=450,  # On réduit un peu par sécurité
            stream=False,
        )

        # On extrait la réponse du bot
        reponse_ia = response.choices[0].message.content.strip()

        # On s'assure que la réponse ne dépasse pas la limite de Discord
        message_header = (
            f"**Ta question :**\n> {question}\n\n**Réponse de Paul-Louis Courier :**\n"
        )
        # On calcule la longueur maximale pour la réponse de l'IA
        max_longueur_reponse = (
            2000 - len(message_header) - 10
        )  # Marge de sécurité de 10 caractères

        # Si la réponse est trop longue, on la tronque proprement
        if len(reponse_ia) > max_longueur_reponse:
            reponse_ia = reponse_ia[:max_longueur_reponse] + "..."

        # On envoie le message final, qui est maintenant garanti d'être sous la limite
        await interaction.followup.send(message_header + reponse_ia)

    except HfHubHTTPError as e:
        # Erreur gérée par la bibliothèque (token invalide, modèle introuvable...)
        print(f"Erreur HTTP de l'API Hugging Face : {e}")
        await interaction.followup.send(
            f":warning: Une erreur est survenue avec l'API de Hugging Face.\n"
            f"Détails : `{e.server_message}`"
        )
    except Exception as e:
        # Autre erreur inattendue
        print(f"Erreur inattendue : {e}")
        await interaction.followup.send(
            ":x: Une erreur inattendue est survenue. Vérifie la console pour plus de détails."
        )


# --- 5. Lancement du Bot ---

if __name__ == "__main__":
    if not all([DISCORD_TOKEN, HF_TOKEN]):
        print(
            "--- ERREUR --- : 'DISCORD_BOT_TOKEN' ou 'HF_TOKEN' est manquant dans le .env"
        )
    else:
        bot.run(DISCORD_TOKEN)
