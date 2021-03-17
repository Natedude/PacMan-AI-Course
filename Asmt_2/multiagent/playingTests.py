from pprint import pprint

sol=[
    [["West", "East"], ["West", "East"], ["West", "East"], ["West", "East"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West", "North"], ["West", "North"], ["West", "North"], ["West", "North"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West", "North"], ["West", "North"], ["West", "North"], ["West", "North"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["West", "Stop"], ["West"], ["Stop"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["West"], ["West"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]],
    [["East", "North"], ["East", "North"], ["East"], ["East"]],
    [["North", "South"], ["North", "South"], ["North"], ["North"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West", "Stop"], ["West"]],
    [["West"], ["West"], ["West", "Stop", "East", "South"], ["West", "East", "South"]],
    [["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]],
    [["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "South"], ["South"], ["Stop", "South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East", "North"], ["East", "North"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["North", "South"], ["North", "South"], ["South"], ["South"]],
    [["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]],
    [["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]],
    [["North", "South"], ["North", "South"], ["North"], ["North"]],
    [["West", "East"], ["West", "East"], ["East"], ["East"]],
    [["West"], ["West"], ["East"], ["East"]],
    [["Stop", "East", "South"], ["East", "South"], ["East"], ["East"]],
    [["Stop", "East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["West", "East"], ["West", "East"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West", "North"], ["West", "North"], ["West", "North"], ["West", "North"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West", "Stop", "East", "North"], ["West", "East", "North"], ["West", "Stop", "East", "North"], ["West", "East", "North"]],
    [["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]],
    [["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]],
    [["Stop", "East", "North"], ["East", "North"], ["Stop", "East", "North"], ["East", "North"]],
    [["Stop", "North"], ["North"], ["Stop", "North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East", "South"], ["East", "South"], ["East", "South"], ["East", "South"]],
    [["East", "South"], ["East", "South"], ["East", "South"], ["East", "South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["North", "South"], ["North", "South"], ["North", "South"], ["North", "South"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West", "Stop", "East", "South"], ["West", "East", "South"], ["West", "Stop", "East", "South"], ["West", "East", "South"]],
    [["West", "Stop", "East", "South"], ["West", "East", "South"], ["West", "Stop", "East", "South"], ["West", "East", "South"]],
    [["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]],
    [["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]],
    [["Stop", "South"], ["South"], ["Stop", "South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["South"], ["South"], ["South"], ["South"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East", "North"], ["East", "North"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["East"], ["East"], ["East"], ["East"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["North"], ["North"], ["North"], ["North"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West"], ["West"], ["West"], ["West"]],
    [["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
]

s = """[["West", "East"], ["West", "East"], ["West", "East"], ["West", "East"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West", "North"], ["West", "North"], ["West", "North"], ["West", "North"]]
[["West"], ["West"], ["West"], ["West"]]
[["West", "North"], ["West", "North"], ["West", "North"], ["West", "North"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["East"], ["East"], ["East"], ["East"]]
[["West", "Stop"], ["West"], ["Stop"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["West"], ["West"]]
[["East"], ["East"], ["East"], ["East"]]
[["North"], ["North"], ["North"], ["North"]]
[["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]]
[["East", "North"], ["East", "North"], ["East"], ["East"]]
[["North", "South"], ["North", "South"], ["North"], ["North"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West", "Stop"], ["West"]]
[["West"], ["West"], ["West", "Stop", "East", "South"], ["West", "East", "South"]]
[["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
[["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "South"], ["South"], ["Stop", "South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East", "North"], ["East", "North"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["North", "South"], ["North", "South"], ["South"], ["South"]]
[["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]]
[["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]]
[["North", "South"], ["North", "South"], ["North"], ["North"]]
[["West", "East"], ["West", "East"], ["East"], ["East"]]
[["West"], ["West"], ["East"], ["East"]]
[["Stop", "East", "South"], ["East", "South"], ["East"], ["East"]]
[["Stop", "East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["West"], ["West"], ["West"], ["West"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["West", "East"], ["West", "East"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West", "North"], ["West", "North"], ["West", "North"], ["West", "North"]]
[["West"], ["West"], ["West"], ["West"]]
[["West", "Stop", "East", "North"], ["West", "East", "North"], ["West", "Stop", "East", "North"], ["West", "East", "North"]]
[["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
[["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
[["Stop", "East", "North"], ["East", "North"], ["Stop", "East", "North"], ["East", "North"]]
[["Stop", "North"], ["North"], ["Stop", "North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East", "South"], ["East", "South"], ["East", "South"], ["East", "South"]]
[["East", "South"], ["East", "South"], ["East", "South"], ["East", "South"]]
[["South"], ["South"], ["South"], ["South"]]
[["North", "South"], ["North", "South"], ["North", "South"], ["North", "South"]]
[["West"], ["West"], ["West"], ["West"]]
[["West", "Stop", "East", "South"], ["West", "East", "South"], ["West", "Stop", "East", "South"], ["West", "East", "South"]]
[["West", "Stop", "East", "South"], ["West", "East", "South"], ["West", "Stop", "East", "South"], ["West", "East", "South"]]
[["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
[["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"], ["Stop", "East", "South"], ["East", "South"]]
[["Stop", "South"], ["South"], ["Stop", "South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["South"], ["South"], ["South"], ["South"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]]
[["East"], ["East"], ["East"], ["East"]]
[["East", "North"], ["East", "North"], ["East", "North"], ["East", "North"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East", "North"], ["East", "North"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["East"], ["East"], ["East"], ["East"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["North"], ["North"], ["North"], ["North"]]
[["West"], ["West"], ["West"], ["West"]]
[["West"], ["West"], ["West"], ["West"]]
[["West", "Stop", "East"], ["West", "East"], ["West", "Stop", "East"], ["West", "East"]]
"""

s2 = """[["West", "East"], ["West", "East"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West", "North"], ["West", "North"]]
[["West"], ["West"]]
[["West", "North"], ["West", "North"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["East"], ["East"]]
[["Stop"], ["West"]]
[["West"], ["West"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["West"], ["West"]]
[["East"], ["East"]]
[["North"], ["North"]]
[["East", "North"], ["East", "North"]]
[["East", "North"], ["East", "North"]]
[["North", "South"], ["North", "South"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West", "Stop"], ["West"]]
[["West", "Stop", "East"], ["West", "East"]]
[["West", "Stop", "East"], ["West", "East"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East", "North"], ["East", "North"]]
[["East"], ["East"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["North", "South"], ["North", "South"]]
[["East", "North"], ["East", "North"]]
[["East", "North"], ["East", "North"]]
[["North", "South"], ["North", "South"]]
[["West", "East"], ["West", "East"]]
[["West", "Stop", "East"], ["West", "East"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East"], ["East"]]
[["East"], ["East"]]
[["West"], ["West"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West", "North"], ["West", "North"]]
[["West"], ["West"]]
[["West", "Stop", "East", "North"], ["West", "East", "North"]]
[["West", "Stop", "East"], ["West", "East"]]
[["West", "Stop", "East"], ["West", "East"]]
[["Stop", "East", "North"], ["East", "North"]]
[["Stop", "North"], ["North"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East", "South"], ["East", "South"]]
[["East", "South"], ["East", "South"]]
[["South"], ["South"]]
[["North", "South"], ["North", "South"]]
[["West"], ["West"]]
[["West", "Stop", "East", "South"], ["West", "East", "South"]]
[["West", "Stop", "East", "South"], ["West", "East", "South"]]
[["West", "Stop", "East"], ["West", "East"]]
[["West", "Stop", "East"], ["West", "East"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "East", "South"], ["East", "South"]]
[["Stop", "South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["South"], ["South"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East", "North"], ["East", "North"]]
[["East"], ["East"]]
[["East", "North"], ["East", "North"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["East", "North"], ["East", "North"]]
[["East"], ["East"]]
[["East"], ["East"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["North"], ["North"]]
[["West"], ["West"]]
[["West"], ["West"]]
[["West", "Stop", "East"], ["West", "East"]]"""
#pprint(s)
print(len(s))
slines = s2.split('\n')
# slines.remove('')
# slines.remove('')
edit = []
for i in range(len(slines)):
    #print(str(i) + ': ' + slines[i])
    newLine = slines[i][2:9]
    newLine = newLine.replace(']','')
    newLine = newLine.replace(',','')
    newLine = newLine.replace('"','')
    #print(newLine)
    #print(type(newLine))
    edit.append(newLine)
    #print(str(i) + ': ' + edit[i])

print(edit)