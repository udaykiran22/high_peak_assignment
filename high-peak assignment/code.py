import sys
outfile = open("output.txt","w")
infile = open("Testcase-3.txt","r")
userlines = infile.readlines()
gandp = {}
pandg = {}
numofemp = int(userlines[0].split(": ")[1])
goodies = userlines[4:]
prices = []
for item in goodies:
    if item[-2:] == "\n":
        item = item.split(": ")
        name,price = item[0],int(item[1][:-1])
    else:
        item = item.split(": ")
        name,price = item[0],int(item[1])
    prices.append(price)
    gandp[name] = price
sprices = sorted(prices)
diff = []
for i in range(len(prices)-numofemp):
    diff.append(sprices[i+numofemp-1] - sprices[i])
for i in gandp:
    pandg[gandp[i]] = i
ind = diff.index(min(diff))
out = ["The goodies selected for distribution are:\n","\n"]
for i in sprices[ind:ind+numofemp]:
    out.append(pandg[i] + ": " + str(i) + "\n")
out.append("\n")
out.append("And the difference between the chosen goodie with highest price and the lowest price is " + str(min(diff)))
outfile.writelines(out)
outfile.close()
