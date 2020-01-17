#convert/calculate information about gasoline and gasoline usage

#assign values to variables

#get user input for # of gals of gas
gal_gas = input("Enter number of gallons of gasoline: ")
#conver input from str to int becuase dealing with float later
gal_gas = float(gal_gas)

#liters per gallon
ltr_p_gal = 3.78541

#gals of gas per barrel of oil
oil_barrel = 19.5

#lbs of c02 produced per gal of gas
c02_produced = 20

#BTU energy per gal of gas
BTU_energy_gas = 115000

#BTU energy per gal of ethanol
BTU_energy_ethanol = 75700

#price of gas per gal
gas_price_p_gal = 3.00


#a. number of liters produced per gal_gas
liters_produced = gal_gas * ltr_p_gal
print(liters_produced, "Liters per ", gal_gas, " gallon(s) of gasoline.")


#b. number of barrels needed to produce gal_gas
barrels_needed = gal_gas / oil_barrel#19.5
print(barrels_needed, " barrels required to make ", gal_gas, "gallons of gasoline.")


#c. number of lbs of c02 produced from 1 gal gas
lbs_c02 = gal_gas * c02_produced
print(lbs_c02, " pounds of c02 produced from ", gal_gas, " gallon(s) of gasoline.")


#d. equivalent energy amnt of ethanol gals
eth_gal = BTU_energy_gas / BTU_energy_ethanol
print(eth_gal, " gallons of ethanol is the energy equivilant of ", gal_gas, "gallon(s) of gasonline")


#e. price of gal_gas
cost = gal_gas * gas_price_p_gal
print("The cost of ", gal_gas, " gallon(s) of gasoline is: ", cost)


#it runs and gives me results but i'm not sure how to check if the results are correct...
#should i be checking the math by working it out on paper?