import pandas as pd
def Attendence_file(s):
    dic_att ={"Name":[]}
    for i in range(1,31):
        dic_att["Day" + str(i)] = []
    data = pd.read_csv("My_faces.csv")
    dn = (data["Name"].values)
    q = list(set(dn))
    for i in q:
        dic_att["Name"].append(i)
        for j in range(1,31):
            dic_att["Day" + str(j)].append(0)
    
    df = pd.DataFrame(dic_att)
    df.to_csv(r'C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36\ ' + s + ".csv",index = None , header = True)
    
for i in range(1,13):
    Attendence_file('My_attendence' + str(i))
