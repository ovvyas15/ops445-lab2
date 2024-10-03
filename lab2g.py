#!/usr/bin/env python3

# Author: Om Vyas
# Author ID: ovvyas.ops445.ca
# Date Created: 2024/09/25

import sys


# Check if an argument was provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

# Loop until the timer reaches 0
while timer > 0:
    print(timer)
    timer -= 1

# Print 'blast off!' once the loop ends
print('blast off!')

