def get_common_elements(a1, a2):
    commons = []
    i = 0
    j = 0
    while i < len(a1) and j < len(a2):
        a1_value = a1[i]
        a2_value = a2[j]
        if a1_value == a2_value:
            # Keep a unique list of common items
            if not commons or commons[-1] != a1_value:
                commons.append(a1[i])
            i += 1
            j += 1
            continue

        # Increment only the side you want to continue on
        if a1_value > a2_value:
            j += 1
        else:
            i += 1

    return commons
