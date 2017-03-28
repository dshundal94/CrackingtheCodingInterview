##Problem 1.9 String Rotation: Assume you have a method isSubstring which checks if one word is a 
#substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation
#of s1 using only one call to isSubstring. E.g. 'waterbottle' --> 'bottlewater' should return
# true. 

def isRotation(s1,s2):
	##check if the lengths are the same and if len > 0
	if (len(s1) == len(s2) & len(s1) > 0 & len(s2) > 0):
		arr = [s2,s2]
		s3 = "".join(arr)
		return isSubstring(s1,s3)
	return false
