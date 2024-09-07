#!/bin/bash

SCRIPT_PATH="$(pwd)/main.py"
INSTALL_DIR="$HOME/.local/bin"
COMMAND_NAME="generate-password"
mkdir -p "$INSTALL_DIR"
echo "#!/bin/bash
python3 $SCRIPT_PATH \"\$@\"
" > "$INSTALL_DIR/$COMMAND_NAME"
chmod +x "$INSTALL_DIR/$COMMAND_NAME"
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "export PATH=\$PATH:$INSTALL_DIR" >> "$HOME/.bashrc"
    echo "Директория $INSTALL_DIR добавлена в PATH. Изменения вступят в силу после перезапуска терминала или выполнения 'source ~/.bashrc'"
fi
echo "Команда '$COMMAND_NAME' успешно установлена. Теперь вы можете использовать её для запуска скрипта."
