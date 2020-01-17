#C1alculate the distance of Voyager 1 from the Sun based on user input,
# report number of days as well as -distance in mi, -distance in km, -distance in AU,
# -round trip time for radio comm.

#get number of days from user and convert str to int
days = input("Enter number of days after 09/25/2009: ")
days = int(days)

#distance from the sun on 9/25/09 in miles
distance = 16637000000

#speed traveling away from sun
speed_traveling = 38241 #miles per hour

#number of hrs in 1 day
hrs_day = 24

#how many km per miles
km_p_mi = 1.609344

#how many miles per au
au_p_mi = 92955887.6

#how many miles per meter
mtr_p_mi = 0.000621371

#speed of light in meters per second
spd_light = 299792458


#a. distance in miles for 1 day
#distance in 1 day
dist_trvld_in_one_day = speed_traveling * hrs_day

#distance based on number of days input
tot_dist_mi = distance + (dist_trvld_in_one_day * days)
print(tot_dist_mi, "miles traveled in ", days, " days.")


#b. convert distance from mi to km
tot_dist_km = tot_dist_mi * km_p_mi
print(tot_dist_km, "kilomters traveled in ", days, " days.")


#c. convert distance from mi to au
tot_dist_au = tot_dist_mi / au_p_mi
print(tot_dist_au, "Astronomical units travled in ", days, " days.")

#d. calculate round trip radio comm time in hrs
rnd_trip_comm_hrs = (tot_dist_km * 2) / dist_trvld_in_one_day
# tot_dist_mi / (dist_trvld_in_one_day * 2)
print(rnd_trip_comm_hrs, "hours to complete round trip radio communication in ", days, " days.")



#it runs and gives me results but i'm not sure how to check if the results are correct...
#should i be checking the math by working it out on paper?