import os
import re

line_regex1 = re.compile(r".*Error.*$")
line_regex2 = re.compile(r".*Warning.*$")

output_filename = os.path.normpath("parsed_lines.txt")
with open(output_filename, "w") as out_file:
    out_file.write("")

with open(output_filename, "a") as out_file:
    with open("test_log.txt", "r") as in_file:
        for line in in_file:
            if (line_regex1.search(line)):
                out_file.write(line)
            elif (line_regex2.search(line)):
                out_file.write(line)