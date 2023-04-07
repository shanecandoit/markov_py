
# markov
# https://en.wikipedia.org/wiki/Markov_algorithm

import json

rules = '''
A -> apple
B -> bag
S -> shop
T -> the
the shop -> my brother
a never used => terminating rule
'''

TERM_SYMBOL = '<:>'

sample = 'I bought a B of As from T S.'


def list_rules(rules: str) -> list:
    rules = rules.split('\n')
    rules = [rule.strip() for rule in rules if rule.strip()]
    return rules


def parse_rules(rules: list) -> dict:
    """ Turn a list of rules into a dictionary of rule pairs."""
    rules_dict = {}
    for rule in rules:
        if len(rule) < 3:
            continue

        # check for -> or =>
        # someone used => for terminating rule, nice
        key, value = None, None
        if '->' in rule:
            key, value = rule.split('->')
        elif '=>' in rule:
            key, value = rule.split('=>')
            value = TERM_SYMBOL + value.strip()
        else:
            continue

        key = key.strip()
        value = value.strip()
        rules_dict[key] = value

    return rules_dict


def markov(rules_map: dict, sample: str) -> str:
    """ Markov algorithm.
    https://en.wikipedia.org/wiki/Markov_algorithm
    """
    # rules = list_rules(rules)
    # rules_map = parse_rules(rules)
    steps = []

    previous = sample
    while True:
        # sample = markov(rules_map, sample)
        for rule in rules_map:
            if rule in sample:

                before = sample
                change = rules_map[rule]
                sample = sample.replace(rule, change)

                after = sample
                left, right = rule, change
                steps.append((before, after, left + ' -> ' + right))

                break
        # termination?
        if TERM_SYMBOL in sample:
            steps[-1] = (before, after, left + ' => ' + right)
            break
        # no change
        if sample == previous:
            break
        previous = sample

    print(f'steps {steps}')
    with open('steps.json', 'w') as f:
        json.dump(steps, f, indent=2)

    return sample


def save_rules(rules: list, filename: str):
    # rules = rules
    rule_pairs = [{k:v} for k,v in parse_rules(rules).items()]
    with open(filename, 'w') as f:
        json.dump(rule_pairs, f, indent=2)


if __name__ == '__main__':

    rules = list_rules(rules)
    print(f'rules {rules}')

    rules_map = parse_rules(rules)
    print(f'rules_map {rules_map}')

    # save sorted rules to a file
    save_rules(rules, 'rules.json')

    result = markov(rules_map, sample)
    print(f'result {result}')

''' 
DONE
we save the rules
remember to preserve the order

we save the steps

TODO

save the result
save hash of the rules
save hash of the steps
save hash of the result

allow to wrap tokens in a class
like a regex
:number :== [123456789][1234567890]*

that way we can do something like
:numer:1 + :number:2 -> add(:number:1, :number:2)

using something like backus naur form

DONT DO THIS
use regex instead
there should be a way to optimize this
so that we only try rules that are applicable

'''