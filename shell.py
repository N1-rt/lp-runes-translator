#!/usr/bin/python3

from os import system
from os import path
from src.objects import Runes

# COMMANDS
COMMAND_SC: str = "!"
EXIT_COMMAND: str = COMMAND_SC + "exit"
SHELL_VERSION: str = "1.0.0"
CLEAR_COMMAND: str = COMMAND_SC + "clear"
COMMAND_ENTER_TEXT: str = COMMAND_SC + "et"
PRINT_ENTERED_TEXT: str = COMMAND_SC + "pet"
TRANSLATE_RUNES: str = COMMAND_SC + "tr"
SHIFT_RUNE = COMMAND_SC + "sr"

COMMANDS = [
    EXIT_COMMAND,
    SHELL_VERSION,
    CLEAR_COMMAND,
    COMMAND_ENTER_TEXT,
    PRINT_ENTERED_TEXT,
    TRANSLATE_RUNES,
    SHIFT_RUNE,
]


enter_text: bool = False
entered_text: str = ""
print("Starting shell...")
try:
    print(f"Shell started!\nShell version:{SHELL_VERSION}")
    while True:
        # pegando o input do usuario
        cmd = input("->>>>:").strip()
        # verificando se começa com o caractere de comandos
        if not cmd.startswith(COMMAND_SC) and not enter_text:
            print("ERROR:ENTER A VALID COMMAND!")
        else:
            match cmd:
                case "!clear":
                    system("clear")
                case "!exit":
                    print("EXITING SHELL!!!")
                    break
                case "!et":
                    # enter texto
                    file_or_shell = input(
                        "Type if the text is in a file(f)\nor if you wanna type in shell(s)\n(f/s):"
                    ).strip()
                    if file_or_shell == "s":
                        # se o texto for inserido no shell pegue o input e jogue no objeto Runes
                        entered_text = input("TEXT:")
                        ru = Runes.Runes(entered_text)
                    elif file_or_shell == "f":
                        string_text = ""
                        file_path = input("type the file path:")
                        is_valid_path = (
                            print("Processing...\nfile founded!! >:D")
                            if path.lexists(file_path)
                            else print("File not founded\ncheck file path again!!")
                        )
                        for l in open(file_path, "r"):
                            string_text += l
                            string_text += "•"
                            pass
                        entered_text = string_text
                        ru = Runes.Runes(entered_text)
                    else:
                        print("ERROR!!:TYPE A VALID COMMAND >:(")
                case "!tr":
                    # traduzir as runas
                    if len(entered_text) != 0:
                        try:
                            ru.decipher_rune()
                        except Exception as e:
                            print("ERROR,cound't translate runes!!")
                            raise e
                case "!sr":
                    # inserir um shift nas runas
                    print("#" * 10 + " SETTING SHIFT TO RUNES " + "#" * 10 + "\n")
                    number_shift = input("Type the number for shifting the runes:")
                    ru.set_shift_cipher(int(number_shift))
                case "!help":
                    for command in COMMANDS:
                        print(command)
                case "!invert":
                    # inverter runas
                    print("#" * 10 + " TRANSLATED RUNES INVERTED " + "#" * 10 + "\n")
                    ru.invert_runes_using_atbash()
                case "!st":
                    # exibir as runas e to texto traduzido
                    ru.show_entered_text()

                case _:
                    print("command not founded")
except Exception as e:
    print("ERROR!:cound't start/continue shell operation\n ABORTING!!")
    raise e
