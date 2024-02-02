# Define the PYTHON variable using shell script
PYTHON := $(shell command -v python3 2> /dev/null || command -v python 2> /dev/null)

# Check if the PYTHON variable is defined, otherwise show an error message
ifndef PYTHON
	$(error 'python' is not found. Please install Python or specify it in your PATH.)
endif

# Determine the PIP variable based on the Python version
ifeq ($(shell $(PYTHON) -c 'import sys; print(sys.version_info.major)'),3)
    PIP := pip3
else
    PIP := pip
endif

# Set the default target to 'help'
.DEFAULT_GOAL := help

# Add environment variables to local .env file
init:
	@touch .env
	@read -p "Please, provide your SPOTIFY_CLIENT_ID: " SPOTIFY_CLIENT_ID; \
	echo "SPOTIFY_CLIENT_ID=$$SPOTIFY_CLIENT_ID" >> .env
	@read -s -p "Please, provide your SPOTIFY_CLIENT_SECRET: " SPOTIFY_CLIENT_SECRET; \
	echo "SPOTIFY_CLIENT_SECRET=$$SPOTIFY_CLIENT_SECRET" >> .env

# Create a virtual environment and install dependencies from requirements.txt
install: venv
	source venv/bin/activate && $(PIP) install -r requirements.txt && deactivate

# Run the project
run:
	source venv/bin/activate && python src/main.py && deactivate

# Display help message with available targets
help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install  Create a virtual environment and install dependencies from requirements.txt."
	@echo "  run      Run the project."
	@echo "  help     Show this help message."
