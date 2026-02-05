import os

# ============================================================
# PART 1: RECURSION WARM UP
# (Function names may differ slightly in your template.
#  If yours are named differently, paste the *logic* inside.)
# ============================================================

def recursive_sum(nums):
    """Return the sum of a list of integers using recursion."""
    # Base case
    if len(nums) == 0:
        return 0
    # Recursive case
    return nums[0] + recursive_sum(nums[1:])


def recursive_count(nums):
    """Return the number of items in a list using recursion (no len())."""
    if nums == []:
        return 0
    return 1 + recursive_count(nums[1:])


def recursive_max(nums):
    """Return the max value in a non-empty list using recursion."""
    if len(nums) == 1:
        return nums[0]
    rest_max = recursive_max(nums[1:])
    return nums[0] if nums[0] > rest_max else rest_max


# ============================================================
# PART 2: COUNT ALL FILES
# ============================================================

def count_files(directory_path):
    """
    Recursively count all files in directory_path (including in subfolders).
    Returns an integer count.
    """
    total = 0

    # List entries in this directory
    try:
        entries = os.listdir(directory_path)
    except FileNotFoundError:
        return 0

    for name in entries:
        full_path = os.path.join(directory_path, name)

        if os.path.isfile(full_path):
            total += 1
        elif os.path.isdir(full_path):
            total += count_files(full_path)

    return total


# ============================================================
# PART 3: FIND INFECTED FILES
# ============================================================

def find_infected_files(directory_path, extension):
    """
    Recursively find all files ending with `extension` under directory_path.
    Returns a list of FULL file paths.
    """
    infected = []

    try:
        entries = os.listdir(directory_path)
    except FileNotFoundError:
        return infected

    for name in entries:
        full_path = os.path.join(directory_path, name)

        if os.path.isfile(full_path):
            if name.endswith(extension):
                infected.append(full_path)
        elif os.path.isdir(full_path):
            infected.extend(find_infected_files(full_path, extension))

    return infected


# ============================================================
# MAIN (Uncomment tests in your template)
# ============================================================

if __name__ == "__main__":
    # Warm-up quick tests (optional)
    # print(recursive_sum([1, 2, 3, 4]))     # 10
    # print(recursive_count([9, 8, 7]))      # 3
    # print(recursive_max([5, 1, 9, 2]))     # 9

    # Your template likely already has test cases to uncomment.
    pass
