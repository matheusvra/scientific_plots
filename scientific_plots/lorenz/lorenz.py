import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import solve_ivp
import progressbar
from loguru import logger

# Configurações gerais
MAX_DURATION_SEC = 30
FPS = 60
N_FRAMES = MAX_DURATION_SEC * FPS
TRAIL_LENGTH = 300
ROTATION_SPEED = 0.2

# Output
OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


# ==============================
# Dinâmica do sistema
# ==============================
def lorenz_model(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]


# ==============================
# Solução numérica
# ==============================
def solve_system(model, t_span, initial_state, t_eval, **kwargs):
    def wrapped_model(t, state):
        return model(t, state, **kwargs)

    sol = solve_ivp(wrapped_model, t_span, initial_state, t_eval=t_eval)
    return sol.y


# ==============================
# Configuração do plot 3D
# ==============================
def setup_plot():
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.grid(False)

    # Limites
    ax.set_xlim([-20, 20])
    ax.set_ylim([-30, 30])
    ax.set_zlim([0, 50])
    ax.set_box_aspect([40, 60, 50])  # Corrige a proporção 3D

    # Remove preenchimento do plano de fundo dos eixos
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Remove a malha (grid)
    ax.xaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
    ax.yaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
    ax.zaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)

    # Torna os eixos brancos
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.zaxis.label.set_color("white")
    ax.tick_params(colors="white")  # Cor dos ticks (valores numéricos)

    return fig, ax


# ==============================
# Animação
# ==============================
# ==============================
# Animação
# ==============================
def create_animation(model_func, params, initial_state, rotation_speed=0.3):
    logger.info("Iniciando simulação...")

    t_span = (0, 40)
    t_eval = np.linspace(t_span[0], t_span[1], N_FRAMES)
    x, y, z = solve_system(model_func, t_span, initial_state, t_eval, **params)
    colors = cm.plasma(np.linspace(0, 1, N_FRAMES))

    fig, ax = setup_plot()
    (line,) = ax.plot([], [], [], lw=2)

    bar = progressbar.ProgressBar(max_value=N_FRAMES)

    def update(frame):
        start = max(0, frame - TRAIL_LENGTH)
        line.set_data(x[start:frame], y[start:frame])
        line.set_3d_properties(z[start:frame])
        line.set_color(colors[frame])

        # Rotação lenta e contínua nos dois eixos
        azim = frame * rotation_speed
        elev = 30 + 10 * np.sin(frame * rotation_speed * np.pi / 180)  # variação suave
        ax.view_init(elev=elev, azim=azim)

        bar.update(frame)
        return (line,)

    logger.info("Criando animação...")
    ani = FuncAnimation(fig, update, frames=N_FRAMES, interval=1000 / FPS, blit=True)

    output_path = os.path.join(OUTPUT_FOLDER, "lorenz_rotating.mp4")
    ani.save(output_path, writer=FFMpegWriter(fps=FPS, bitrate=2000))
    logger.success(f"Vídeo salvo em: {output_path}")

    plt.close()


# ==============================
# Execução principal
# ==============================
if __name__ == "__main__":
    initial_state = [1, 1, 1]
    lorenz_params = dict(sigma=10, rho=28, beta=8 / 3)
    create_animation(lorenz_model, lorenz_params, initial_state, rotation_speed=ROTATION_SPEED)
