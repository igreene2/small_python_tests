import numpy as np
import json

sv1 = np.random.rand(5, 1)
sv2 = np.random.rand(5, 1)
tv = np.random.rand(5, 1)

sv0 = np.squeeze(sv1)
sv3 = np.squeeze(sv2)
tv0 = np.squeeze(tv)


vectors = [sv0, sv3, tv0]

for v in vectors:
    count = 0
    for x in v:
        x = x*10
        v[count] = x
        count = count + 1
        #print(x)

tv = np.reshape(tv, (5, 1))
print(tv)
sv0 = sv0.reshape(5, 1)
#print(sv0)

supportMatrix = sv0*np.transpose(sv0)
print(supportMatrix)

count = 0
full_set = []
for v in supportMatrix:
    count2 = 0
    for x in v:
        data_set =  {"_instr_No.": count, 
                    "addr": hex(count), 
                    "data": float(v[count2]), 
                    "mode": "1",
                    "isfloat": "0"}
        full_set.append(data_set)
        #json_dump = json.dumps(data_set, indent=4)
        #print(json_dump)
        #print(",")
        count = count+1
        count2 = count2 + 1

count2 = 0
print(count)
for x in tv:   
    data_set =  {"_instr_No.": count, 
                "addr": hex(count), 
                "data": float(tv[count2]), 
                "mode": "1",
                "isfloat": "0"}
    full_set.append(data_set)
    #json_dump = json.dumps(data_set, indent=4)
    #print(json_dump)
    #print(",")
    count = count+1
    count2 = count2 + 1
#print(",")
print(count)

json_dump = json.dumps(full_set, indent=4)
print(json_dump)



b = -1
th = 0
sum = 0

out = tv.T.dot(supportMatrix)
print(out)
outdot = out.dot(tv)
print(outdot)


print("polyprec")
#print(out)
final = outdot - th - b
print(final)