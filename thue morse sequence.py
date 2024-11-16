# 1st term = 0
# Take current terms in Thue Morse sequence & switch each 0 to 1 and 1 to 0
# Append new terms to the existing sequence
#
# for e.g
# step 1 : 2nd term = 1 and sequence = 0 1
# Step 2: next terms = 1 0 and sequence = 0 1 1 0
# Step 3: next terms = 1 0 0 1 and sequence = 0 1 1 0 1 0 0 1
# and so on...

import sys
import time
start = time.time()
thue_morse_sequence = [0]
new_terms = []
for step in range(1,21):
	for term in thue_morse_sequence:
		next_term = (0 if term == 1 else 1)
		new_terms.append(next_term)
	thue_morse_sequence.extend(new_terms)
	new_terms = []
end = time.time()
#print(thue_morse_sequence)
print(end-start)
