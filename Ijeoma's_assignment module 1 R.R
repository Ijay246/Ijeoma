# Create a vector containing 500 names using a sequence
names <- paste0("Employee_", 1:500)

# Generating random worker data - gender and salary using a function
generate_data <- function() {
  # Randomly select a gender
  gender <- sample(c("Female", "Male"), 1)
  
  # Generate a random salary between $6000 and $32000
  salary <- sample(6000:32000, 1)
  
  # Create a list containing name, gender, and salary
  list(
    name = sample(names, 1),
    gender = gender,
    salary = salary
  )
}

# Save the result of the function in a vector named employees, containing information for 500 workers
employees <- replicate(500, generate_data(), simplify = FALSE)

# CREATING PAYMENT SLIPS
payment_slips <- list()  # Create an empty list to store payment slips

#Error handling and generating slips
tryCatch({
  # Loop through each employee to generate a payment slip
  for (i in seq_along(employees)) {
    employee <- employees[[i]]
    
    # Create an empty list for the payment slip
    payment_slip <- list()
    payment_slip$name <- employee$name
    payment_slip$salary <- employee$salary
    
    # Conditional statements to assign employee levels
    if (employee$salary > 10000 && employee$salary < 20000) {
      payment_slip$level <- "A1"
    }
    if (employee$salary > 7500 && employee$salary < 30000 && employee$gender == "Female") {
      payment_slip$level <- "A5-F"
    }
    
    # Append each slip to the payment_slips list
    payment_slips[[i]] <- payment_slip
  }
}, error = function(e) {
  # Print error message if there's an issue
  print(paste("An error occurred:", e))
})

# View employees and their payment slips
print(employees)
cat("\n\n\n") #Create 3 new lines
print(payment_slips)

# Why Some Workers Might Not Get Assigned Levels:
# *Salary Range:
 
# Workers with salaries less than or equal to $10,000 or greater than or equal to $20,000 
# do not meet the first condition.

# Workers with salaries less than or equal to $7,500 or greater than or equal to $30,000 
# do not meet the second condition.

# *Gender Requirement:

# The second condition only applies to female workers. 
# Male workers with salaries between $7,500 and $30,000 do not meet the A5-F level 
#condition.