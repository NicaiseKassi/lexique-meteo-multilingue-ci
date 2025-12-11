#!/bin/bash

# Script de déploiement Git pour le Lexique Météorologique Multilingue
# Usage: ./deploy-git.sh "Votre message de commit"

# Couleurs pour les messages
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Déploiement Git ===${NC}"

# Vérifier si un message de commit est fourni
if [ -z "$1" ]; then
    echo -e "${RED}❌ Erreur: Veuillez fournir un message de commit${NC}"
    echo "Usage: ./deploy-git.sh \"Votre message de commit\""
    exit 1
fi

MESSAGE="$1"

# Afficher le statut actuel
echo -e "\n${BLUE}📊 Statut Git:${NC}"
git status --short

# Ajouter tous les fichiers modifiés
echo -e "\n${BLUE}📦 Ajout des fichiers...${NC}"
git add .

# Vérifier s'il y a des changements à commiter
if git diff --staged --quiet; then
    echo -e "${RED}⚠️  Aucun changement à commiter${NC}"
    exit 0
fi

# Afficher les fichiers qui seront commités
echo -e "\n${BLUE}📝 Fichiers à commiter:${NC}"
git diff --staged --name-only

# Créer le commit
echo -e "\n${BLUE}💾 Création du commit...${NC}"
git commit -m "$MESSAGE"

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Erreur lors du commit${NC}"
    exit 1
fi

# Pousser vers GitHub
echo -e "\n${BLUE}🚀 Push vers GitHub...${NC}"
git push origin main

if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}✅ Déploiement réussi !${NC}"
    echo -e "${GREEN}🌐 https://github.com/NicaiseKassi/lexique-meteo-multilingue-ci${NC}"
else
    echo -e "${RED}❌ Erreur lors du push${NC}"
    exit 1
fi
