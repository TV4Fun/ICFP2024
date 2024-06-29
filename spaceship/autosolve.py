import sys
import os
from pathlib import Path
import requests
from traceback import print_exc
import time
from typing import List, Optional

# Add the parent directory to the Python path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir))

from icfp.encode import encode_and_compile
from icfp.decode import decode_message
import find_optimal_path as snl

URL = "https://boundvariable.space/communicate"
AUTH_HEADER = {"Authorization": "Bearer f8fb3b34-7f8f-4cb0-bd74-c83be464d0a1"}


def send_command(command: str) -> str:
    payload = encode_and_compile(command)
    response = requests.post(URL, data=payload, headers=AUTH_HEADER)
    return decode_message(response.text)


def get_spaceship_coordinates(ship_number: int) -> str:
    return send_command(f"get spaceship{ship_number}")


def solve_spaceship(ship_number: int, path: str):
    send_command(f"solve spaceship{ship_number} {path}")


def main():
    for ship_number in range(1, 26):  # 1 to 25
        try:
            # Get coordinates for the current spaceship
            coordinates_str = get_spaceship_coordinates(ship_number)

            # Find the optimal path
            optimal_path = snl.get_optimal_path(coordinates_str)

            # Send the solution to the terminal
            solve_spaceship(ship_number, optimal_path)

            print(f"Solved spaceship{ship_number}")

            # Add a small delay to avoid overwhelming the server
            time.sleep(1)
        except Exception as e:
            print(f"Error processing spaceship{ship_number}: {str(e)}")
            print_exc()


if __name__ == "__main__":
    main()
