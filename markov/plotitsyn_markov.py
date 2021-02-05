# Markov algorithm by Karrtopelka %)%)%)%)%)%)%)@*&$(@


def markov(alph="", rule="", uword=""):
    # alphabet
    alphabet = list(set(alph.lower()))
    alphabet.sort()

    # rules
    temp = []
    rules = {}
    while len(temp) != len(rule.lower().split(" ")):
        w = rule.lower()
        c = w.split(" ")
        for b in range(0, len(c)):
            temp.append(c[b])

    for i in temp:
        wc = i.split("-")
        if wc[0] in wc[1]:
            return "Rule: {} - {} is bad. Infinite Loop".format(wc[0], wc[1])
        rules.update({wc[0]: wc[1]})

    # word
    for k in uword:
        if k in alphabet:
            continue
        else:
            return "Word have symbols which are not in alphabet"

    # algorithm
    token = list(rules.keys())
    token_k = list(rules.values())
    ind = 0
    wrd = uword
    while ind < len(token):
        if token[ind] in wrd:
            wrd = wrd.replace(str(token[ind]), str(token_k[ind]), 1)
            ind = 0
        else:
            ind += 1

    print("Alphabet: {}".format(alphabet))
    print("Rules: {}".format(rules))
    print("Executed u_word: ")
    return wrd


# runner (commented for running UnitTests, uncomment if you need)
# u_alphabet = input("alphabet: ")
# u_rules = input("rules (rule-ex rule-ex ...): ")
# u_word = input("word: ")
# print(markov(u_alphabet, u_rules, u_word))
