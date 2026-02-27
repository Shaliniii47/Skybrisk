#  Create a basic data processing script (e.g., calculating the average temperature).
# Get the number of temperature you want to rwad
n = int(input("Enter the number of temperature "))   

# collect all temperature
Temperatures = []
for i in range(n):
    temp = float(input(f"Enter the temperature {i + 1}:"))
    Temperatures.append(temp)

# Process the data
Avg_temp = sum(Temperatures) / n

# display the result
print(f"Average temprature of the week is : {Avg_temp:.2f}°C")