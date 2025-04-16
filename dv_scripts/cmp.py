#!/usr/bin/python3
# -*-coding :utf-8 -*-

def get_cmp_cmd() :
    rtl_files = '${RTL_HOME}/dut.f'
    tb_files  = '../cfg/tb.f'
    tb_top    = 'harness'
    
    cmp_cmd = 'vcs -ntb_opts uvm-1.2 -full64 -sverilog -debug_access+all -kdb -lca -timescale=1ps/1fs'
    
    cmp_cmd = cmp_cmd + ' -F '+rtl_files 
    cmp_cmd = cmp_cmd + ' -f '+tb_files
    cmp_cmd = cmp_cmd + ' -top '+ tb_top
    return cmp_cmd
