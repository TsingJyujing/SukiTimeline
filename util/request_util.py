
def get_default(dic,key:str,default_value:str)->str:
    try:
        return dic[key]
    except:
        return default_value