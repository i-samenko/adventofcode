# part-1
ans = 0
with open("./input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        nums = []
        for ch in line:
            if ch.isdigit():
                nums.append(ch)
        ans += int(nums[0] + nums[-1])
print(ans)

# part-2
mapping = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"}

ans = 0
with open("./input.txt") as file:
    for line in file.readlines():
        line = line.strip()
        nums = []
        for i, ch in enumerate(line):
            if ch.isdigit():
                nums.append(ch)
            for key in mapping:
                if line[i:].startswith(key):
                    nums.append(mapping[key])
        ans += int(nums[0]+nums[-1])
print(ans)
