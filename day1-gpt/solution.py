# Open the file in read mode
with open("input", "r") as file:
    # Create a dictionary to store the total calories for each Elf
    elf_calories = {}
    
    # Set the current Elf to 1
    current_elf = 1
    
    # Read the file line by line
    for line in file:
        # If the line is blank, move on to the next Elf
        if line is "\n":
            current_elf += 1
        else:
            # Convert the line to an integer
            calories = int(line)
            
            # Add the calories to the current Elf's total
            if current_elf not in elf_calories:
                elf_calories[current_elf] = calories
            else:
                elf_calories[current_elf] += calories
    
    # Find the Elf with the most calories
    max_calories = 0
    max_elf = 0
    for elf, calories in elf_calories.items():
        if calories > max_calories:
            max_calories = calories
            max_elf = elf
    
    # Print the result
    print(f"Elf {max_elf} has the most calories: {max_calories}")