###################################################################################
#                             top n most frequent phrases                         #
###################################################################################

from collections import Counter
from pathlib import Path

def top_phrases(input_file_name, top_n = 3):
	#verify input file path
	if not Path(input_file_name).exists():
		raise FileNotFoundError("You need to provide correct path of input file")

	phrases = Counter()

	with open(input_file_name) as input_file:
		for line in input_file:
			line = line.rstrip()    #remove new line character at the end of each row
			phrases += Counter(line.lower().split("|"))

	#convert most frequent phrases tuple to dictionary
	top_n_phrases = dict(phrases.most_common(top_n))
	return top_n_phrases


if __name__ == "__main__":
	input_file_name = "../../phrases.txt"    #large input file path
	top_n = 100000

	print(top_phrases(input_file_name, top_n))