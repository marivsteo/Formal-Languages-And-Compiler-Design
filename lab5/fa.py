class FiniteAutomata:

    def __init__(self, states, alphabet, q0, final_states, transitions):
        self.states = states
        self.alphabet = alphabet
        self.q0 = q0
        self.final_states = final_states
        self.transitions = transitions

    @staticmethod
    def get_values(line):
        return line.strip().split(' ')[2:]

    @staticmethod
    def read_file(file_name):
        with open(file_name) as file:
            states = FiniteAutomata.get_values(file.readline())
            alphabet = FiniteAutomata.get_values(file.readline())
            q0 = FiniteAutomata.get_values(file.readline())[0]
            final_states = FiniteAutomata.get_values(file.readline())
            file.readline()
            transitions = {}
            for line in file:
                starting_state = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                symbol = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                ending_state = line.strip().split('->')[1].strip()

                if (starting_state, symbol) in transitions.keys():
                    transitions[(starting_state, symbol)].append(ending_state)
                else:
                    transitions[(starting_state, symbol)] = [ending_state]

            return FiniteAutomata(states, alphabet, q0, final_states, transitions)

    def dfa_check(self):
        for k in self.transitions.keys():
            if len(self.transitions[k]) > 1:
                return False
        return True

    def __str__(self):
        return "states = { " + ', '.join(self.states) + " }\n" \
                "alphabet = { " + ', '.join(self.alphabet) + " }\n" \
                "q0 = { " + self.q0 + " }\n" \
                "final_states = { " + ', '.join(self.final_states) + " }\n" \
                "transitions = { " + str(self.transitions) + " } "
