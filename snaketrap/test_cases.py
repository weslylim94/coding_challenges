import Game_Detector

# These tests used the same exact sample dictionary given in the prompt
sample_dict = {
    "CallOfDutyWW2": ["Call of duty world war two", "COD WW2", "COD WWII","WW2COD"],
    "Fortnite": ["Fortnite", "Fort Nite"],
    "Destiny": ["Destiny", "original Destiny game"],
    "Destiny2": ["Destiny 2", "the last Destiny game", "Destiny II"],
    "WorldOfWarcraft": ["WoW the game", "world of warcraft"]
}

# the test text is to account for every possible edge case
# sample text also verifies that the example in the prompt works
text0 = []
text1 = ['Destiny']
text2 = ['Destiny Fortnite']
text3 = ['WoW the game']
text4 = ['I only play WoW the game on weekends']
text5 = ['the last Destiny the last Destiny game']
text6 = ['I played the last Destiny game, WW2COD, and Fort Nite a lot.']

sample_text = ["I liked the last Destiny game, now I play Fortnite",
    "Lol, no comment about that",
    "I'm still playing world of warcraft since ww2"]


# DESCRIPTION:
#   runs assert tests by calling detect_game from Game_Detector.py
#   fails and gives AssertionError if tests fail
#   run_tests is called in Game_Detector.py
def run_tests():
	# TEST 0: empty list
	assert Game_Detector.detect_game(sample_dict, text0) == []
	# TEST 1: basic single word alias
	assert Game_Detector.detect_game(sample_dict, text1) == ['TAG{Destiny,Destiny}']
	# TEST 2: multiple basic single word aliases
	assert Game_Detector.detect_game(sample_dict, text2) == ['TAG{Destiny,Destiny} TAG{Fortnite,Fortnite}']
	# TEST 3: multi-word alias
	assert Game_Detector.detect_game(sample_dict, text3) == ['TAG{WorldOfWarcraft,WoW the game}']
	# TEST 4: non-alias words with multi-word and single-word aliases
	assert Game_Detector.detect_game(sample_dict, text4) == ['I only play TAG{WorldOfWarcraft,WoW the game} on weekends']
	# TEST 5: non-alias words with multi-word alias with another alias in it
	assert Game_Detector.detect_game(sample_dict, text5) == ['the last TAG{Destiny,Destiny} TAG{Destiny2,the last Destiny game}']
	# TEST 6: punctuation ignored when coupled with aliases [.,!?;]
	assert Game_Detector.detect_game(sample_dict, text6) == ['I played TAG{Destiny2,the last Destiny game}, TAG{CallOfDutyWW2,WW2COD}, and TAG{Fortnite,Fort Nite} a lot.']
	# TEST 7: given example on the prompt: multi string, multi-word and single-word aliases mixed with non-alias words, punctuation included.
	assert Game_Detector.detect_game(sample_dict, sample_text) == ['I liked TAG{Destiny2,the last Destiny game}, now I play TAG{Fortnite,Fortnite}', 'Lol, no comment about that', "I'm still playing TAG{WorldOfWarcraft,world of warcraft} since ww2"]

