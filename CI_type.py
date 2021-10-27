import math

with open("./file.log") as file:
    n=0
    candidates0=[]
    candidates1=[]
    for line in file:
        n+=1
        if line.startswith(" Gradient of iOther State"):
            candidates0.append(n)
        if line.startswith(" Gradient of iVec State"):
            candidates1.append(n)
    
    last0=candidates0[-1]
    last1=candidates1[-1]
    allx0,allx1=[],[]
    ally0,ally1=[],[]
    allz0,allz1=[],[]
    n=0

with open("./file.log") as file:
    for line in file:
        n+=1
        all0,all1=[],[]
        if n > last0 and n< last1:
            stripping=line.strip().split(' ')
            for value in stripping:
                if value != '':
                    all0.append(float(value))
            allx0.append(all0[0])
            ally0.append(all0[1])
            allz0.append(all0[2])
    
        dim=len(allx0)
        
        if n>last1 and n<last1+dim+1:
            stripping=line.strip().split(' ')
            for value in stripping:
                if value != '':
                    all1.append(float(value))
            allx1.append(all1[0])
            ally1.append(all1[1])
            allz1.append(all1[2])

c=0
prod=0
peaked=0
sloped=0
range=25

for element in allx0:
    prod=allx0[c]*allx1[c]+ally0[c]*ally1[c]+allz0[c]*allz1[c]
    norm0 = math.sqrt(allx0[c]**2 + ally0[c]**2+ allz0[c]**2)
    norm1 = math.sqrt(allx1[c]**2 + ally1[c]**2+ allz1[c]**2)
    div=prod/(norm0*norm1)
    angle=(math.acos(div))*57.296
    type=abs(180 - angle)
    if type <=range:
        peaked+=1
    else:
        sloped+=1
    c+=1

print("For ",dim," vectors forming the gradient, the results are: ",peaked," peaked",sloped," sloped")
print("The range that has been considered is 180 -",range)

