import re

reserved_words = []
separators = []
operators = []


def read_file():
    with open('token.in', 'r') as f:
        f.readline()
        for i in range(16):
            operators.append(f.readline().strip())
        for i in range(10):
            separator = f.readline().strip()
            if separator == "space":
                separator = " "
            separators.append(separator)
        for i in range(23):
            reserved_words.append(f.readline().strip())


class Scanner:

    def is_identifier(self, token):
        # backslashes are not handled in any special way
        return re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9])', token) is not None

    def is_constant(self, token):
        # backslashes are not handled in any special way
        return re.match(r'^(0|[+\-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_part_of_operator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.get_operator_token(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.get_string_token(line, index)
                tokens.append(token)
                token = ''

            elif line[index] in separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def get_string_token(self, line, index):
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def is_part_of_operator(self, char):
        for operator in operators:
            if char in operator:
                return True
        return False

    def get_operator_token(self, line, index):
        token = ''
        while index < len(line) and self.is_part_of_operator(line[index]):
            token += line[index]
            index += 1

        return token, index
