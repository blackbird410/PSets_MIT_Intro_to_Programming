# Problem Set 4A
# Name: Neil Taison RIGAUD
# Collaborators: None
# Time Spent: 0:50 minutes 

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''

    # Base case 
    if len(sequence) == 1:
        return list(sequence)
    else:
        permutation_list = []
        # We hold the first letter of the sequence and sends the rest to the recursive function
        letter = sequence[0]
        sequence_list = get_permutations(sequence[1:]) 

        # For each words in the sequence_list we will add the letter at all the positions in the sequence
        for word in sequence_list:
            length = len(word)
            
            # Include the letter at every position in the current sequence
            for i in range(length + 1):
                permutation_list.append(word[0:i] + letter + word[i:])
        
        return permutation_list
    


if __name__ == '__main__':
   #EXAMPLE
   example_input = 'abc'
   print('Input:', example_input)
   print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
   print('Actual Output:', get_permutations(example_input))
   
   assert get_permutations("abc") == ["abc", "bac", "bca", "acb", "cab", "cba"]
   assert get_permutations("bush") == ['bush', 'ubsh', 'usbh', 'ushb', 'bsuh', 'sbuh', 'subh', 'suhb', 'bshu', 'sbhu', 'shbu', 'shub', 'buhs', 'ubhs', 'uhbs', 'uhsb', 'bhus', 'hbus', 'hubs', 'husb', 'bhsu', 'hbsu', 'hsbu', 'hsub']
   assert get_permutations("idiot") == ['idiot', 'diiot', 'diiot', 'dioit', 'dioti', 'iidot', 'iidot', 'idiot', 'idoit', 'idoti', 'iiodt', 'iiodt', 'ioidt', 'iodit', 'iodti', 'iiotd', 'iiotd', 'ioitd', 'iotid', 'iotdi', 'idoit', 'dioit', 'doiit', 'doiit', 'doiti', 'iodit', 'oidit', 'odiit', 'odiit', 'oditi', 'ioidt', 'oiidt', 'oiidt', 'oidit', 'oidti', 'ioitd', 'oiitd', 'oiitd', 'oitid', 'oitdi', 'idoti', 'dioti', 'doiti', 'dotii', 'dotii', 'iodti', 'oidti', 'oditi', 'odtii', 'odtii', 'iotdi', 'oitdi', 'otidi', 'otdii', 'otdii', 'iotid', 'oitid', 'otiid', 'otiid', 
'otidi', 'idito', 'diito', 'diito', 'ditio', 'ditoi', 'iidto', 'iidto', 'idito', 'idtio', 'idtoi', 'iitdo', 'iitdo', 'itido', 'itdio', 'itdoi', 'iitod', 'iitod', 'itiod', 'itoid', 'itodi', 'idtio', 'ditio', 'dtiio', 'dtiio', 'dtioi', 'itdio', 'tidio', 'tdiio', 'tdiio', 'tdioi', 'itido', 'tiido', 'tiido', 'tidio', 'tidoi', 'itiod', 'tiiod', 'tiiod', 'tioid', 'tiodi', 'idtoi', 'ditoi', 'dtioi', 'dtoii', 'dtoii', 'itdoi', 'tidoi', 'tdioi', 'tdoii', 'tdoii', 'itodi', 'tiodi', 'toidi', 'todii', 'todii', 'itoid', 'tioid', 'toiid', 'toiid', 'toidi']

