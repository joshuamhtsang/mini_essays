
class MDP:
    """Class representing a Markov Decision Process (MDP)"""
    def __init__(self, N):
        self.N = N # length of the line
    
    def is_end(self, state):
        """Function to check whether a state is terminal"""
        return state == self.N

    def states(self):
        """Function to return an generator over all states"""
        return range(1,self.N + 1)

    def actions(self, state):
        """Function to return avaliable actions for a given state"""
        possible_actions = []
        if state + 1 <= self.N:
            possible_actions.append("right")
        if state - 1 >= 1:
            possible_actions.append("left")
        return possible_actions
    
    def discount(self):
        """Discount factor"""
        return 1.0

    def P(self, state, action):
        """Function representing P(s',r|s,a) in Bellmans equation
        of an MDP.
        Given a (state, action) pair returns a list of triples of:
        [(<next_state>, <transition_probability>, <reward>), ...]"""
        result = []
        if action == "right":
            result.append((state+1, -1.0, 1.0))
        elif action == "left":
            result.append((state-1, -1.0, 1.0))
        return result

def value_iteration(mdp, num_iters):
    """Function to perform Value Iteration on an MDP object"""
    # Store the State Value Function values in a dictionary
    V = {}

    # Initialize all state values to zero
    for state in mdp.states():
        V[state] = 0.0
    
    print(V)

    # Define the Quality Function, Q
    def Q(state, action):
        # Sum over available next states
        sum_over_next_states = 0
        for next_state, reward, trans_prob in mdp.P(state, action):
            sum_over_next_states += trans_prob * (reward + mdp.discount()*V[next_state])
        return sum_over_next_states

    # Loop over the states and perform value iteration
    for iteration in range(0, num_iters):
        V_new = {}
        for state in mdp.states():
            if mdp.is_end(state):
                V_new[state] = 1.0
            else:
                V_new[state] = max(Q(state, action) for action in mdp.actions(state))
        
        print(f'Iteration = {iteration:3d}, V_new = {V_new}')
        V = V_new


if __name__ == "__main__":
    mdp1 = MDP(10)
    print([mdp1.actions(i) for i in mdp1.states()])
    print(mdp1.P(2, "left"))
    print(mdp1.P(1, "right"))

    value_iteration(mdp1, 20)
