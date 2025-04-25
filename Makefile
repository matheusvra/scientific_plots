create_env:
	printf "Creating virtual environment...\n"
	poetry env use python3

install:
	printf "Installing dependencies...\n"
	poetry install

run_lorenz:
	printf "Creating lorenz video...\n"
	poetry run python scientific_plots/lorenz/lorenz.py

run_rossler:
	printf "Creating rossler video...\n"
	poetry run python scientific_plots/rossler/rossler.py

