# ---
# jupyter:
#   jupytext:
#     hide_notebook_metadata: true
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Advent of Code 2020
#
# ## Table of Contents
#
# * [Day 1: Report Repair](#day-1-report-repair)
# * [Day 2: Password Philosophy](#day-2-password-philosophy)
# * [Day 3: Toboggan Trajectory](#day-3-toboggan-trajectory)
# * [Day 4: Passport Processing](#day-4-passport-processing)
# * [Day 15: Rambunctious Recitation](#day-15-rambunctious-recitation)

# %% [markdown]
# ## Day 1: Report Repair
#
# After saving Christmas [five years in a row](https://adventofcode.com/events), you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.
#
# The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them **stars**. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.
#
# To save your vacation, you need to get all **fifty stars** by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants **one star**. Good luck!
#
# Before you leave, the Elves in accounting just need you to fix your **expense report** (your puzzle input); apparently, something isn't quite adding up.
#
# Specifically, they need you to **find the two entries that sum to** `2020` and then multiply those two numbers together.
#
# For example, suppose your expense report contained the following:
#
#     1721
#     979
#     366
#     299
#     675
#     1456
#
# In this list, the two entries that sum to `2020` are `1721` and `299`. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is `514579`.
#
# Of course, your expense report is much larger. **Find the two entries that sum to `2020`; what do you get if you multiply them together?**
#
# Your puzzle answer was `224436`.

# %%
input = [1721, 979, 366, 299, 675, 1456]

# %%
input = open('input.1.txt', 'r').readlines()
input = [int(x) for x in input]

# %%
for i in input:
    j = 2020 - i
    if j in input:
        print("%d * %d = %d" % (i, j, i * j))

# %% [markdown]
# ### Part Two
#
# The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find **three** numbers in your expense report that meet the same criteria.
#
# Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`. Multiplying them together produces the answer, **`241861950`.**
#
# In your expense report, **what is the product of the three entries that sum to `2020`?**
#
# Your puzzle answer was `303394260`.

# %%
for i in input:
    for j in input:
        k = 2020 - i - j
        if k in input:
            print("%d * %d * %d = %d" % (i, j, k, i * j * k))

# %% [markdown]
# ## Day 2: Password Philosophy
#
# Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via [toboggan](https://en.wikipedia.org/wiki/Toboggan).
#
# The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.
#
# Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.
#
# To try to debug the problem, they have created a list (your puzzle input) of **passwords** (according to the corrupted database) and the **corporate policy when that password was set**.
#
# For example, suppose you have the following list:
#
#     1-3 a: abcde
#     1-3 b: cdefg
#     2-9 c: ccccccccc
#
# Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, `1-3 a` means that the password must contain `a` at least `1` time and at most `3` times.
#
# In the above example, `2` passwords are valid. The middle password, `cdefg`, is not; it contains no instances of `b`, but needs at least `1`. The first and third passwords are valid: they contain one `a` or nine `c`, both within the limits of their respective policies.
#
# **How many passwords are valid** according to their policies?
#
# Your puzzle answer was `556`.

# %%
input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

# %%
input = open('input.2.txt', 'r').readlines()
input = [i.strip() for i in input]

# %%
import numpy as np
import re

REGEX = re.compile("(.*)-(.*) (.*): (.*)")

def valid(input_line):
    p_min, p_max, p, s = REGEX.match(input_line).groups()
    return int(p_min) <= s.count(p) <= int(p_max)

np.sum([valid(i) for i in input])


# %% [markdown]
# ### Part Two
#
# While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.
#
# The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.
#
# Each policy actually describes two **positions in the password**, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) **Exactly one of these positions** must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
# Given the same example list from above:
#
# * `1-3 a: abcde` is **valid**: position `1` contains `a` and position `3` does not.
# * `1-3 b: cdefg` is **invalid**: neither position `1` nor position `3` contains `b`.
# * `2-9 c: ccccccccc` is **invalid**: both position `2` and position `9` contain `c`.
#
# **How many passwords are valid** according to the new interpretation of the policies?
#
# Your puzzle answer was `605`.

# %%
def valid2(input_line):
    i, j, p, s = REGEX.match(input_line).groups()
    return (s[int(i) - 1] == p) != (s[int(j) - 1] == p)

np.sum([valid2(i) for i in input])

