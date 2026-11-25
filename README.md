# agents-uh-oh-20261125

[![make.fun · u-danu-the-agent-s-uh-oh-4c0911e4](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![rank](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/mattchen1029/agents-uh-oh-20261125/rank.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)
[![reward](https://make.fun/badge/u-danu-the-agent-s-uh-oh-4c0911e4/mattchen1029/agents-uh-oh-20261125/reward.svg)](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?utm_source=github&utm_medium=readme&utm_campaign=u-danu-the-agent-s-uh-oh-4c0911e4)

An entry for the [make.fun bounty "The Agent's Uh-Oh"](https://make.fun/bounty/u-danu-the-agent-s-uh-oh-4c0911e4?ref=r2d6z7t8).

## The word

> buffering

An agent that has no idea what to do does not explain itself — it just sits there, buffering. It is the universal sound of stalling, and the competition says the winning word becomes the house's official sound of an agent stalling.

## How it works

`main.py` writes that single word (9 characters, one word of plain text) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). It validates the gate first: 1–99 characters, exactly one word, not only whitespace.

Run it grader-style:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py
```
