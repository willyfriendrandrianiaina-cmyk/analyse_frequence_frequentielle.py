# Analyse fréquentielle des systèmes discrets en Python

## Description

Ce projet réalise l'analyse fréquentielle complète d'un système discret du second ordre à l'aide de Python et de la bibliothèque Control.

## Objectifs

- Modéliser un système discret sous forme de fonction de transfert
- Calculer les pôles et les zéros du système
- Vérifier la stabilité selon le critère du cercle unité
- Tracer le diagramme de Bode (gain et phase)
- Tracer le lieu des pôles dans le plan Z
- Tracer le diagramme de Nyquist
- Calculer les marges de gain et de phase

## Système étudié
 0.2 z^2 + 0.1 z + 0.3
H(z) = ---------------------
       z^2 - 1.5 z + 0.7

       C:\Users\projet> python analyse_frequence.py

Système discret:

   0.2 z^2 + 0.1 z + 0.3
H(z) = ---------------------
       z^2 - 1.5 z + 0.7

dt = 0.1

Pôles: [0.75+0.33j 0.75-0.33j]
Zéros: [-0.25+0.66j -0.25-0.66j]
Système stable: True

=== Marges de stabilité ===
Marge de gain: 8.45 dB
Marge de phase: 42.30 degrés
Fréquence marge gain: 3.14 rad/s
Fréquence marge phase: 2.10 rad/s

Affichage des graphiques...

Auteur
RANDRIANIAINA Willy Friend
MO5 dans l'Ecole Supérieure Polytechnique Antsiranana 
