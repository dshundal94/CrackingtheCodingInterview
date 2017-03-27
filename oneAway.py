#Problem 1.5: There are three type of edits that can be peformed on strings: insert a character, 
# remove a character, or replace a character. Given two strings, write function to check if they
# are one edit (or zero edits) away

# checking to see if the second string can be one edit away from matching the first string
#the insertion and deletion of character are basically the same thing
def oneAway(str1, str2): 
	if len(str1) == len(str2):
		return oneEditReplace(str1, str2)
	elif len(str1) + 1 == len(str2):
		return oneEditInsert(str1, str2)
	elif len(str1) -1 == len(str2):
		return oneEditInsert(str2, str1)
	return false

##zip bounds the words together for example if str1 was "paco" and str2 was "taco", 
#then zip(str1, str2) would be ((p,t), (a,a), (c,c), (o, o)), each with it's own tuple
def oneEditReplace(str1, str2): 
	edited = False
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            if edited:
                return False
            edited = True
    return True

def oneEditInsert(str1, str2):
    edited = False
    i, j = 0, 0
    while i < len(str1) and j < len(str2):
    	#the will become false, when there are two edits at the minimum, if the
    	# characters don't mtch, then set edited to true, and move j along, if it doesn't match
    	#again, then we know there are more than two edits
        if str1[i] != str2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True