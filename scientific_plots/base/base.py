import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from matplotlib import cm
from scipy.integrate import solve_ivp
import progressbar
from loguru import logger

# General Parameters
MAX_DURATION_SEC = 30
FPS = 60
N_FRAMES = MAX_DURATION_SEC * FPS
TRAIL_LENGTH = 300
ROTATION_SPEED = 0.2

# ==============================
# Numerical integration
# ==============================
def solve_system(model, t_span, initial_state, t_eval, **kwargs):
    def wrapped_model(t, state):
        return model(t, state, **kwargs)

    sol = solve_ivp(wrapped_model, t_span, initial_state, t_eval=t_eval)
    return sol.y


# ==============================
# 3D plot setup
# ==============================
def setup_plot(xlim, ylim, zlim, box_aspect):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    fig.patch.set_facecolor("black")
    ax.set_facecolor("black")
    ax.grid(False)

    # Limites
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)
    ax.set_box_aspect(box_aspect)  # Fixes the 3D aspect ratio

    # Remove background plane filling of the axes
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False

    # Remove the grid
    ax.xaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
    ax.yaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)
    ax.zaxis._axinfo["grid"]["color"] = (1, 1, 1, 0)

    # Make the axes white
    ax.xaxis.label.set_color("white")
    ax.yaxis.label.set_color("white")
    ax.zaxis.label.set_color("white")
    ax.tick_params(colors="white")  # Color of the ticks (numerical values)

    return fig, ax


# ==============================
# Animation creation
# ==============================
def create_animation(
    model_func,
    params,
    initial_state,
    output_path, 
    n_frames=N_FRAMES,
    trail_length=TRAIL_LENGTH,
    fps=FPS,
    rotation_speed=0.3,
    t_span=(0, 40),
    **kwargs,
):
    logger.info("Starting simulation...")

    t_eval = np.linspace(t_span[0], t_span[1], n_frames)
    x, y, z = solve_system(model_func, t_span, initial_state, t_eval, **params)
    colors = cm.plasma(np.linspace(0, 1, n_frames))

    xlim: list[int] = kwargs.get("xlim", [-20, 20])
    ylim: list[int] = kwargs.get("ylim", [-30, 30])
    zlim: list[int] = kwargs.get("zlim", [0, 50])
    box_aspect: list[int] = kwargs.get("box_aspect", [40, 60, 50])
    
    fig, ax = setup_plot(
        xlim=xlim,
        ylim=ylim,
        zlim=zlim,
        box_aspect=box_aspect,
    )
    (line,) = ax.plot([], [], [], lw=2)

    bar = progressbar.ProgressBar(max_value=n_frames)

    def update(frame):
        start = max(0, frame - trail_length)
        line.set_data(x[start:frame], y[start:frame])
        line.set_3d_properties(z[start:frame])
        line.set_color(colors[frame])

        # Slow and continuous rotation on all three axes
        azim = frame * rotation_speed
        elev = 30 + 10 * np.sin(frame * rotation_speed * np.pi / 180)  # smooth variation
        roll = 10 * np.cos(frame * rotation_speed * np.pi / 180)  # additional smooth variation
        ax.view_init(elev=elev, azim=azim)
        ax.dist = 10 + roll  # Simulate roll by varying the distance

        bar.update(frame)
        return (line,)

    logger.info("Creating animation...")
    ani = FuncAnimation(fig, update, frames=n_frames, interval=1000 / fps, blit=True)

    ani.save(output_path, writer=FFMpegWriter(fps=fps, bitrate=2000))
    logger.success(f"Video saved in: {output_path}")

    plt.close()

