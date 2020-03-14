from Automata import Automata
from MealyAutomata import MealyAutomata
from MooreAutomata import MooreAutomata
import Partition

class Equivalence:
    """
    Main class of the model 
    """

    EQUIVALENT_MACHINES = "They are equivalent"
    NOT_EQUIVALENT_MACHINES = "They are not equivalent"
    PRIMA = "'"

    def __init__(self, automata1, automata2):
        self.automata1 = automata1
        self.automata2 = automata2

    """
    The second automata will be the one that will be replaced
    We have to check first which one is bigger 
    """

    def rename_states(self, automata1, automata2):
        states_automata1 = automata1.S
        state_automata2 = automata2.S

        new_states = {}

        for state in state_automata2:
            new_states[state] = ""
            if state in states_automata1:
                new_states[state] = state+self.PRIMA

        automata2.replace_states(new_states)

    def sum_automatas(self, automata1, automata2):
        Q = (automata1.Q).union(automata2.Q)
        state_map = automata1.state_map.update(automata2.state_map)
        transition_map = automata1.transition_map.update(
            automata2.transition_map)

        automata = Automata(Q, automata1.S, automata2.R)
        automata.state_map = state_map
        automata.transition_map = transition_map
        self.automata_sum = automata
        return automata


    def validate_equivalence(self, automata1, automata2, partitions):
        elements_in_partition = False
        initial_state = False

        states_automata1 = automata1.Q
        states_automata2 = automata2.Q

        initial_automata1 = automata1.initial_state
        initial_automata2 = automata2.initial_state

        for partition in partitions:
            union_1 = partition.intersection(states_automata1)
            union_2 = partition.intersection(states_automata2)

            if initial_automata1 in partition:
                if initial_automata2 in partition:
                    initial_state = True
                else:
                    return initial_state

            if len(union_1) == 0 or len(union_2) == 0:
                return elements_in_partition

        elements_in_partition = True
        return (elements_in_partition and initial_state)




ma = MealyAutomata(['A','B','C'],[0,1],[0,1],'A')
ma.add_state('B')
ma.add_state('C')
ma.add_transition(1,'A', 'C',0)
ma.add_transition(0,'A','B',1)
ma.add_transition(0,'B','A',1)
ma.add_transition(1,'B','C',0)
ma.add_transition(0,'C','A',1)
ma.add_transition(1,'C','C',1)

print(ma.sort_transition_map())
print(ma.get_response('A'))
print(ma.get_response('B'))
print(ma.get_response('C'))


print(Partition.first_partition(ma))