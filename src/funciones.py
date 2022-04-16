import os
import random

OUTPUT = "beatmaplist.csv"


def roll():
    return f"You rolled {random.randint(1, 999)}"


def analize(path):
    if "osu" in path and os.path.exists(path):
        writer = open(OUTPUT, "w", newline="")
        count = 0
        for _map in os.listdir(path):
            if _map.startswith(("1", "2", "3", "4", "5", "6", "7", "8", "9")) is True:
                writer.writelines(
                    "https://osu.ppy.sh/beatmapsets/"
                    + _map.split(" ", 1)[0]
                    + "\t" * 2
                    + _map.split(" ", 1)[1]
                    + "\n"
                )
                count += 1
        return f"Files analized: {count}"
