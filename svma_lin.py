import numpy as np
import json

sv1 = np.random.rand(18, 1)
sv2 = np.random.rand(18, 1)
tv = np.random.rand(18, 1)

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
        print(x)

count = 0
full_set = []
for v in vectors:
    count2 = 0
    for x in v:
        data_set =  {"_instr_No.": count, 
                    "addr": hex(count), 
                    "data": v[count2], 
                    "mode": "1",
                    "isfloat": "0"}
        full_set.append(data_set)
        #json_dump = json.dumps(data_set, indent=4)
        #print(json_dump)
        #print(",")
        count = count+1
        count2 = count2 + 1
    data_set =  {"_instr_No.": count, 
                    "addr": hex(count), 
                    "data": -0.000108612, 
                    "mode": "1",
                    "isfloat": "0"}
    full_set.append(data_set)
  
    #print(",")
    count = count + 1

json_dump = json.dumps(full_set, indent=4)
print(json_dump)

supportVectors = [sv0, sv3];
#print(supportVectors);

alpha = -0.000108612
b = -1
th = 0
sum = 0

# linear
for x in supportVectors:
    #print(x)
    #print(tv)
    out = np.dot(x, tv)
    #print(out)
    outAlpha = out*alpha
    sum += outAlpha

print("linear")
print(sum)
final = sum - th - b
print(final)








