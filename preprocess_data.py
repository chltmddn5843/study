import numpy as np
import pandas as pd
import data_load

def interpolation(df_temp, ordern):
    #spline interpolation
    dl_bler_inter_2=df_temp['dl_bler'].interpolate(method='polynomial', order=ordern)
    ul_bler_inter_2=df_temp['ul_bler'].interpolate(method='polynomial', order=ordern)
    conn_avg_inter_2=df_temp['conn_avg'].interpolate(method='polynomial', order=ordern)
    conn_max_inter_2=df_temp['conn_max'].interpolate(method='polynomial', order=ordern)
    interx2in_succ_rate_inter_2=df_temp['interx2in_succ_rate'].interpolate(method='polynomial', order=ordern)
    interx2out_succ_rate_inter_2=df_temp['interx2out_succ_rate'].interpolate(method='polynomial', order=ordern)
    intraenb_succ_rate_inter_2=df_temp['intraenb_succ_rate'].interpolate(method='polynomial', order=ordern)
    dl_prb_inter_2=df_temp['dl_prb'].interpolate(method='polynomial', order=ordern)
    ul_prb_inter_2=df_temp['ul_prb'].interpolate(method='polynomial', order=ordern)
    reconfig_succ_rate_inter_2=df_temp['reconfig_succ_rate'].interpolate(method='polynomial', order=ordern)
    
    
    df_preprocessed=pd.DataFrame()
    df_preprocessed['dl_bler_inter']=dl_bler_inter_2
    df_preprocessed['ul_bler_inter']=ul_bler_inter_2
    df_preprocessed['conn_avg_inter']=conn_avg_inter_2
    df_preprocessed['conn_max_inter']=conn_max_inter_2
    df_preprocessed['interx2in_succ_rate_inter']=interx2in_succ_rate_inter_2
    df_preprocessed['interx2out_succ_rate_inter']=interx2out_succ_rate_inter_2
    df_preprocessed['intraenb_succ_rate_inter']=intraenb_succ_rate_inter_2
    df_preprocessed['dl_prb_inter']=dl_prb_inter_2
    df_preprocessed['ul_prb_inter']=ul_prb_inter_2
    df_preprocessed['reconfig_succ_rate_inter']=reconfig_succ_rate_inter_2
    
    return df_preprocessed

def return_preprocess_data(df_list, machine_name, order):
    df = data_load.return_data(df_list, machine_name)
    
    df_preprocess = interpolation(df, order)
    
    return df_preprocess
    