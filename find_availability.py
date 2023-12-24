def find_common(availability_lists):
    if not availability_lists:
        return [], []

    # Convert each person's availability into sets of days
    availability_sets = [set(availability) for availability in availability_lists]

    common_availability = availability_sets[0]
    for availability_set in availability_sets[1:]:
        common_availability = common_availability.intersection(availability_set)

    most_matching_availability = availability_sets[0]
    most_matching_count = len(availability_sets[0])

    for availability_set in availability_sets[1:]:
        overlap = availability_set.intersection(common_availability)
        if len(overlap) > most_matching_count:
            most_matching_availability = availability_set
            most_matching_count = len(overlap)

    return sorted(list(common_availability)), sorted(list(most_matching_availability))

available_days = [
    [16, 17, 19, 20, 23, 24, 25, 26, 27, 30],
    [20, 23, 25, 26, 27, 30, 31],
    [16, 17, 28, 29, 30, 31],
    [17, 18, 19, 25]
]

common_days, most_matching_days = find_common(available_days)

if common_days or most_matching_days:
    print("Common availability for all people:", common_days)
    print("Availability that matches the most people:", most_matching_days)
else:
    print("No common availability found for any people.")
