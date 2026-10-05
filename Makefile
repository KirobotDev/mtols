CC       := gcc
CFLAGS   := -Wall -Wextra -O2
TARGET   := tools.exe
SOURCES  := menu.c

PYTHON := $(shell py --version >NUL 2>&1 && echo py || echo python)

.PHONY: all deps build run clean help

all: deps build

deps:
	$(PYTHON) -m pip install -r requirements.txt

build: $(TARGET)

$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) $(SOURCES) -o $(TARGET)
	@echo [OK] Compilation terminee : $(TARGET)

run: build
	@./$(TARGET)

clean:
	@cmd /c "del /q $(TARGET) >NUL 2>&1"
	@cmd /c "if exist $(TARGET) (echo [ATTENTION] $(TARGET) est encore utilise par un MTools ouvert.) else (echo [OK] Nettoyage termine)"
	@cmd /c "if exist $(TARGET) (echo            Ferme la ou les fenetres MTools, puis relance make clean.) else (echo.)"

help:
	@echo.
	@echo MTOLS - commandes disponibles :
	@echo.
	@echo   make         Prepare tout (deps + compilation)
	@echo   make deps    Installe les dependances Python
	@echo   make build   Compile tools.exe
	@echo   make run     Compile puis lance tools.exe
	@echo   make clean   Supprime les fichiers generes
	@echo.