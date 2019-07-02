def HeightConverter(feet=0, inches=0): # Default values of the argument are 0
    """Convert American metric value to European metric value"""

    inch_to_cm = 2.54
    inches_to_cm = inches * inch_to_cm
    feets_to_cm = feet * 12 * inch_to_cm

    cm_to_meter = (feets_to_cm + inches_to_cm) / 100.00
    
    print(cm_to_meter)
    #return cm_to_meter THIS DOENST RETURN ANYTHING. WHY???

HeightConverter(5,11)