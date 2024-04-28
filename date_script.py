
from datetime import date, datetime

current_date = date.today().isoformat()
with open("today.txt", "w") as file:
    file.write(current_date)

with open("today.txt", "r") as file:
    today_string = file.read()

parsed_date = datetime.strptime(today_string, "%Y-%m-%d").date()

print("Written Date:", current_date)
print("Read String:", today_string)
print("Parsed Date:", parsed_date)
