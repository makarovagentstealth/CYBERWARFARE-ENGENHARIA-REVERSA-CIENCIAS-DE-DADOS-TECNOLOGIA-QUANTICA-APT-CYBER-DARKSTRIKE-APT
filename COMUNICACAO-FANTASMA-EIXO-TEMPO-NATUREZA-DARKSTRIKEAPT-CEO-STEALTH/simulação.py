import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft
from scipy.integrate import odeint
from hashlib import sha256

# --- Parâmetros Quântico-Mecânicos e de Vento ---
h = 1e-34  # Constante de Planck reduzida (simplificada)
k = 0.1    # Constante de rigidez da folha (N/m)
c = 0.05   # Coeficiente de amortecimento (Ns/m)
Δt = 0.01  # Passo temporal (s)
t = np.arange(0, 10, Δt)

# --- Equação do Movimento da Folha com Incerteza Quântica ---
def leaf_motion(y, t, F_wind):
    x, v = y
    dxdt = v
    dvdt = (F_wind(t) - k*x - c*v) / 0.001  # massa = 0.001kg
    return dxdt, dvdt

# --- Função de Vento Dinâmico (Estático + Quântico) ---
def F_wind(t):
    # Componente estática (direção predominante)
    static = 0.5 * np.sin(2 * np.pi * 0.3 * t)
    # Componente dinâmica (Heisenberg Uncertainty)
    quantum_fluct = h * np.random.normal(scale=1/np.sqrt(Δt))  # ΔxΔp ≥ ħ/2
    return static + quantum_fluct

# --- Simulação ODE ---
sol = odeint(leaf_motion, [0, 0], t, args=(F_wind,))
x = sol[:, 0]

# --- Análise de Fourier (SIGINT) ---
fft_vals = np.abs(fft(x))
freqs = np.fft.fftfreq(len(t), Δt)

# --- Geração de Assinatura (Hash Quântico-Ambienta) ---
binary_x = (x > np.median(x)).astype(int)
binary_str = ''.join(map(str, binary_x))
signature = sha256(binary_str.encode()).hexdigest()

# --- Plotagem dos Resultados ---
plt.figure(figsize=(15, 10))

# Movimento da Folha
plt.subplot(3, 1, 1)
plt.title("Dinâmica da Folha: Posição vs Tempo")
plt.plot(t, x, color='green')
plt.ylabel("Posição (m)")

# Análise de Frequência
plt.subplot(3, 1, 2)
plt.title("Assinatura de Frequência (SIGINT)")
plt.plot(freqs[:len(freqs)//2], fft_vals[:len(fft_vals)//2])
plt.xlabel("Frequência (Hz)")
plt.ylabel("Amplitude")

# Representação Binária
plt.subplot(3, 1, 3)
plt.title("Codificação Binária/Quântica")
plt.step(t, binary_x, where='mid', color='black')
plt.ylabel("0/1")

plt.tight_layout()

print(f"Assinatura Ambiental Gerada: {signature[:16]}... (SHA-256)")
print(f"Entropia do Sistema: {np.std(x):.2e} m")

# --- Efeito de Observação Quântica (Medida Altera Estado) ---
# Simula o colapso da função de onda ao medir
x_observed = x + np.random.normal(0, np.sqrt(h/Δt), len(x))  # Ruído de medição quântico

plt.show()
