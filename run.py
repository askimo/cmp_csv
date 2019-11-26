# -*- coding: utf-8 -*-

import pandas as pd


old_file_path="./old.csv"
new_file_path="./new.csv"
res_file_path="./res.csv"

#dtype = {'column_name' : str}设置列数据类型

#dt={"岗位薪点":"float64","市补":"float64","提租":"float64","加班":"float64","通讯费":"float64","证件补贴":"float64","保健津贴":"float64","其他":"float64","扣款":"float64","应发合计":"float64","养老":"float64","公积":"float64","医疗":"float64","失业":"float64","扣工会费":"float64","实发合计":"float64"}
dt={}
old=pd.read_csv(old_file_path,encoding="gb18030",header=1,dtype=dt)
new=pd.read_csv(new_file_path,encoding="gb18030",header=1,dtype=dt)

item=new.columns
row_n=len(new)

#item=["序号","二级核算项目","项目","部门","工号","姓名","岗位薪点","市补","提租","加班","通讯费","证件补贴","保健津贴","其他","扣款","应发合计","养老","公积","医疗","失业","扣工会费","实发合计","备注"]
#old.loc[0,item[5]]获取某一行的写法

#for i in range(row_n):
#    s=old.loc[i]

#old.iloc[2,2]
DIF=[]
ADD=[]
DEL=[]

new=new.fillna(0.0)
old=old.fillna(0.0)

old.apply(pd.to_numeric, errors='ignore')
new.apply(pd.to_numeric, errors='ignore')

key=4

new.iloc[:,0]=""
old.iloc[:,0]=""

for i in range(row_n):
    GH=new.iloc[i,key]
    search=old[old[item[key]]==GH]
    if len(search) == 1 : #找到1个
        new.iloc[i,0]="match"
        old_id=old[old["工号"]==GH].index[0]
        dif_flag=False
        for j in range(1,23):
            if j==21 or j==15:
                continue#合计列就不要单独对比了

            if new.iloc[i,j]==old.iloc[old_id,j]:
                pass
            else:
                new.iloc[i,0]+=item[j]
                dif_flag=True
                print("工号："+str(GH)+" col:"+item[j])
                print("new.iloc[%d,%d]="%(i,j)+str(new.iloc[i,j])+"  old.iloc[%d,%d]="%(old_id,j)+str(old.iloc[old_id,j]))
        if dif_flag:
            DIF.append(new.iloc[i,])
            #print("**** FIND   DIFERENCE ****")
        old.iloc[old_id,0]="match"

        pass
    elif len(search)== 0 :#没找到，说明这个GH是新增的
        
        pass
    else:#旧的有，新的没有，说明是删除了人员
        pass





res=pd.DataFrame(DIF)
res.to_csv(res_file_path)

        
    
