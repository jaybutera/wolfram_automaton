from PIL import Image
import numpy as np

# Map production rules (current state -> next state)
'''
rules = {
    (True, True, True) : False,
    (True, True, False) : False,
    (True, False, True) : False,
    (True, False, False) : True,
    (False, True, True) : True,
    (False, True, False) : True,
    (False, False, True) : True,
    (False, False, False) : False,
}
'''
rules = {
    (True, True, True) : False,
    (True, True, False) : True,
    (True, False, True) : True,
    (True, False, False) : False,
    (False, True, True) : True,
    (False, True, False) : True,
    (False, False, True) : True,
    (False, False, False) : False,
}

# Generage based on rules
def new_state(state):
    # Always pad state with two empty cells on either side
    # This allows any 3 cell rule to be realized
    ns = [False, False] # New state

    for i in range(len(state)-2):
        ns.append( rules[ tuple(state[i:i+3]) ] )

    # End padding
    ns.extend([False, False])

    return ns

# Simulate automata and return all states as a 2D array
def run(num_epochs):
    # Initial state
    cur_state = [False, False, True, False, False]
    # Create 2D array to store full generation history
    states = np.zeros( (num_epochs, len(cur_state) + num_epochs*2) )

    for epoch in range(num_epochs):
        # Record state into forever land
        for i in range(len(cur_state)):
            # Translate cells to center image
            states[epoch, i+(num_epochs-epoch)] = 255 if cur_state[i] else 0

        # Update
        cur_state = new_state( cur_state )

    return states

if __name__ == '__main__':
    # Number of epochs generated, this includes the initial state
    num_epochs = 1500

    # Simulate
    states = run(num_epochs)

    # Create bitmap image
    img = Image.fromarray(states)
    img.show()
