def generate_language(productions, start_symbol):
    language = []

    def derive(sequence, index):
        if index == len(sequence):
            language.append(''.join(sequence))
            return
        for production in productions.get(sequence[index], []):
            new_sequence = sequence[:index] + list(production) + sequence[index + 1:]
            derive(new_sequence, index + len(production))

    derive([start_symbol], 0)
    return language

# Example usage
productions = {
    'S': ['aA', 'bB'],
    'A': ['c'],
    'B': ['d']
}
start_symbol = 'S'

derivation_language = generate_language(productions, start_symbol)
for string in derivation_language:
    print(string)
