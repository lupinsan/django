from datetime import *
date1 = "2022.05.11 13:30:00"
date2 = "2022.05.10 12:00:00"
date1 = datetime.strptime(date1, "%Y.%m.%d %H:%M:%S")
date2 = datetime.strptime(date2, "%Y.%m.%d %H:%M:%S")
print(" date1:", date1, "\n" ,"date2:", date2)
duration = date1 - date2
print(duration.seconds)