# %% [markdown]
# ## Day 3: Toboggan Trajectory
#
# With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.
#
# Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (`.`) and trees (`#`) you can see. For example:
#
#     ..##.......
#     #...#...#..
#     .#....#..#.
#     ..#.#...#.#
#     .#...##..#.
#     ..#.##.....
#     .#.#.#....#
#     .#........#
#     #.##...#...
#     #...##....#
#     .#..#...#.#
#
# These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:
#
#     ..##.........##.........##.........##.........##.........##.......  --->
#     #...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#     .#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#     ..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#     .#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#     ..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
#     .#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#     .#........#.#........#.#........#.#........#.#........#.#........#
#     #.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#     #...##....##...##....##...##....##...##....##...##....##...##....#
#     .#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# You start on the open square (`.`) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).
#
# The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by **counting all the trees** you would encounter for the slope **right 3, down 1**:
#
# From your starting position at the top-left, check the position that is right `3` and down `1`. Then, check the position that is right `3` and down `1` from there, and so on until you go past the bottom of the map.
#
# The locations you'd check in the above example are marked here with `O` where there was an open square and `X` where there was a tree:
#
#     ..##.........##.........##.........##.........##.........##.......  --->
#     #..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
#     .#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
#     ..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
#     .#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
#     ..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
#     .#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
#     .#........#.#........X.#........#.#........#.#........#.#........#
#     #.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#     #...##....##...##....##...#X....##...##....##...##....##...##....#
#     .#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
#
# In this example, traversing the map using this slope would cause you to encounter `7` trees.
#
# Starting at the top-left corner of your map and following a slope of right `3` and down `1`, **how many trees would you encounter?**

# %%
input = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]

# %%
input = open('input.3.txt', 'r').readlines()
input = [i.strip() for i in input]


# %%
def is_tree(x, y):
    line = input[y]
    return line[x % len(line)] == '#'

trees = 0

for i in range(len(input)):
    if is_tree(3 * i, i):
        trees += 1

trees


# %% [markdown]
# ### Part Two
#
# Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.
#
# Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:
#
# * Right 1, down 1.
# * Right 3, down 1. (This is the slope you already checked.)
# * Right 5, down 1.
# * Right 7, down 1.
# * Right 1, down 2.
#
# In the above example, these slopes would find `2`, `7`, `3`, `4`, and `2` tree(s) respectively; multiplied together, these produce the answer **`336`**.
#
# **What do you get if you multiply together the number of trees encountered on each of the listed slopes?**
#
# Your puzzle answer was `2122848000`.

# %%
def num_trees(v_x, v_y):
    x = 0
    y = 0
    trees = 0
    while y < len(input):
        trees += is_tree(x, y)
        x += v_x
        y += v_y
    return trees

num_trees(3, 1)

# %%
speeds = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

np.prod([num_trees(*s) for s in speeds])

# %% [markdown]
# ## Day 4: Passport Processing
#
# You arrive at the airport only to realize that you grabbed your North Pole Credentials instead of your passport. While these documents are extremely similar, North Pole Credentials aren't issued by a country and therefore aren't actually valid documentation for travel in most of the world.
#
# It seems like you're not the only one having problems, though; a very long line has formed for the automatic passport scanners, and the delay could upset your travel itinerary.
#
# Due to some questionable network security, you realize you might be able to solve both of these problems at the same time.
#
# The automatic passport scanners are slow because they're having trouble **detecting which passports have all required fields**. The expected fields are as follows:
#
# * `byr` (Birth Year)
# * `iyr` (Issue Year)
# * `eyr` (Expiration Year)
# * `hgt` (Height)
# * `hcl` (Hair Color)
# * `ecl` (Eye Color)
# * `pid` (Passport ID)
# * `cid` (Country ID)
#
# Passport data is validated in batch files (your puzzle input). Each passport is represented as a sequence of `key:value` pairs separated by spaces or newlines. Passports are separated by blank lines.
#
# Here is an example batch file containing four passports:
#
#     ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
#     byr:1937 iyr:2017 cid:147 hgt:183cm
#
#     iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
#     hcl:#cfa07d byr:1929
#
#     hcl:#ae17e1 iyr:2013
#     eyr:2024
#     ecl:brn pid:760753108 byr:1931
#     hgt:179cm
#
#     hcl:#cfa07d eyr:2025 pid:166559648
#     iyr:2011 ecl:brn hgt:59in
#
# The first passport is **valid** - all eight fields are present. The second passport is **invalid** - it is missing `hgt` (the Height field).
#
# The third passport is interesting; the **only missing field** is `cid`, so it looks like data from North Pole Credentials, not a passport at all! Surely, nobody would mind if you made the system temporarily ignore missing `cid` fields. Treat this "passport" as **valid**.
#
# The fourth passport is missing two fields, `cid` and `byr`. Missing `cid` is fine, but missing any other field is not, so this passport is **invalid**.
#
# According to the above rules, your improved system would report **`2`** valid passports.
#
# Count the number of **valid** passports - those that have all required fields. Treat `cid` as optional. **In your batch file, how many passports are valid?**
#
# Your puzzle answer was `219`.

# %%
input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

# %%
input = open('input.4.txt', 'r').read()

# %%
passports = [{kv.split(":")[0]: kv.split(":")[1] for kv in p.split()} for p in input.split("\n\n")]

