import random

def get_next_state(markov_chain, state):
    next_state_items = markov_chain[state].items()
    next_states = map(lambda x: x[0], next_state_items)
    next_state_counts = map(lambda x: x[1], next_state_items)
    total_count = sum(next_state_counts)
    next_state_probabilities = []
    running_total = 0
    for next_state_count in next_state_counts:
        probability = float(next_state_count) / total_count
        running_total += probability
        next_state_probabilities.append(running_total)
    sample = random.random()
    for index, next_state_probability in enumerate(next_state_probabilities):
        if sample <= next_state_probability:
            return next_states[index]
    return None


def main():
    with open('text', 'r') as file:
        for line in file:
            print(line)


if __name__ == '__main__':
    markov_chain = {
        'a': {
            'b': 3,
            'c': 1,
            'f': 7
        }
    }
    print(get_next_state(markov_chain, 'a'))
