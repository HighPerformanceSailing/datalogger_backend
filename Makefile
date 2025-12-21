
all: update-git install run

install:
	@echo "Installing Poetry dependencies"
	poetry install

update-git:
	@echo "Pulling from GitHub repository"
	git pull


run:
	@echo "Running Data Logger Backend"
	poetry run python src/main.py

