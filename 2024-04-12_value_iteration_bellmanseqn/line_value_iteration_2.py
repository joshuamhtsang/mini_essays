"""The line MDP with rewards at each end"""

class MDP:
    """Class representing a Markov Decision Process (MDP)"""
    def __init__(self, N):
        self.N = N # length of the line
    
    def is_end(self, state):
        """Function to check whether a state is terminal"""
        result = False
        if state == 1:
            result = True
        elif state == self.N:
            result = True
        return result
    
    def terminal_states_and_rewards(self):
        terminal_states = {
            1: 1.0,
            self.N: 75.0
        }
        return terminal_states

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

    def next_state_prob_reward(self, state, action):
        """Function to return list of triples of:
        [(<next_state>, <transition_probability>, <reward>), ...]"""
        result = []
        if action == "right":
            result.append((state+1, 1.0, -1.0))
        elif action == "left":
            result.append((state-1, 1.0, -1.0))
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
        for next_state, trans_prob, reward in mdp.next_state_prob_reward(state, action):
            sum_over_next_states += trans_prob * (reward + mdp.discount()*V[next_state])
        return sum_over_next_states

    # Loop over the states and perform value iteration
    for iteration in range(0, num_iters):
        print("V     = ", V)
        V_new = {}
        for state in mdp.states():
            if mdp.is_end(state):
                V_new[state] = mdp.terminal_states_and_rewards()[state]
            else:
                V_new[state] = max(Q(state, action) for action in mdp.actions(state))
        
        print("V_new = ", V_new)
        V = V_new
    
    # Print out the final policy
    pi = {}
    for state in mdp.states():
        if mdp.is_end(state):
            pi[state] = None
        else:
            pi[state] = max((Q(state, action), action) for action in mdp.actions(state))
    
    print(pi)


if __name__ == "__main__":
    mdp1 = MDP(100)
    print([mdp1.actions(i) for i in mdp1.states()])
    print(mdp1.next_state_prob_reward(2, "left"))
    print(mdp1.next_state_prob_reward(1, "right"))

    value_iteration(mdp1, 1000)

    # Write a function to print out the policy too.
