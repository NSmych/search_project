# Определяем переменную PYTHON с использованием shell
PYTHON := $(shell command -v python3 2> /dev/null || command -v python 2> /dev/null)

# Если переменная PYTHON не определена, выведите сообщение об ошибке
ifndef PYTHON
	$(error 'python' is not found. Please install Python or specify it in your PATH.)
endif

# Определяем переменную PIP в зависимости от версии Python
ifeq ($(shell $(PYTHON) -c 'import sys; print(sys.version_info.major)'),3)
    PIP := pip3
else
    PIP := pip
endif

.DEFAULT_GOAL := help

venv:
	$(PYTHON) -m venv venv

install:
	source venv/bin/activate && $(PIP) install -r requirements.txt && deactivate

help:
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  venv     Create a virtual environment."
	@echo "  install  Install dependencies from requirements.txt."
	@echo "  help     Show this help message."
