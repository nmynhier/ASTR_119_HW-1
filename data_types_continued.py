#string

s = "i am a string."
print(type(s)) 			# say str

#boolean

yes = True
print(type(yes))		#boolean truw

no = False
print(type(no))			#boolean false

#list -- ordered and changeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))		#will say tuple
print(type(alpha_list[0]))	#will say string
alpha_list.append("d")		#will add "d" to the list end
print(alpha_list)		#will print list

#tuple -- ordered and unchangebale

alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))	#will say tuple

try:
	alpha_tuple[2] = "d"	#attemp the following line
except TypeError:		#wont work and will raise TypeError
	print("we cant add the elements to tuples!")	#print this message
print(alpha_tuple)		#will print tuple
