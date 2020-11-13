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

    def verify_sequence(self, sequence):
        if not self.dfa_check():
            return False
        if sequence[0] != self.q0:
            return False
        if sequence == self.q0:
            return True
        if len(sequence) == 1 and sequence != self.q0:
            return False
        current_state = sequence[0]
        second_state = sequence[1]
        while len(sequence) > 1 and current_state is not None:
            found = False
            for t in self.transitions:
                if current_state == t[0] and second_state in self.transitions[t]:
                    found = True
                    sequence = sequence[1:]
                    current_state = sequence[0]
                    if len(sequence) > 1:
                        second_state = sequence[1]
                    break

            if not found:
                return False
        return current_state is not None and sequence in self.final_states

    def __str__(self):
        return "states = { " + ', '.join(self.states) + " }\n" \
                "alphabet = { " + ', '.join(self.alphabet) + " }\n" \
                "q0 = { " + self.q0 + " }\n" \
                "final_states = { " + ', '.join(self.final_states) + " }\n" \
                "transitions = { " + str(self.transitions) + " } "
