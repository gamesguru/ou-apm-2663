#!/usr/bin/env python3

# NOTE: you should solve this through inclusion/exclusion. This is just to check.

_7nums = []
_13nums = []
_91nums = []

for i in range(1, 1000):
    if i % 7 == 0:
        _7nums.append(i)
    if i % 13 == 0:
        _13nums.append(i)

    if i % (7 * 13) == 0:
        _91nums.append(i)

print(f"Divisible by 7:       {len(_7nums)}")
print(f"Divisible by 13:      {len(_13nums)}")
print(f"Divisible by 7 * 13:  {len(_91nums)}")

print()
print("Now what...?")
print("Note these are exactly floor(999/x) where x=[7, 13, 91]")