required = ['hcl', 'iyr', 'eyr', 'ecl', 'pid', 'byr', 'hgt']

len([p for p in passports if set(p.keys()).issuperset(required)])

# %% [markdown]
# ### Part Two
# The line is moving more quickly now, but you overhear airport security talking about how passports with invalid data are getting through. Better add some data validation, quick!
#
# You can continue to ignore the cid field, but each other field has strict rules about what values are valid for automatic validation:
#
# * `byr` (Birth Year) - four digits; at least `1920` and at most `2002`.
# * `iyr` (Issue Year) - four digits; at least `2010` and at most `2020`.
# * `eyr` (Expiration Year) - four digits; at least `2020` and at most `2030`.
# * `hgt` (Height) - a number followed by either `cm` or `in`:
#     * If cm, the number must be at least `150` and at most `193`.
#     * If in, the number must be at least `59` and at most `76`.
# * `hcl` (Hair Color) - a `#` followed by exactly six characters `0`-`9` or `a`-`f`.
# * `ecl` (Eye Color) - exactly one of: `amb` `blu` `brn` `gry` `grn` `hzl` `oth`.
# * `pid` (Passport ID) - a nine-digit number, including leading zeroes.
# * `cid` (Country ID) - ignored, missing or not.
#
# Your job is to count the passports where all required fields are both present and valid according to the above rules. Here are some example values:
#
#     byr valid:   2002
#     byr invalid: 2003
#
#     hgt valid:   60in
#     hgt valid:   190cm
#     hgt invalid: 190in
#     hgt invalid: 190
#
#     hcl valid:   #123abc
#     hcl invalid: #123abz
#     hcl invalid: 123abc
#
#     ecl valid:   brn
#     ecl invalid: wat
#
#     pid valid:   000000001
#     pid invalid: 0123456789
#
# Here are some invalid passports:
#
#     eyr:1972 cid:100
#     hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926
#
#     iyr:2019
#     hcl:#602927 eyr:1967 hgt:170cm
#     ecl:grn pid:012533040 byr:1946
#
#     hcl:dab227 iyr:2012
#     ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277
#
#     hgt:59cm ecl:zzz
#     eyr:2038 hcl:74454a iyr:2023
#     pid:3556412378 byr:2007
#
# Here are some valid passports:
#
#     pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
#     hcl:#623a2f
#
#     eyr:2029 ecl:blu cid:129 byr:1989
#     iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm
#
#     hcl:#888785
#     hgt:164cm byr:2001 iyr:2015 cid:88
#     pid:545766238 ecl:hzl
#     eyr:2022
#
#     iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
#
# Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
#
# Your puzzle answer was `127`.

# %%
input = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

# %%
input = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

# %%
input = open('input.4.txt', 'r').read()


# %%
def valid(passport):
    if "byr" not in passport: return False
    if not passport["byr"].isnumeric(): return False
    if not 1920 <= int(passport["byr"]) <= 2002: return False

    if "iyr" not in passport: return False
    if not passport["iyr"].isnumeric(): return False
    if not 2010 <= int(passport["iyr"]) <= 2020: return False

    if "eyr" not in passport: return False
    if not passport["eyr"].isnumeric(): return False
    if not 2020 <= int(passport["eyr"]) <= 2030: return False

    if "hgt" not in passport: return False
    if passport["hgt"][-2:] == 'cm':
        if not 150 <= int(passport["hgt"][:-2]) <= 193: return False
    elif passport["hgt"][-2:] == 'in':
        if not 59 <= int(passport["hgt"][:-2]) <= 76: return False
    else:
        return False

    if "hcl" not in passport: return False
    if not re.search(r'^#(?:[0-9a-f]{3}){1,2}$', passport["hcl"]): return False

    if "ecl" not in passport: return False
    if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]: return False

    if "pid" not in passport: return False
    if not re.search(r'^\d{9}$', passport["pid"]): return False

    return True

passports = [{kv.split(":")[0]: kv.split(":")[1] for kv in p.split()} for p in input.split("\n\n")]
np.sum([1 if valid(p) else 0 for p in passports])

