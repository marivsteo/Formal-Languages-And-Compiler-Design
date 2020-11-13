from fa import FiniteAutomata


class Console:

    def __read_fa(self):
        self.fa = FiniteAutomata.read_file('fa.in')

    def __print_all(self):
        print(self.fa)

    def __print_states(self):
        print(self.fa.states)

    def __print_alphabet(self):
        print(self.fa.alphabet)

    def __print_q0(self):
        print(self.fa.q0)

    def __print_final_states(self):
        print(self.fa.final_states)

    def __print_transitions(self):
        print(self.fa.transitions)

    def __print_dfa_check(self):
        print("Yes, it is a DFA") if self.fa.dfa_check() else print("No, it's not a DFA")

    def __verify_sequence(self):
        sequence = input("What is the sequence you want to test?")
        print("Yes, the sequence is accepted") if self.fa.verify_sequence(sequence) else print("No, it's not accepted")

    def run(self):
        self.__read_fa()
        commands = {'1': self.__print_all,
                    '2': self.__print_states,
                    '3': self.__print_alphabet,
                    '4': self.__print_q0,
                    '5': self.__print_final_states,
                    '6': self.__print_transitions,
                    '7': self.__print_dfa_check,
                    '8': self.__verify_sequence}
        ok = False
        while not ok:
            print("0. Exit")
            print("1. Display the finite automata")
            print("2. Display all states")
            print("3. Display the alphabet")
            print("4. Display the initial state/q0")
            print("5. Display the final states")
            print("6. Display all transitions")
            print("7. Check if FA is DFA")
            print("8. Check if a sequence is accepted")
            print(">>")
            cmd = input()
            if cmd in commands.keys():
                commands[cmd]()
            elif cmd == "0":
                ok = True
            else:
                continue


ui = Console()
ui.run()
