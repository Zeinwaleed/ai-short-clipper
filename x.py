# z = "welcome to English in a minute bones are strong they make up our skeleton but what could it mean to have a bone to pick with someone then are you ready to read scripts may be turn on WhatsApp about something actually"
# x = [i for i in range(len(z)) if z.startswith("bones are strong", i)]

# print(len("bones are strong"))
# print(x[0])
start_times = [31]


for start_time in start_times:
    end_time = start_time + len("bones are strong")
    print(start_time - 31)

print(end_time)