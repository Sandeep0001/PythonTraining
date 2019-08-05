name = "Alex"
for i in name:
    print(i)
    if i== 'e':
        break

name = "Alex"
for i in name:
    print(i)
    if i== 'e':
        continue

str = ["Python", "Java", "Ruby", "C sharp"]
for i in range(len(str)):
    print(str[i])
    if str[i] == 'Java':
        print("Hey I found Java so breaking")
        break


str = ["Python", "Java", "Ruby", "C sharp"]
for i in range(len(str)):
    print(str[i])
    if str[i] == 'Java':
        print("Hey I found Java so continuing")
        continue

lang = ["Kannada", "Hindi", "Telugu", "English"]
flag = False
for i in range(len(lang)):
    print(lang[i])
    if lang[i] == "Telugu":
        flag = True
        print("Telugu is the regional language of India")
        break