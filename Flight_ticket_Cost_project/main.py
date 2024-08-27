def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost = 0
    # Write your logic here
    ticket_for_adult = no_of_adults * 37550  # 1,87,750
    ticket_for_child = no_of_children * 37550 / 3  # 25,033
    ticket_of_both = ticket_for_adult + ticket_for_child  # 2,12,783

    service = ticket_of_both * 7 / 100  # 14,894
    include_service = ticket_of_both + service
    discount = include_service * 10 / 100  # 22,767
    total_ticket_cost = include_service - discount

    return total_ticket_cost


# Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost = calculate_total_ticket_cost(5, 2)
print("Total Ticket Cost:", total_ticket_cost)
