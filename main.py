import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# ========== DÉFINITION DU SYSTÈME ==========
# Système discret: H(z) = (0.2z² + 0.1z + 0.3) / (z² - 1.5z + 0.7)
num = [0.2, 0.1, 0.3]      # Numérateur
den = [1, -1.5, 0.7]       # Dénominateur
Ts = 0.1                    # Période d'échantillonnage

sys = ctrl.TransferFunction(num, den, Ts)
print("Système discret:")
print(sys)

# ========== PÔLES ET STABILITÉ ==========
poles = ctrl.pole(sys)
zeros = ctrl.zero(sys)
stable = all(abs(p) < 1 for p in poles)

print(f"\nPôles: {poles}")
print(f"Zéros: {zeros}")
print(f"Système stable: {stable}")

# ========== DIAGRAMME DE BODE ==========
plt.figure(figsize=(12, 5))

# Gain
plt.subplot(1, 2, 1)
mag, phase, omega = ctrl.bode(sys, plot=False)
plt.semilogx(omega, 20*np.log10(mag))
plt.xlabel('Fréquence (rad/s)')
plt.ylabel('Gain (dB)')
plt.title('Diagramme de Bode - Gain')
plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='r', linestyle='--', alpha=0.5)

# Phase
plt.subplot(1, 2, 2)
plt.semilogx(omega, phase * 180/np.pi)
plt.xlabel('Fréquence (rad/s)')
plt.ylabel('Phase (degrés)')
plt.title('Diagramme de Bode - Phase')
plt.grid(True, alpha=0.3)
plt.axhline(y=-180, color='r', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# ========== LIEU DES PÔLES (PLAN Z) ==========
plt.figure(figsize=(8, 8))

# Cercle unitaire
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta), 'k--', alpha=0.5, label='Cercle unitaire')

# Pôles (x) et zéros (o)
plt.plot(np.real(zeros), np.imag(zeros), 'o', markersize=10, label='Zéros')
plt.plot(np.real(poles), np.imag(poles), 'x', markersize=10, label='Pôles', color='red')

plt.xlabel('Partie réelle')
plt.ylabel('Partie imaginaire')
plt.title('Lieu des pôles et zéros (Plan Z)')
plt.grid(True, alpha=0.3)
plt.axis('equal')
plt.legend()
plt.axhline(y=0, color='k', alpha=0.2)
plt.axvline(x=0, color='k', alpha=0.2)
plt.show()

# ========== DIAGRAMME DE NYQUIST ==========
plt.figure(figsize=(8, 8))
ctrl.nyquist(sys)
plt.title('Diagramme de Nyquist')
plt.grid(True, alpha=0.3)
plt.show()

# ========== MARGES DE STABILITÉ ==========
gm, pm, wgm, wpm = ctrl.margin(sys)

print(f"\n=== Marges de stabilité ===")
print(f"Marge de gain: {gm:.2f} dB")
print(f"Marge de phase: {pm:.2f} degrés")

if wgm:
    print(f"Fréquence marge gain: {wgm:.3f} rad/s")
if wpm:
    print(f"Fréquence marge phase: {wpm:.3f} rad/s")