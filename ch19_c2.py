# Initialize rabbit and fox populations
initial_rabbit_population = 50
initial_fox_population = 10

# Define model parameters
growth_rate = 0.05
interaction_coefficient = 0.0002

# Simulate population changes over 10 iterations
for iteration in range(10):
    # Calculate change in rabbit population
    change_rabbit = growth_rate * initial_rabbit_population - interaction_coefficient * initial_fox_population * initial_rabbit_population
    #change_rabbit = growth_rate * initial_rabbit_population
    
 # Update rabbit population based on the calculated change
    new_rabbit_population = initial_rabbit_population + change_rabbit
    
    # Display results for each iteration
    print(f"Iteration {iteration + 1}: Rabbit Population = {new_rabbit_population:.2f}")
    
    # Update initial rabbit population for the next iteration
    initial_rabbit_population = new_rabbit_population

# Output the final rabbit population
print(f"Final Rabbit Population: {new_rabbit_population:.2f}")
