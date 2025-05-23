import os
from scientific_plots.base.base import create_animation

# General Parameters
MAX_DURATION_SEC = 30
FPS = 60
N_FRAMES = MAX_DURATION_SEC * FPS
TRAIL_LENGTH = 300
ROTATION_SPEED = 0.2
T_SPAN = (0, 40)  # Time interval for the simulation

# ==============================
# System dynamics
# ==============================
def lorenz_model(t, state, sigma=10, rho=28, beta=8 / 3):
    x, y, z = state
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    return [dx, dy, dz]


# ==============================
# Main execution
# ==============================
if __name__ == "__main__":
    initial_state = [1, 1, 1]
    lorenz_params = dict(sigma=10, rho=28, beta=8 / 3)
    OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    output_path = os.path.join(OUTPUT_FOLDER, "lorenz_attractor.mp4")
    create_animation(
        model_func=lorenz_model,
        params=lorenz_params,
        initial_state=initial_state,
        output_path=output_path,
        n_frames=N_FRAMES,
        trail_length=TRAIL_LENGTH,
        fps=FPS,
        rotation_speed=ROTATION_SPEED,
        t_span=T_SPAN,
        xlim=[-20, 20],
        ylim=[-30, 30],
        zlim=[0, 50],
        box_aspect=[40, 60, 50],  # Aspect ratio of the box (x, y, z)
    )
