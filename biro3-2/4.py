def vizen_jaras(val):
    if not isinstance(val, str): return False
    
    allo = 0
    hullamos = 0
    
    for i in val:
        if("_" in i):
            allo += 1
        elif("~" in i):
            hullamos += 1
    
    return hullamos >= allo

# print(vizen_jaras("~~_~~~__~_~~__"))