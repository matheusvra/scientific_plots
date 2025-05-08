import os
from scientific_plots.base.base import create_animation

# ==============================
# Parâmetros gerais
# ==============================
MAX_DURATION_SEC = 45
FPS = 90
N_FRAMES = MAX_DURATION_SEC * FPS
TRAIL_LENGTH = 600
ROTATION_SPEED = 0.1
T_SPAN = (0, 60)


# ==============================
# Dinâmica do sistema "Corda"
# ==============================
def corda_model(t, state, a=0.25, b=4.0, F=8.0, G=1.0):
    x, y, z = state
    dx = -y - z - a * x + a * F
    dy = x * y - b * x * z - y + G
    dz = b * x * y + x * z - z
    return [dx, dy, dz]


# ==============================
# Execução principal
# ==============================
if __name__ == "__main__":
    initial_state = [1.0, 0.0, 0.0]
    corda_params = dict(a=0.25, b=4.0, F=8.0, G=1.0)

    OUTPUT_FOLDER = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(OUTPUT_FOLDER, "corda_attractor.mp4")

    create_animation(
        model_func=corda_model,
        params=corda_params,
        initial_state=initial_state,
        output_path=output_path,
        n_frames=N_FRAMES,
        trail_length=TRAIL_LENGTH,
        fps=FPS,
        rotation_speed=ROTATION_SPEED,
        t_span=T_SPAN,
        xlim=[-10, 10],
        ylim=[-15, 40],
        zlim=[-30, 40],
        box_aspect=[40, 40, 50],
    )
