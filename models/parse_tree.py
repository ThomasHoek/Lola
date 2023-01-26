from nltk.ccg import chart, lexicon

string_symbols = "S, NP, N, PP"

# Collecting all rules from the parses #
def make_dict(data):
    dict_rules = {}
    new_data = data.split('\n')
    for item in new_data:
        x = item.strip()  # Removing the spaces at the beginning of the line.

        # Searching for lines that start with t (= terminal lines), containing the lexical rules
        if x.startswith('t'):

            # Extracting the word and its correspondig rule (+ cleaning up the data)
            y = x.split(", ")
            rule = (y[0].replace("t(", '')).upper()
            word = (y[1].replace("'", '')).lower()

            rule = rule.replace(":DCL", "")
            rule = rule.replace(":TO", "")
            rule = rule.replace(":ADJ", "")
            rule = rule.replace(":B", "")

            dict_rules[word] = rule

    print(dict_rules)
    return dict_rules


def make_lexicon(dict_rules):
    # CONSTRUCTING A LEXICON (out of the dict) #
    lexical_string = ""
    for item in dict_rules:
        x = dict_rules[item]
        rule_string = item + " => " + x
        lexical_string = lexical_string + rule_string + "\n"

        ccg_string = ":- " + string_symbols + "\n" + lexical_string

    return ccg_string


def generate_parse(sentence, ccg_string):
    # GENERATING CCG TREES # TOY example
    sentence = sentence.lower()

    # Creating lexicon
    x = lexicon.fromstring(ccg_string)

    # CCG derivations
    rules = chart.DefaultRuleSet
    parser = chart.CCGChartParser(x, rules)
    parses = list(parser.parse(sentence.split()))

    for parse in parses:
        return parse


def parse_tree(sentence, data):
    parse_lexicon = make_lexicon(make_dict(data))
    return generate_parse(sentence, parse_lexicon)


if __name__ == "__main__":
    data = r'''
ccg(84,
 ba(s:dcl,
  fa(np,
   t(np/n, 'Een', [lemma:'een']),
   t(n, 'man', [lemma:'man'])),
  fa(s:dcl\np,
   t((s:dcl\np)/pp, 'zit', [lemma:'zit']),
   fa(pp,
    t(pp/np, 'in', [lemma:'in']),
    fa(np,
     t(np/n, 'een', [lemma:'een']),
     t(n, 'veld', [lemma:'veld'])))))).
     ccg(263,
 ba(s:dcl,
  fa(np,
   t(np/n, 'Sommige', [lemma:'sommige']),
   t(n, 'mensen', [lemma:'mensen'])),
  t(s:dcl\np, 'lopen', [lemma:'lopen']))).
'''

    sentence = "Een man zit in een veld"
    sentence_2 = "Sommige mensen lopen"

    ccg_dict = make_dict(data)
    ccg_lexicon = make_lexicon(ccg_dict)
    print(generate_parse(sentence, ccg_lexicon))
    print(generate_parse(sentence_2, ccg_lexicon))
