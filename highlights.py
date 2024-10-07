from pathlib import Path
from data import res
import os

# Define the path to the specific file
file_path = Path("themes/tr.json")

path = "themes"

# Iterate over all files in the folder
for filename in os.listdir(path):
    file_path = os.path.join(path, filename)

    # Ensure we're reading only files (not directories)
    if os.path.isfile(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()

            for i in range(len(lines)):
                if i + 1 in res:
                    font_style = res[i + 1]["fontStyle"]
                    pos = res[i + 1]["pos"]

                    pos_format = {
                        0: f'"fontStyle": "{font_style}"',
                        1: f'"fontStyle": "{font_style}",',
                        2: f',"fontStyle": "{font_style}" }}',
                    }

                    # Update the line with the appropriate format
                    lines[i] = pos_format.get(pos, lines[i])

        with open(file_path, "w") as file:
            file.writelines(lines)
