import numpy as np
import json

#sv1 = np.random.rand(18, 1)
#sv2 = np.random.rand(18, 1)
tv = np.random.rand(18, 1)

#sv0 = np.squeeze(sv1)
#sv3 = np.squeeze(sv2)
tv0 = np.squeeze(tv)

tv1 = []
for v in tv0:
    tv1.append(v*10)
print(tv1)

sv0 = []
sv3 = []
for x in tv0:
    sv0.append(x*10+2)
    sv3.append(x*10+1)

print(sv0)
print(sv3)

vectors = [sv0, sv3, tv1]

count = 0
full_set = []
for v in vectors:
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
    data_set =  {"_instr_No.": count, 
                    "addr": hex(count), 
                    "data": 1.0, 
                    "mode": "1",
                    "isfloat": "0"}
    full_set.append(data_set)
  
    #print(",")
    count = count + 1

json_dump = json.dumps(full_set, indent=4)
print(json_dump)

supportVectors = [sv0, sv3];
#alternatively just pass in tv to these and you should get 2!
#print(supportVectors);

tau = 1
alpha = 1
b = 0
th = 0
sum = 0
c = 2

# linear
out = []
for x in supportVectors:
    #print(x)
    #print(tv)
    count = 0
    for y in x:
        out.append(y - tv1[count])
        count = count + 1
    outMag = np.linalg.norm(out)
    negMagSquareTau = outMag**2*-1*tau
    exponent = np.exp(negMagSquareTau)
    print(out)
    print(outMag)
    print(negMagSquareTau)
    print(exponent)
    outAlpha = exponent*alpha
    sum += outAlpha
    out = []

print("rbf")
print(sum)
final = sum - th - b
print(final)