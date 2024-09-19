def calculate_budget(total_amount):
    # Define ratios
    essentials_ratio = 0.45
    leisure_ratio = 0.15
    savings_ratio = 0.10
    growth_ratio = 0.30
    
    # Essentials breakdown
    rent_ratio = 0.50
    food_and_groceries_ratio = 0.30
    bills_and_utilities_ratio = 0.20
    
    # Leisure breakdown
    entertainment_ratio = 0.50
    dining_out_ratio = 0.20
    cannabis_ratio = 0.20
    other_leisure_ratio = 0.10
    
    # Savings breakdown
    emergency_fund_ratio = 0.50
    debt_repayment_ratio = 0.30
    short_term_savings_ratio = 0.20
    
    # Growth breakdown
    education_and_learning_ratio = 0.50
    personal_projects_ratio = 0.20
    tools_and_resources_ratio = 0.20
    items_ratio = 0.10
    clothing_ratio = 0.10  # Moved Clothing to Growth

    # Calculate amounts
    essentials = total_amount * essentials_ratio
    leisure = total_amount * leisure_ratio
    savings = total_amount * savings_ratio
    growth = total_amount * growth_ratio

    rent = essentials * rent_ratio
    food_and_groceries = essentials * food_and_groceries_ratio
    bills_and_utilities = essentials * bills_and_utilities_ratio
    
    entertainment = leisure * entertainment_ratio
    dining_out = leisure * dining_out_ratio
    cannabis = leisure * cannabis_ratio
    other_leisure = leisure * other_leisure_ratio
    
    emergency_fund = savings * emergency_fund_ratio
    debt_repayment = savings * debt_repayment_ratio
    short_term_savings = savings * short_term_savings_ratio
    
    education_and_learning = growth * education_and_learning_ratio
    personal_projects = growth * personal_projects_ratio
    tools_and_resources = growth * tools_and_resources_ratio
    items = growth * items_ratio
    clothing = growth * clothing_ratio  # Adjusted Clothing allocation
    
    # Output results
    print(f"Total Budget: KES {total_amount:.2f}\n")
    print("Essentials:")
    print(f"  Rent: KES {rent:.2f}")
    print(f"  Food & Groceries: KES {food_and_groceries:.2f}")
    print(f"  Bills & Utilities: KES {bills_and_utilities:.2f}\n")
    
    print("Leisure:")
    print(f"  Entertainment: KES {entertainment:.2f}")
    print(f"  Dining Out: KES {dining_out:.2f}")
    print(f"  Cannabis: KES {cannabis:.2f}")
    print(f"  Other Leisure: KES {other_leisure:.2f}\n")
    
    print("Savings:")
    print(f"  Emergency Fund: KES {emergency_fund:.2f}")
    print(f"  Debt Repayment: KES {debt_repayment:.2f}")
    print(f"  Short-Term Savings: KES {short_term_savings:.2f}\n")
    
    print("Growth:")
    print(f"  Education & Learning: KES {education_and_learning:.2f}")
    print(f"  Personal Projects: KES {personal_projects:.2f}")
    print(f"  Tools & Resources: KES {tools_and_resources:.2f}")
    print(f"  Items (e.g., headphones): KES {items:.2f}")
    print(f"  Clothing: KES {clothing:.2f}\n")

# Input section
try:
    total_budget = float(input("Enter your total monthly budget in KES: "))
    if total_budget < 0:
        raise ValueError("The budget amount should be positive.")
    calculate_budget(total_budget)
except ValueError as e:
    print(f"Invalid input: {e}")