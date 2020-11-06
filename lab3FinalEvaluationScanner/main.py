from PIF import PIF
from Scanner import Scanner
from SymbolTable import SymbolTable
from Scanner import read_file, reserved_words, separators, operators


def main():
    read_file()
    file_name = "p1.txt"
    symbol_table = SymbolTable(15)
    pif = PIF()
    scanner = Scanner()
    exception_message = ""

    with open(file_name, 'r') as file:
        line_counter = 0
        for line in file:
            line_counter += 1
            for token in scanner.tokenize(line.strip()):
                if token in reserved_words+separators+operators:
                    if token == ' ':
                        continue
                    pif.add(token, (0, 0))
                elif scanner.is_identifier(token) or scanner.is_constant(token):
                    identifier = symbol_table.position(token)
                    pif.add(token, identifier)
                else:
                    exception_message += 'Lexical error at token ' + token + ', at line ' + str(line_counter) + "\n"

    with open('st.out', 'w') as writer:
        writer.write(str(symbol_table))

    with open('pif.out', 'w') as writer:
        writer.write(str(pif))

    if exception_message == '':
        print("Lexically correct")
    else:
        print(exception_message)


main()
