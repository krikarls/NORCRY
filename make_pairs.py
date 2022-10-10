import numpy as np
import pandas as pd
import random

round = input("\nWhich round is it? (1, 2 or 3)\n")

# Read score sheet
data = pd.read_csv("NORCRY-2022-Q3-results.csv", sep = ",", engine = 'python')

# Print current score board
print("\nCurrent score board:")
print(data.to_string(index=False))

# Extract relevant data
names = list(data["Player name"])
scores = list(data["Total pts"])

# Number of whole pairs
num_pairs = int(np.floor(len(names)/2.0))

# Random pairing
if round == "1":
    print("Hei")
    # Draw random names and tables
    random_name_idx = random.sample(range(0, len(names)), len(names))
    random_table_numbers = random.sample(range(1, num_pairs+1), num_pairs)

    # Print random pairs
    print("\nMatches:")
    for i in range(0,num_pairs):
        idx1 = random_name_idx[i*2]
        idx2 = random_name_idx[i*2 +1]
        print(names[idx1],"vs",names[idx2]," @  table",random_table_numbers[i])

# Score-based pairing
else:
    # Sort players by total score and draw random table
    sorted_idx = np.argsort(np.array(scores))[::-1]
    random_table_numbers = random.sample(range(1, num_pairs+1), num_pairs)

    # Print score-based pairs
    print("\nMatches:")
    for i in range(0,num_pairs):
        idx1 = sorted_idx[i*2]
        idx2 = sorted_idx[i*2 +1]
        print(names[idx1],"vs",names[idx2]," @  table",random_table_numbers[i])

# Check if there is an odd number of players
if (len(names) % 2) is not 0:
    rnd_idx = random.randint(0, len(names)-1)
    print("\nThere is an odd number of players.")
    print(f"May I suggest that {names[rnd_idx]} skips this round?\n")
