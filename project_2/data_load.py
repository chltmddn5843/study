import numpy 
import pandas as pd
from datetime import datetime, timedelta
import os 

def labelmerge(data): 
    new_label=[]
    for i in range(len(data)):
        id=data['enb_cell_id'][i]+'-'+str(data['dt'][i])+'-'+str(data['hh'][i])
        
        new_label.append(id)
        
    data['New']=new_label
    
    return data

def extract_data(df_list,cell_id):
    set_label=[]
    date_start = datetime.strptime("20210901", "%Y%m%d")
    date_end = datetime.strptime("20211201", "%Y%m%d")
    date_diff = date_end - date_start
    
    for i in range(date_diff.days):
        date=date_start + timedelta(days = i)
        for j in range(24):
            value= cell_id + '-' + date.strftime('%Y%m%d') + '-' + str(j)
            set_label.append(value)
            
    df_final=pd.DataFrame()
    df_final['New']=set_label

    if cell_id in df_list[0].enb_cell_id.unique():
        for i in range(len(df_list)):
            df_tmp = labelmerge(df_list[i][df_list[i].enb_cell_id==cell_id].reset_index(drop=True))
            df_final = pd.merge(df_final,df_tmp ,left_on='New',right_on='New',how='left')
            df_final.drop(['enb_cell_id', 'dt', 'hh'],axis='columns', inplace=True)
    print('데이터 병합 완료')
    return df_final

def return_data(df_lists, machine_name):
    
    id_df=pd.DataFrame()
    id_df['enb_cell_id']=df_lists[0]['enb_cell_id']
    
    id_df_2=id_df.drop_duplicates('enb_cell_id').reset_index(drop=True)
    
    new_id=[]
    for i in range(len(id_df_2)):
        new_id.append(id_df_2['enb_cell_id'][i])  
    
    print('데이터 병합 준비 완료')
    
    df_concat=extract_data(df_lists, machine_name)
    
    # df_concat.to_csv('1005_1.csv', header=True, index=False)
    
    return df_concat