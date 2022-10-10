# Napište interaktivní program, který udržuje seznam řetězců v souborech.
# Po spuštěí programu by program měl vytvořit seznam všech souborů v aktuálním adresáři, které mají příponu .lst. Použijte os.listdir(".") pro získání
# všech souborů a odfiltrujte ty, které nemají příponu .lst. Pokud žádné takové soubory neexistují, program by měl vyzvat uživatele k zadání názvu souboru a připojit
# příponu .lst, pokud ji uživatel nezadá. Pokud existují, měly by bát k dispozici jako číslovaný seznam a uživatel by měl být vyzván k zadání čísla vybraného souboru P, 
# resp. zadat 0, pokud chce vytvořit nový soubor.

# Pokud byl zvolen existující soubor, měly by se načíst jeho prvky. Pokud je prázdný, nebo pokud byl zadán nový soubor, program by měl vypsat:
# "V seznamu nejsou žádné prvky"

# Pokud nejsou v seznamu prvky, měly by být nabídnuty možnosti "Přidat" a "Konec".
# Pokud jsou v seznamu prvky, měly by být nabídnuty možnosti "Přidat", "Vymazat" a "Uložit".

# Snažte se o co nejkratší funkci main() (cca 30 řádků) a umístěte do ní hlavní cyklus programu. 
# Dále napište:
#     - funkci pro získání nového, nebo stávajícího názvu souboru,
#     - funkci pro přeložení možností uživateli a pro získání jeho volby,
#     - funkci pro přidání prvku,
#     - funkci pro výmaz prvku,
#     - funkci pro vypsání seznamu prvků, či názvů souborů,
#     - funkci pro načtení seznamu,
#     - funkci pro uložení seznamu.

# Prvky udržujte v abecedním pořadí nezávislém na velikosti písmen. Kontrolujte, zda je seznam špinavý (tj. změněn bez uložení). Možnost uložení nabídněte pouze tehdy,
# pokud je seznam špinavý.

import os


def main():
    items = []
    lister = os.listdir("./files")
    # list(filter(lambda x: x%2==0, range(80)))
    for i in range(len(lister)):
        if lister[i].__contains__(".lst"):
            items.append(lister[i])
    if len(items) == 0:
        newFile = input("Zadej soubor: ")
        if not newFile.endswith(".lst"):
            newFile = newFile + ".lst"
        createFile(newFile)
        items.append(newFile)
    else:
        print(0, "[Novy soubor]")
        for i, item in enumerate(items):
            print(i + 1, item)
        inp = int(input("Zadej cislo souboru: "))
        if inp == 0:
            newFile2 = input("Zadej soubor: ")
            if not newFile2.endswith(".lst"):
                newFile2 = newFile2 + ".lst"
            createFile(newFile2)
            items.append(newFile2)
        else:
            file = open("./files/" + items[inp - 1], 'r')
            line_list = []
            for line in file:
                line_list.append(line.strip())
            if len(line_list) == 0:
                print("V seznamu nejsou žádné prvky\n")
                inp2 = int(input("0 Pridat\n1 Konec\nZadej:"))
                if inp2 == 0:
                    file = open("./files/" + items[inp - 1], 'a')
                    file.write(input("Zadej text: "))
                    file.close()
                else:
                    return 0
            else:
                print(line_list)
                inp2 = int(input("0 Pridat\n1 Vymazat\n2 Ulozit"))
                if inp2 == 0:
                    file = open("./files/" + items[inp - 1], 'a')
                    file.write(input("Zadej text: "))
                    file.close()
                elif inp2 == 1:
                    file = open("./files/" + items[inp - 1], 'a')
                    file.truncate(0)
                    file.close()
                else:
                    return 0


def createFile(name):
    open("./files/" + name, 'w')


def get_string(message, name="string", default=None, minimum_length=0, maximum_length=80):
    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line:
                if default is not None:
                    return default
                if minimum_length == 0:
                    return ""
                else:
                    raise ValueError("{0} may not be empty".format(
                        name))
            if not (minimum_length <= len(line) <= maximum_length):
                raise ValueError("{name} must have at least "
                                 "{minimum_length} and at most "
                                 "{maximum_length} characters".format(
                    **locals()))
            return line
        except ValueError as err:
            print("ERROR", err)


def get_integer(message, name="integer", default=None, minimum=0,
                maximum=100, allow_zero=True):
    class RangeError(Exception):
        pass

    message += ": " if default is None else " [{0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = int(line)
            if i == 0:
                if allow_zero:
                    return i
                else:
                    raise RangeError("{0} may not be 0".format(name))
            if not (minimum <= i <= maximum):
                raise RangeError("{name} must be between {minimum} "
                                 "and {maximum} inclusive{0}".format(
                    " (or 0)" if allow_zero else "", **locals()))
            return i
        except RangeError as err:
            print("ERROR", err)
        except ValueError as err:
            print("ERROR {0} must be an integer".format(name))


main()