# %% [markdown]
# ## Day 15: Rambunctious Recitation
#
# You catch the airport shuttle and try to book a new flight to your vacation island. Due to the storm, all direct flights have been cancelled, but a route is available to get around the storm. You take it.
#
# While you wait for your flight, you decide to check in with the Elves back at the North Pole. They're playing a **memory game** and are ever so excited to explain the rules!
#
# In this game, the players take turns saying **numbers**. They begin by taking turns reading from a list of **starting numbers** (your puzzle input). Then, each turn consists of considering the **most recently spoken number**:
#
# * If that was the **first** time the number has been spoken, the current player says `0`.
# * Otherwise, the number had been spoken before; the current player announces **how many turns apart** the number is from when it was previously spoken.
#
# So, after the starting numbers, each turn results in that player speaking aloud either `0` (if the last number is new) or an **age** (if the last number is a repeat).
#
# For example, suppose the starting numbers are `0, 3, 6`:
#
# * **Turn 1**: The `1`st number spoken is a starting number, **`0`**.
# * **Turn 2**: The `2`nd number spoken is a starting number, **`3`**.
# * **Turn 3**: The `3`rd number spoken is a starting number, **`6`**.
# * **Turn 4**: Now, consider the last number spoken, `6`. Since that was the first time the number had been spoken, the `4`th number spoken is **`0`**.
# * **Turn 5**: Next, again consider the last number spoken, `0`. Since it had been spoken before, the next number to speak is the difference between the turn number when it was last spoken (the previous turn, `4`) and the turn number of the time it was most recently spoken before then (turn `1`). Thus, the 5th number spoken is `4 - 1`, **`3`**.
# * **Turn 6**: The last number spoken, `3` had also been spoken before, most recently on turns `5` and `2`. So, the `6`th number spoken is `5 - 2`, **`3`**.
# * **Turn 7**: Since `3` was just spoken twice in a row, and the last two turns are `1` turn apart, the `7`th number spoken is **`1`**.
# * **Turn 8**: Since `1` is new, the `8`th number spoken is **`0`**.
# * **Turn 9**: `0` was last spoken on turns `8` and `4`, so the `9`th number spoken is the difference between them, **`4`**.
# * **Turn 10**: `4` is new, so the `10`th number spoken is **`0`**.
#
# (The game ends when the Elves get sick of playing or dinner is ready, whichever comes first.)
#
# Their question for you is: what will be the **`2020`th** number spoken? In the example above, the `2020`th number spoken will be `436`.
#
# Here are a few more examples:
#
# * Given the starting numbers `1,3,2`, the `2020`th number spoken is `1`.
# * Given the starting numbers `2,1,3`, the `2020`th number spoken is `10`.
# * Given the starting numbers `1,2,3`, the `2020`th number spoken is `27`.
# * Given the starting numbers `2,3,1`, the `2020`th number spoken is `78`.
# * Given the starting numbers `3,2,1`, the `2020`th number spoken is `438`.
# * Given the starting numbers `3,1,2`, the `2020`th number spoken is `1836`.
#
# Given your starting numbers, **what will be the `2020`th number spoken?**
#
# Your puzzle input is `1,12,0,20,8,16`.

# %%
input = [0, 3, 6]

# %%
input = [1, 3, 2]

# %%
input = [2, 1, 3]

# %%
input = [1, 12, 0, 20, 8, 16]

# %%
n = 2020

sequence = []

for i in range(1, n + 1):
    if i <= len(input):
        sequence.append(input[i - 1])
    else:
        last = sequence[-1]
        occurrences = [i for i, n in enumerate(sequence[::-1]) if n == last]
        assert len(occurrences) > 0
        if len(occurrences) == 1:
            sequence.append(0)
        elif len(occurrences) >= 2:
            sequence.append(occurrences[1] - occurrences[0])

sequence[n - 1]

# %% [markdown]
# ## Part Two
#
# Impressed, the Elves issue you a challenge: determine the `30000000`th number spoken. For example, given the same starting numbers as above:
#
# * Given `0,3,6`, the `30000000`th number spoken is `175594`.
# * Given `1,3,2`, the `30000000`th number spoken is `2578`.
# * Given `2,1,3`, the `30000000`th number spoken is `3544142`.
# * Given `1,2,3`, the `30000000`th number spoken is `261214`.
# * Given `2,3,1`, the `30000000`th number spoken is `6895259`.
# * Given `3,2,1`, the `30000000`th number spoken is `18`.
# * Given `3,1,2`, the `30000000`th number spoken is `362`.
#
# Given your starting numbers, **what will be the `30000000`th number spoken?**
#
# Your puzzle answer was `47205`.

# %%
n = 2020

sequence = []

for i in range(1, n + 1):
    if i <= len(input):
        sequence.insert(0, input[i - 1])
    else:
        last = sequence[0]
        try:
            previous = sequence.index(last, 1)
            sequence.insert(0, previous)
        except ValueError:
            sequence.insert(0, 0)

sequence[0]

# %%
n = 2020

mentions = {}

for i in range(1, n + 1):
    if i <= len(input):
        mentions[input[i - 1]] = [i]
        last = input[i - 1]
    else:
        if len(mentions[last]) == 1:
            age = 0
        else:
            age = mentions[last][0] - mentions[last][1]
        last = age
        if age in mentions:
            mentions[age] = [i, mentions[age][0]]
        else:
            mentions[age] = [i]

last
