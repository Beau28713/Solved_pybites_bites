from functools import partial

def round_number(num, det):
    return round(num, det)
rounder_int =  partial(round_number, det = 0)
rounder_detailed =  partial(round_number, det = 4)