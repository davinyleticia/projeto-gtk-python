# Configuração de Ambiente Virtual

```bash
python3 -m venv --system-site-packages venv

source venv/bin/activate

python --noconsole --onefile main.py

```

# Dependência do sistema (Linux/Debian/Ubuntu)

O GTK 3 não é instalado via `pip`, ele é uma biblioteca do sistema operacional

```bash

sudo apt update
sudo apt install python3-gi python3-gi-cairo girl1.2-gtk-3.0 libgirepository1.0-dev

```
