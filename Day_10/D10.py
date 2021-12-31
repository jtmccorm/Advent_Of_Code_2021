# AOC_2021
# author: @jtmccorm
import re
from collections import Counter
import numpy as np


def remove_small_chunks(chunk: str) -> str:
    chunk = chunk.replace("()", "")
    chunk = chunk.replace("{}", "")
    chunk = chunk.replace("[]", "")
    chunk = chunk.replace("<>", "")
    return chunk


def clean_chunk(old: str) -> str:
    new = remove_small_chunks(old)
    while new != old:
        old, new = new, remove_small_chunks(new)
    return new


def identify_corruption(chunk: str) -> str:
    if re.match("^.*(\{|\[|<)\).*$", chunk): return ")"
    elif re.match("^.*(\(|\[|<)}.*$", chunk): return "}"
    elif re.match("^.*(\(|\{|<)].*$", chunk): return "]"
    elif re.match("^.*(\(|\{|\[)>.*$", chunk): return ">"
    else: return ''


def completion_score(chunk: str, score: int) -> int:
    next = chunk[-1]
    chunk = chunk[:-1]
    if next == "(": score = 5 * score + 1
    elif next == "[": score = 5 * score + 2
    elif next == "{": score = 5 * score + 3
    elif next == "<": score = 5 * score + 4
    if chunk == "":
        return score
    else:
        return completion_score(chunk, score)

if __name__ == '__main__':
    chunks = [line.rstrip() for line in open("D10_input.txt")]
    cleaned_chunks = [clean_chunk(chunk) for chunk in chunks]

    # Part 1 =======================================
    illegal_chars = [identify_corruption(chunk) for chunk in cleaned_chunks if identify_corruption(chunk) != '']
    illegal_counts = Counter()
    for char in illegal_chars:
        illegal_counts[char] += 1
    print(f"Part 1 - \n\t{illegal_counts}"
          f"\n\t{illegal_counts[')']*3 + illegal_counts[']']*57 + illegal_counts['}']*1197 + illegal_counts['>']*25137}")

    # Part 2 =======================================
    incomplete_lines = [chunk for chunk in cleaned_chunks if identify_corruption(chunk) == '']
    completion_scores = [completion_score(line, 0) for line in incomplete_lines]
    print(f"Part 2 - \n\tMedian - {np.median(np.array(completion_scores))}")
