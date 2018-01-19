# Map production rules (current state -> next state)
rules = {
    (True, True, True) : True,
    (True, True, False) : True,
    (True, False, True) : True,
    (True, False, False) : True,
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

# Number of rows to generate
epochs = 10
cur_state = [False, False, True, False, False]

print (cur_state)
for i in range(epochs):
    cur_state = new_state( cur_state ) # Update
    print (cur_state)
