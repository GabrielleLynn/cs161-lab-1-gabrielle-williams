#calculate population based on number of years given by user input

#name variables and assign values
#get number of years
years = input("Enter number of years to see estimated population: ")
years = int(years)

#1 births every 7 seconds
births = 7

#1 death every 13 seconds
deaths = 13

#1 new immigrant every 35 seconds
immigrants = 35

#number of seconds in 1 day
sec_p_day = 86400

#number of days in 1 year
day_p_year = 365

#current population
cur_pop = 307357870


#births per year
birth_p_year = (sec_p_day / births) * day_p_year


#deaths per year
death_per_year = (sec_p_day / deaths) * day_p_year


#new immigrants per year
immigrant_p_year = (sec_p_day / immigrants) * day_p_year


#population fluxuation per year
pop_flux_p_year = births + immigrants - deaths


#calculate and print population based on user input
pop = (pop_flux_p_year * years) + cur_pop
print(pop)



#it runs and gives me results but i'm not sure how to check if the results are correct...
#should i be checking the math by working it out on paper?