from threading import Timer
from colorama import Back
from os import get_terminal_size

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_emirp(n):
    if not is_prime(n):
        return False
    reversed_n = int(str(n)[::-1])
    return is_prime(reversed_n) and n != reversed_n

count = 0
emirps_discovered_sec = 0
emirps_discovered_last_sec = 0
total_emirps_found = 0
latest_emirp = 0
last_three_outcomes = [1, 1, 1]
suspended = False

def calculate_persec():
    global emirps_discovered_sec, emirps_discovered_last_sec, total_emirps_found, latest_emirp, last_three_outcomes, suspended
    local_var = emirps_discovered_sec
    local_var2 = emirps_discovered_last_sec

    if not suspended:
        if all(outcome == "0" for outcome in last_three_outcomes):
            print("\n" + Back.BLUE + "*** Terminal logging is facing an issue, calculations are still running ***" + Back.RESET)
            suspended = True
    elif suspended:
        if not all(outcome == "0" for outcome in last_three_outcomes):
            print(Back.LIGHTMAGENTA_EX + "*** Terminal logging is no longer facing an issue, calculations resume... ***" + Back.RESET + "\n")
            suspended = False

    if not suspended:
        if local_var > local_var2:
            local_var = str(local_var)
            total_emirps_str = str(total_emirps_found)
            latest_emirp_str = str(latest_emirp)
            print(Back.GREEN + local_var, "emirps discovered per second" + Back.RESET + " | Total emirps:", total_emirps_str + " | Latest emirp:", latest_emirp_str)
        elif local_var < local_var2:
            local_var = str(local_var)
            total_emirps_str = str(total_emirps_found)
            latest_emirp_str = str(latest_emirp)
            print(Back.RED + local_var, "emirps discovered per second" + Back.RESET + " | Total emirps:", total_emirps_str + " | Latest emirp:", latest_emirp_str)
        else:
            local_var = str(local_var)
            total_emirps_str = str(total_emirps_found)
            latest_emirp_str = str(latest_emirp)
            print(Back.YELLOW + local_var, "emirps discovered per second" + Back.RESET + " | Total emirps:", total_emirps_str + " | Latest emirp:", latest_emirp_str)

    if len(last_three_outcomes) == 3:
        last_three_outcomes.pop(0)
        local_var = str(local_var)
        last_three_outcomes.append(local_var)
        #print(last_three_outcomes)

    emirps_discovered_last_sec = emirps_discovered_sec
    emirps_discovered_sec = 0
    
    Timer(1.0, calculate_persec).start()

Timer(1.0, calculate_persec).start()

try:
    while True:
        if is_emirp(count):
            emirps_discovered_sec += 1
            total_emirps_found += 1
            latest_emirp = count
        count += 1
except KeyboardInterrupt:
    pass

print("Emirp discovery stopped.")
