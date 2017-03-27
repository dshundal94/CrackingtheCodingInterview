#Problem 1.6 String Compression: Implement a method to perform basica string compression using 
# counts of repeated characters. E.g. the string "aabccccaaa" would become :a2b1c4a3. If compressed
# string would not become smaller than original string, then return original. 

def string_compression(string):
    compressed = []
    counter = 0

    for i in range(len(string)):
        if i != 0 and string[i] != string[i - 1]:
            compressed.append(string[i - 1] + str(counter))
            counter = 0
        counter += 1

    # add last repeated character
    compressed.append(string[-1] + str(counter))

    # returns original string if compressed string isn't smaller
    return min(string, ''.join(compressed), key=len)