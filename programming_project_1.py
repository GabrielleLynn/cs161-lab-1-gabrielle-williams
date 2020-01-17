#Calcualte how deep it would be if all the water from the great lakes was evenly spread over the 48 contiguous U.S. states

#name variables assign values accordingly
lake_vol = 22810
surface_area = 2959064.44

#divide volume by area assign result to depth
#depth result in km
depth = lake_vol / surface_area

#convert depth in km to depth in ft
depth = depth * 3280.8 #ft = km*3280.8

#display answer
print("if all the water from the great lakes was evenly spread over the 48 contiguous U.S. states, the water would be: ", depth, "feet deep")



#i dont feel like the math is right...
#when i looked for the depth online to see if i was right my result did not match
#not sure what im missing here, could you go over this one in class?