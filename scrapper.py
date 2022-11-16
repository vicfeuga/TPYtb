#!/usr/bin/env python
from fonctions import *
import argparse

#Create argument parser ibject
parser = argparse.ArgumentParser()

#Add argument 
parser.add_argument('--input', help='JSON input with URL ', required=True)
parser.add_argument('--output', help='JSON output with the results', required=True)

#Get argument
args = parser.parse_args()
argdict = vars(args)
input_para = argdict['input']
output_para = argdict['output']

#read input file
id_list=read_input(input_para)

data = []
#navigate in all videos id
for i in id_list['videos_id']:
    #Get informations for video i
    d = find_informations(i)
    data.append(d)

#write down the results
write_output(output_para, data)