def generate_regex(regular_grammar):
    regex_dict = {}

    for rule in regular_grammar:
        lhs, rhs = rule.split("->")
        lhs = lhs.strip()
        rhs = rhs.strip()

        if lhs not in regex_dict:
            regex_dict[lhs] = []

        if len(rhs) == 1:  # Single terminal
            regex_dict[lhs].append(rhs)
        else:  # Non-terminal followed by terminal
            non_terminal, terminal = rhs[0], rhs[1]
            regex_dict[lhs].append(f"{terminal}({non_terminal})*")

    return regex_dict

def main():
    regular_grammar = [
        "S -> aA",
        "A -> bB",
        "B -> cB",
        "B -> d"
    ]

    regex_dict = generate_regex(regular_grammar)

    for non_terminal, regex_list in regex_dict.items():
        regex_str = "|".join(regex_list)
        print(f"{non_terminal} -> {regex_str}")

if __name__ == "__main__":
    main()
