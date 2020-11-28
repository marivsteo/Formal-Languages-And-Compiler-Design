class Grammar:
    def __init__(self, fileName):
        self.Terminals: [str] = []
        self.Nonterminals: [str] = []
        self.Productions: dict = {}
        self.fileName = fileName
        self.read_from_file(self.fileName)

    def read_from_file(self, __path_to_file):
        with open(self.fileName, 'r') as fh:
            text_lines = fh.readlines()

        self.Nonterminals = [elem for elem in text_lines[0].strip().split(',')]
        self.Terminals = [elem for elem in text_lines[1].strip().split(',')]

        for line in text_lines[2:]:
            split = line.strip().split("->")
            non_terminal = split[0]
            right_side = [elem.strip() for elem in split[1].split('|')]

            list = self.Productions.get(non_terminal, [])
            for elem in right_side:
                list.append(elem)

            self.Productions[non_terminal] = list

    def get_terminals(self):
        return self.Terminals

    def get_non_terminals(self):
        return self.Nonterminals

    def get_productions(self):
        return self.Productions

    def get_production_for_non_terminal(self, non_terminal):
        return self.Productions.get(non_terminal, [])