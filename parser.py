def is_date(line):
    return len(line.split("/")) == 2

remind_time = "10am"

f_in = open("template.txt", "r")
lines = f_in.readlines()
for line in lines:
    if "event title" in line.lower():
        event_title = line.lstrip("Event Title: ").strip()
        f_out = open(event_title.strip() + ".txt", "w")
    elif is_date(line.split(":")[0]):
        date = line.split(":")[0]
        posters = line.split(":")[1].rstrip().split("@")
        try:
            posters.remove(" ")
        except:
            pass
        for poster in posters:
            poster = poster.strip()
            print(
                "/remind @" + poster + " \"Please make a post about " + event_title + " today. 1-3pm are recommended. Don't forget to check off this Slack reminder when complete!\" "
                                                                                      "at " + remind_time + " " + date)
            f_out.write("/remind @" + poster + " \"Please make a post about " + event_title + " today. 1-3pm are recommended. Don't forget to check off this Slack reminder when complete!\" "
                                                                                      "at " + remind_time + " " + date + "\n")
f_in.close()
f_out.close()
