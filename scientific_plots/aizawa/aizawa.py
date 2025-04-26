import os
from scientific_plots.base.base import create_animation

# General Parameters
MAX_DURATION_SEC = 30
FPS = 90
N_FRAMES = MAX_DURATION_SEC * FPS
TRAIL_LENGTH = 600
ROTATION_SPEED = 0.2
T_SPAN = (0, 200)  # Time interval for the simulation


# ==============================
# System dynamics
# ==============================
def aizawa_model(t, state, a=0.95, b=0.7, c=3.5, d=4.5, e=0.7, f=0.25):
    x, y, z = state
    dx = (z - b) * x - d * y
    dy = d * x + (z - b) * y
    dz = c + a * z - (z**3) / 3 - (x**2 + y**2) * (1 + e * z) + f * z * (x**3)
    return [dx, dy, dz]


# ==============================
# Main execution
# ==============================
if __name__ == "__main__":
    initial_state = [0.1, 1.0, 0.01]

    aizawa_params = {
        "a": 0.95,
        "b": 0.7,
        "c": 0.6,
        "d": 3.5,
        "e": 0.25,
        "f": 0.1,
    }

    OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    output_path = os.path.join(OUTPUT_FOLDER, "aizawa_attractor.mp4")
    create_animation(
        model_func=aizawa_model,
        params=aizawa_params,
        initial_state=initial_state,
        output_path=output_path,
        n_frames=N_FRAMES,
        trail_length=1200,
        fps=FPS,
        rotation_speed=ROTATION_SPEED,
        t_span=T_SPAN,
        xlim=[-2, 2],
        ylim=[-2, 2],
        zlim=[-1, 2],
        box_aspect=[40, 40, 30],  # To keep proportions beautiful
    )
