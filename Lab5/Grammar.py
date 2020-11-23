class Grammar:

    def __init__(self, Nonterminals, Terminals, Productions, S):
        self.Nonterminals = Nonterminals
        self.Terminals = Terminals
        self.Productions = Productions
        self.S = S

    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName) as file:
            Nonterminals = Grammar.parseLine(file.readline())
            Terminals = Grammar.parseLine(file.readline())
            S = file.readline().split('=')[1].strip()
            Productions = Grammar.parseRules(Grammar.parseLine(''.join([line for line in file])))

            return Grammar(Nonterminals, Terminals, Productions, S)

    @staticmethod
    def parseRules(rules):
        result = []

        for rule in rules:
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [value.strip() for value in rhs.split('|')]

            for value in rhs:
                result.append((lhs, value))

        return result

    def isNonTerminal(self, value):
        return value in self.Nonterminals

    def isTerminal(self, value):
        return value in self.Terminals

    def getProductionsFor(self, nonTerminal):
        if not self.isNonTerminal(nonTerminal):
            raise Exception('Can only show productions for non-terminals')

        return [prod for prod in self.Productions if prod[0] == nonTerminal]

    def __str__(self):
        return 'Nonterminals = { ' + ', '.join(self.Nonterminals) + ' }\n' \
               + 'Terminals = { ' + ', '.join(self.Terminals) + ' }\n' \
               + 'Productions = { ' + ', '.join([' -> '.join(prod) for prod in self.Productions]) + ' }\n' \
               + 'S = ' + str(self.S) + '\n'
