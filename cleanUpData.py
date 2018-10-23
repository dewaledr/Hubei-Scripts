# Try to clean this data using Function programming paradigm

import re
states = ['  Alabama ', 'Georgi-a', 'Georgia!', 'georgia', 'floRida', 'south Carolina',
 'West Virginia?', 'new ??york', 'NEW JERSEy','iDAho']

def remove_punctuation(inString):
    return re.sub('[!#?-]', '', inString)

cleanOps = [str.strip, remove_punctuation, str.title]

def cleanStrings(strings, ops):
    result = []
    for state in strings:
        for tasks in ops:
        #for function in ops:
            state = tasks(state)
            #state = function(state)
            #print(state)
        result.append(state)
    return result

# Run the program
print(cleanStrings(states, cleanOps))
print("...End of Clean up Operation...")