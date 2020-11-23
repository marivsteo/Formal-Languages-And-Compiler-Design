from Grammar import Grammar


class Main:
    def __init__(self):
        self.grammar = None

    def run(self):
        while True:
            print(">>")
            cmd = input()
            if cmd == "1":
                self.readGrammar()
            elif cmd == "2":
                self.printNonTerminals()
            elif cmd == "3":
                self.printTerminals()
            elif cmd == "4":
                self.printProductions()
            elif cmd == "5":
                self.printProductionsForNonTerminal()

    def readGrammar(self):
        self.grammar = Grammar.fromFile('g1.txt')
        print("Read grammar")

    def printNonTerminals(self):
        print(self.grammar.Nonterminals)

    def printTerminals(self):
        print(self.grammar.Terminals)

    def printProductions(self):
        print(self.grammar.Productions)

    def printProductionsForNonTerminal(self):
        print(">>Nonterminal:")
        nonterm = input()
        print(self.grammar.getProductionsFor(nonterm))


main = Main()
main.run()
