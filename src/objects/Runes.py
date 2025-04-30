"""
Version:1.0.0
MadeBy:n1r7

"""

import os
from pathlib import Path


class Runes:
    def __init__(self, runes_text: str):
        self.runes_text = runes_text  # variavel onde as runas vão ser armazenadas
        self.shift = 0  # obtendo quanto de shifting a pessoa vai querer nas runas

    # lista das letras ; runas ; numeros correspondentes de cada runa para fazer a tradução
    alphabet: list[str] = []
    primus: list[int] = []
    runes: list[str] = []
    translated_text = ""
    translated_text_without_shift = ""
    inverted_runes = -1

    # caminhos dos assets
    PATH = Path.cwd()
    ALPHABET_PATH = os.path.join(PATH, "assets/alph.txt")
    PRIMUS_PATH = os.path.join(PATH, "assets/primus.txt")
    RUNES_PATH = os.path.join(PATH, "assets/runes.txt")

    rune_shift = None
    for letter in open(ALPHABET_PATH, "r"):
        alphabet.append(letter.strip())
        pass
    for num in open(PRIMUS_PATH, "r"):
        primus.append(int(num.strip()))
        pass
    for rune in open(RUNES_PATH, "r"):
        runes.append(rune.strip())

    # decifrando as runas
    def decipher_rune(self):
        try:
            # resetando as variaveis antes de inserir algo nelas
            self.translated_text = ""
            self.translated_text_without_shift = ""
            # obtendo o valor de cada runa no texto inserido!
            for r in self.runes_text:
                if (
                    r.strip() in Runes.runes
                ):  # removendo possiveis "/n" no texto e verificando se a runa esta presente na lista
                    rune_index = Runes.runes.index(
                        r
                    )  # obtendo o valor do index na runa

                    # transcrevendo o valor da runa para o valor do caractere baseado na posição
                    # caso 1: se o valor do shift + o valor do index da runa for menor ou igual à 28(quantia de runas)
                    # entao: valor da runa traduzida vai ser o valor do seu index + o shift no na letra do alfabeto correspondente
                    # caso 2: valor do index da runa + shift é maior que 28(quantia de runas)
                    # então: valor da runa traduzida vai ser o resto da divisão desse valor por 28(como dar a volta em um relogio e começar a contar denovo)
                    rune_shift = (
                        Runes.alphabet[rune_index + self.shift]
                        if rune_index + self.shift <= 28
                        else Runes.alphabet[(rune_index + self.shift) % 28]
                    )
                    # adicionar esses valores na variavel de texto
                    self.translated_text_without_shift += Runes.alphabet[rune_index]
                    self.translated_text += rune_shift

                elif r == "•":
                    # caso o caractere for um ponto,então adicionar caractere de um espaço ao texto decodificado
                    self.translated_text += " "
                    self.translated_text_without_shift += " "
                else:
                    # se o caractere nao estiver na lista de runas
                    # exibir um erro!
                    print(f"Rune({r}) not founded <:(")
            # exibindo valores para o usuario
            print("#" * 10 + " Translated Runes " + "#" * 10)
            print("\n")
            print(f"Original runes:\n{self.runes_text}\n")
            print(f"Original Translated text:\n{self.translated_text_without_shift}\n")
            print(
                f"Translated text With shift:\n{self.translated_text}\n"
            ) if self.shift != 0 else print("No shift included!")
            print(f"Shift value:{self.shift}\n")
        except Exception as e:
            raise e

    def sum_gematria_values(self):
        # WIP
        for r in self.runes_text:
            if r.strip() in Runes.runes:
                rune_index = Runes.rune.index(r)

    def set_shift_cipher(self, shift_num):
        # auto-explicativo
        self.shift = int(shift_num)

    def invert_runes_using_atbash(self):
        # decifrando texto usanto atbash: a = z ; b = y = c = x idem...
        self.inverted_runes = self.inverted_runes * -1
        rune_atbash_translated = ""
        inverted_runes_text = ""
        for r in self.runes_text:
            # mesmo processo do metodo decipher
            if r.strip() in Runes.runes:
                rune_index = Runes.runes.index(r)
                rune_atbash = Runes.alphabet[-rune_index - 1]
                inverted_runes_text += Runes.runes[-rune_index - 1]
                rune_atbash_translated += rune_atbash

            elif r.strip() == "•":
                rune_atbash_translated += " "
                inverted_runes_text += "•"
        # substituindo os valores invertidos para a lista de runas e lista de texto traduzido para que possa
        # ser feito shifiting e outras operações!
        self.translated_text = rune_atbash_translated
        self.runes_text = inverted_runes_text
        # exibindo valores para usuario
        print(f"Translated atbash runes text:\n{rune_atbash_translated}\n")
        print(
            "[Warning] the text now is inverted,if you want to back to normal use the command again\n"
        )
        print(f"Inverted Runes status:{self.inverted_runes}\n")
        pass

    def show_entered_text(self):
        # auto-explicativo
        print(f"entered translated text:\n{self.translated_text}\n")
        print(f"entered runes:\n{self.runes_text}\n")
