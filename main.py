
# Electricity Bill Calculator

# Function to calculate electricity cost
def units_cost(units):
    if units < 0:
        raise ValueError("Units cannot be negative")

    if units <= 100:
        return units * 3
    elif units <= 200:
        return (100 * 3) + ((units - 100) * 5)
    else:
        return (100 * 3) + (100 * 5) + ((units - 200) * 7)


# Function to calculate fixed charge
def fixed_charge():
    return 50


# Function to calculate total bill
def total_bill(units):
    return units_cost(units) + fixed_charge()


# New feature added in Phase 4
def is_high_consumption(units):
    return units > 300


# Main function
def main():
    print("===== ELECTRICITY BILL CALCULATOR =====")

    units = float(input("Enter electricity units consumed: "))

    if not units.is_integer():
        print("Please enter a whole number of units.")
        return

    units = int(units)

    print("Units Consumed:", units)
    print("Electricity Cost: Rs.", units_cost(units))
    print("Fixed Charge: Rs.", fixed_charge())
    print("Total Electricity Bill: Rs.", total_bill(units))
    print("High Consumption:", is_high_consumption(units))


# Main program execution
if __name__ == "__main__":
    main()
