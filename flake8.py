#!/usr/bin/env python

import sys
import subprocess

# Exécute la commande"flake8" pour vérifier la qualité du code
result = subprocess.run(["flake8"])

# Si la commande retourne un code d'erreur, affiche un message d'erreur
# et annule le commit
if result.returncode != 0:
    print("Erreur de qualité du code détectée")
    print(result)
    sys.exit(1)

# Si la commande s'exécute avec succès, affiche un message de succès
# et continue avec le commit
print("Code de qualité vérifié avec succès.")
sys.exit(0)
