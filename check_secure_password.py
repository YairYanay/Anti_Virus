import random
import string
import time

def benchmark_cracking_attempts(password_length, character_set):
    start_time = time.time()    
    seconds_to_run = 0.1
    attempts_made = 0

    while time.time() - start_time < seconds_to_run:
        password = ''.join(random.choice(character_set) for _ in range(password_length))
        attempts_made += 1

    return attempts_made / seconds_to_run

def calculate_time_cracking(password):
    attemps_per_second = benchmark_cracking_attempts(len(password), string.printable[:-2])
    combination = len(string.printable[:-2]) ** len(password) 

    return combination / attemps_per_second

creck_time_second = calculate_time_cracking(input("what is your password: "))
creck_time_minutes = creck_time_second / 60
creck_time_hours = creck_time_minutes / 60
creck_time_days = creck_time_hours / 24

print()
print(f"second: {creck_time_second}")
print(f"minutes: {creck_time_minutes}")
print(f"hours: {creck_time_hours}")
print(f"days: {creck_time_days}")