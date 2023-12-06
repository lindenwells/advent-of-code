from os import environ
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()


def get_input(year: int, day: int) -> list[str]:
    possible_input_file_path = Path(f"2023/inputs/{day}.in")
    if possible_input_file_path.exists():
        with open(possible_input_file_path, "r") as f:
            return f.readlines()

    else:
        session_token = environ.get("AOC_SESSION_TOKEN")
        r = requests.get(
            f"https://adventofcode.com/{year}/day/{day}/input",
            cookies=dict(session=session_token),
        )
        with open(possible_input_file_path, "w") as f:
            f.write(r.text)
        return r.text.splitlines()
