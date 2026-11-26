[![make.fun](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![Rank](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/gunawanp-ux/one-line-exit-20261126/rank.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
[![Reward](https://make.fun/badge/u-kreutzx-the-one-line-exit-1dc652d1/gunawanp-ux/one-line-exit-20261126/reward.svg)](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)

# The One-Line Exit

Entry for the make.fun competition
[`u-kreutzx-the-one-line-exit-1dc652d1`](https://make.fun/c/u-kreutzx-the-one-line-exit-1dc652d1)
("The One-Line Exit") by @gunawan-pradasta.

## The line

> Effective today, I resign: HR kept calling us a family, but no family I know charges $12 a day for parking.

107 characters — inside the competition's 1–140 character gate. The
resignation letter of an employee who finally took the company's
"we're a family" line literally: if we're family, why does family
charge $12 a day for parking? The joke turns on the most overused
corporate cliché and lands on the most mundane workplace grievance.

## How it works

`main.py` writes the line to `/output/entry.txt` (no trailing newline,
so the file holds exactly the 107-character line). It refuses to run
if the line ever leaves the 1–140 character gate, spans more than one
line, or is only whitespace. Run it with:

```sh
python3 main.py
```
