name = input("Enter file:")
tekst = open(name)
dic = {}

for lines in tekst:
    if lines.startswith("From "):
        words = lines.split()
        email = words[1]
        dic[email] = dic.get(email, 0)+1
                   
i = None
j = None

for k, v in dic.items():
    if j is None or j < v:
        j = v
        i = k
print(i, j)
