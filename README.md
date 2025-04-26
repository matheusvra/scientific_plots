# 3D Plot Animator

Follow us on Instagram for updates and more visualizations: [@science_plots_3d](https://www.instagram.com/science_plots_3d/)

This repository is designed to simulate, visualize, and animate 3D plots of dynamical systems like the Lorenz attractor, Rössler attractor etc., using Python and Matplotlib. The animations are customizable, beautifully styled, and exportable as high-quality MP4 videos.

## Requirements

To run this repository, you'll need:

- A Linux-based OS (tested on Manjaro)
- Python 3.11 or newer
- Poetry for dependency and environment management
- ffmpeg installed for video export
- A terminal or IDE (e.g., VS Code) with access to the shell

## How to Install Python (Linux)

If you don’t have Python yet, install it via your package manager:

**Arch/Manjaro:**
```bash
sudo pacman -S python
```

**Debian/Ubuntu:**
```bash
sudo apt install python3.11 python3.11-venv
```

Check version:
```bash
python --version
```

## How to Install Poetry

Install Poetry using the official installer:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Make sure Poetry is available in your shell:

```bash
poetry --version
```

If the command is not found, you may need to add Poetry to your PATH. Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload the shell:

```bash
source ~/.bashrc  # or  source ~/.zshrc
```

## How to Configure the Repository

1. Clone the repository:

```bash
git clone https://github.com/your-username/3d-plot-animator.git
cd 3d-plot-animator
```

2. Install dependencies using Poetry:

```bash
poetry install
```

3. Activate the virtual environment:

```bash
poetry shell
```

4. (Optional) Install FFmpeg if needed:

**Arch/Manjaro:**
```bash
sudo pacman -S ffmpeg
```

**Debian/Ubuntu:**
```bash
sudo apt install ffmpeg
```

## How to Use

You can run the scripts to generate the animations with make commands (Check the Makefile to run the commands manually):

### Lorenz
```shell
make run_lorenz
```

### Rössler
```shell
make run_rossler
```

### Aizawa
```shell
make run_aizawa
```

and etc.

Optional parameters can be configured inside the script, such as:

- `rotation_speed`: Adjust the speed of the camera rotation (e.g., 0.2, 0.4)
- `TRAIL_LENGTH`, `FPS`, `MAX_DURATION_SEC`: Control animation behavior and speed

The final video will be saved in the `output/` folder inside the specific strange attractor folder.

## Acknowledgments

Developed and maintained by **Matheus Anjos**  
Contact: [matheusvra@hotmail.com](mailto:matheusvra@hotmail.com)
