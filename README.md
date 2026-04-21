# Analyse fréquentielle des systèmes discrets en Python

## Description

Ce projet réalise l'analyse fréquentielle complète d'un système discret du second ordre à l'aide de Python et de la bibliothèque Control. Il permet de :

- Calculer les pôles et les zéros du système
- Vérifier la stabilité selon le critère du cercle unité
- Tracer le diagramme de Bode (gain et phase)
- Tracer le lieu des pôles dans le plan Z
- Tracer le diagramme de Nyquist
- Calculer les marges de gain et de phase

## Système étudié
H(z) = (0.2z² + 0.1z + 0.3) / (z² - 1.5z + 0.7) , Ts = 0.1s

## Installation
```bash
pip install numpy matplotlib scipy control
