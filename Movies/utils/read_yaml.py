import yaml
import os
"""
Created on Monday feb 13 2023
@author: kumar.dahal

this functions is created to read yaml file and return the dictionary 
"""
def read_yaml_file(filepath:str) -> dict:
    try:
        with open(filepath,'rb') as yaml_file:
            read_yaml =yaml.safe_load(yaml_file)
        return read_yaml    
    except FileExistsError as fe:
        return fe