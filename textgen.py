import random
import queue
import argparse
from collections import defaultdict


def get_next_state(markov_chain, state):
    next_state_items = list(markov_chain[state].items())
    next_states = [x[0] for x in next_state_items]
    next_state_counts = [x[1] for x in next_state_items]
    total_count = sum(next_state_counts)
    next_state_probabilities = []
    probability_total = 0
    for next_state_count in next_state_counts:
        probability = float(next_state_count) / total_count
        probability_total += probability
        next_state_probabilities.append(probability_total)
    sample = random.random()
    for index, next_state_probability in enumerate(next_state_probabilities):
        if sample <= next_state_probability:
            return next_states[index]
    return None


def tokenise_text_file(file_name):
    with open(file_name, 'r') as file:
        return ' '.join(file).split()


def create_markov_chain(tokens, order):
    if order > len(tokens):
        raise Exception('Order greater than number of tokens.')
    markov_chain = defaultdict(lambda: defaultdict(int))
    current_state_queue = queue.Queue()
    for index, token in enumerate(tokens):
        if index < order:
            current_state_queue.put(token)
            if index == order - 1:
                current_state = ' '.join(list(current_state_queue.queue))
        elif index < len(tokens):
            current_state_queue.get()
            current_state_queue.put(token)
            next_state = ' '.join(list(current_state_queue.queue))
            markov_chain[current_state][next_state] += 1
            current_state = next_state
    return markov_chain


def get_random_capitalised_state(markov_chain):
    uppercase_states = [state for state in markov_chain.keys() if state[0].isupper()]
    if len(uppercase_states) == 0:
        return random.choice(list(markov_chain.keys()))
    return random.choice(uppercase_states)


def generate_text(markov_chain, words):
    state = get_random_capitalised_state(markov_chain)
    text = state.split()[:words]
    while len(text) < words:
        state = get_next_state(markov_chain, state)
        if state is None:
            state = get_random_capitalised_state(markov_chain)
        text.append(state.split()[-1])
    return ' '.join(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Markov Chain Text Generator')
    parser.add_argument('-f', '--file', required=True,
                        help='Name of file to read text from.')
    parser.add_argument('-o', '--order', default=1, type=int,
                        help='Number of past states each state depends on.')
    parser.add_argument('-w', '--words', default=100, type=int,
                        help='Number of words to generate.')
    pargs = parser.parse_args()

    tokens = tokenise_text_file(pargs.file)
    markov_chain = create_markov_chain(tokens, order=pargs.order)
    print(generate_text(markov_chain, pargs.words))
