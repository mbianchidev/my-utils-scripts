import re

# TODO make it runnable via file input


def process_input(input_str):
    entries = re.findall(r'(.+), \[(\d{2}/\d{2}/\d{4} \d{2}:\d{2})\]\n([\d,]+) (.+)', input_str)

    result_str = ""
    for entry in entries:
        description = entry[3].strip()
        amount = entry[2]

        result_str += f"{description}\t€ {amount}\n"

    return result_str.strip()

# copy-paste the message here
# format is:
# Your telegram name, [18/12/2023 11:34]
# Macbook keyaboard 100
# [space here]
# Your telegram name, [24/12/2023 18:04]
# Slam dunk festival ticket 180


input_str = """

"""

output_str = process_input(input_str)
msg = """Remember to copy the output and paste it in the expenses sheet
 (paste special -> values only)"""

print(msg)
print(output_str+"\n")
print("""Remember to run it on https://www.online-python.com/ otherwise tabs don't work properly.""")
