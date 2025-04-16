#!/usr/bin/python3
# -*-coding :utf-8 -*-

#import ConfigParser

def get_cmp_cfg() :
    cmp_str = ""

    return cmp_str

def get_sim_cfg() :
    sim_str = ""

    return sim_str

def get_rgs_cfg() :
    rgs_str = ""

    return rgs_str

#def sim_ini() :

def get_sim_cfg(sim_cfg):
    all_cfg = ''
    f = open(sim_cfg)
    l_list = f.readlines()
    for l_cfg in l_list:
        if "=" in l_cfg :
            l_cfg=l_cfg.replace('\n','')
            all_cfg = all_cfg+" +"+l_cfg+" "  
    return all_cfg
