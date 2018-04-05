# NOTE: Help was obtained through Wikipedia and Stack Overflow as sources of consultation
# Other documentation for proofs and ideas are found in Documentation.pdf

import sys
import re
import test_cases

# sample_dict = {
#     "CallOfDutyWW2": ["Call of duty world war two", "COD WW2", "COD WWII","WW2COD"],
#     "Fortnite": ["Fortnite", "Fort Nite"],
#     "Destiny": ["Destiny", "original Destiny game"],
#     "Destiny2": ["Destiny 2", "the last Destiny game", "Destiny II"],
#     "WorldOfWarcraft": ["WoW the game", "world of warcraft"]
# }

# sample_text = ["I liked the last Destiny game, now I play Fortnite",
#     "Lol, no comment about that",
#     "I'm still playing world of warcraft since ww2"]

# PARAMETERS:
#   dict: dictionary with
#       key: Game Name
#       value: Game Alias
#   str_list: list of strings with text possibly containing Game Aliases
# DESCRIPTION:
#   reads through str_list and changes any Game Aliases to a tagged game
#   returns text with Game Aliases replaced with the Game ID
#   Ex: world of warcraft -> TAG{WorldOfWarcraft,world of warcraft}
def detect_game(dict, str_list):
    start = 0
    end = 0

    # goes through every string in str_list
    cur = 0
    for words in str_list:
        words = re.findall(r"[\w']+|[.,!?;]", words)

        # goes through every word in words
        for i in range(len(words)):

            # error checking
            if i > len(words) - 1:
                break

            # builds list of possible aliases for the current word
            alias_candidates = []
            for key in dict:
                for val in dict[key]:
                    if words[i] in val:
                        alias_candidates.append(val)
                start = i
                r = _detect_game(alias_candidates, words[i:], i)
                end = r[0]
                alias = r[1]

                # error chcking
                if start < end:
                    words[start] = 'TAG{' + key + ',' + alias + '}'
                    words = words[:start + 1] + words[end:]
        str_list[cur] = ' '.join(words).replace(" ,", ",") \
            .replace(" .", ".",) \
            .replace(" !", "!",) \
            .replace(" ?", "?",) \
            .replace(" ;", ";",)
        cur = cur + 1
    return str_list


# PARAMETERS:
#   list: list of possible aliases the current string can be
#   words: list of words in string that possibly containing Game Aliases
#   index: index of the current string in the string list; used to determine the end index
# DESCRIPTION:
#   helper function to detect_game(dict, str_list)
#   goes through the words in the string to see if there is an alias
#   possible alias matches are in list
#   returns ending index and the matched alias, returns (0, None) otherwise
def _detect_game(list, words, index):
    next = 0
    cur = ''
    for i in range(len(words)):

        # check current substring to see if it is an alias
        cur = ' '.join(words[:i + 1])
        for j in list:
            if cur not in j:
                if ' '.join(words[:(i)]) == j:
                    return (next + index, j)
        next = next + 1

    # finding if alias is valid if alias is the last word in string
    for k in list:
        if cur == k:
            return (next + index, k)
    return 0, None


 
# MAIN CODE RUNNING TESTS
if __name__ == "__main__":
    # print detect_game(sample_dict, sample_text)

    test_cases.run_tests()
    print "All the tests have been passed. See the tests ran in test_cases.py"