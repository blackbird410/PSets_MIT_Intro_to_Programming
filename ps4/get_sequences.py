from copy import copy


def main():
    # Take a sequence from the user
    sequence = input("Enter a sequence of letter: ")

    # Recursively add the permutations of the string
    permutations = get_permutation(sequence)

    print(f"\n-----------\nNumber of permutations: {len(permutations)}\nPermutations: {permutations}\n----------\n")


def get_permutation(sequence):

    # Base case 
    if len(sequence) == 1:
        return list(sequence)
    else:
        # We hold the first letter of the sequence and sends the rest to the recursive function

        return permute(get_permutation(sequence[1:]), sequence[0]) 


def permute(sequence_list, letter):
    """Returns a list of all the permutation of a sequence of characters."""

    permutation_list = []
    # For each words in the sequence_list we will add the letter at all the positions in the sequence
    for word in sequence_list:
        length = len(word)
        
        # Include the letter at every position in the current sequence
        for i in range(length + 1):
            permutation_list.append(word[0:i] + letter + word[i:])

    return permutation_list


if __name__ == "__main__":
    main()
