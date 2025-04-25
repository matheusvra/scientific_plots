import os
from scientific_plots.base.base import create_animation

# General Parameters
MAX_DURATION_SEC = 45
FPS = 60
N_FRAMES = MAX_DURATION_SEC * FPS
TRAIL_LENGTH = 1000
ROTATION_SPEED = 0.3
T_SPAN = (0, 150)  # Time interval for the simulation

# ==============================
# System dynamics
# ==============================
def rossler_model(t, state, a=0.2, b=0.2, c=5.7):
    x, y, z = state
    dx = -y - z
    dy = x + a * y
    dz = b + z * (x - c)
    return [dx, dy, dz]


# ==============================
# Main execution
# ==============================
if __name__ == "__main__":
    initial_state = [1, 1, 1]
    rossler_params = {
        "a": 0.2,
        "b": 0.2,
        "c": 5.7,
    }
    OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    output_path = os.path.join(OUTPUT_FOLDER, "rossler_attractor.mp4")
    create_animation(
        model_func=rossler_model,
        params=rossler_params,
        initial_state=initial_state,
        output_path=output_path,
        n_frames=N_FRAMES,
        trail_length=TRAIL_LENGTH,
        fps=FPS,
        rotation_speed=ROTATION_SPEED,
        t_span=T_SPAN,
        xlim=[-15, 15],
        ylim=[-15, 10],
        zlim=[0, 20],
        box_aspect=[40, 30, 25],  # Aspect ratio of the box (x, y, z)
    )
