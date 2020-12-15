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
