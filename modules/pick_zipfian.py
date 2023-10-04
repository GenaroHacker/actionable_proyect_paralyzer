
import random

def pick_zipfian(strings):
    # Calculate the total sum for normalization (The Harmonic series sum)
    total = sum(1/n for n in range(1, len(strings) + 1))
    
    # Generate a random number between 0 and the total sum
    rand_num = random.uniform(0, total)
    
    # Initialize a running sum
    running_sum = 0
    
    # Loop through the list to find the selected item
    for i, string in enumerate(strings, start=1):
        running_sum += 1/i
        if running_sum >= rand_num:
            return string

if __name__ == "__main__":
    # Test the function with a list of strings
    strings = ["apple", "banana", "cherry", "date", "elderberry"]
    print(pick_zipfian(strings))
