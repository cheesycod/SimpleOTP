import time
from hashlib import sha512
from math import floor
def gen_otp(skey: str) -> str:
    ct = sha512((skey[:4] + str(floor(time.time()/30)) + skey + skey[4:]).encode()).hexdigest()
    otp = ""
    otp_len = 0
    for char in ct:
        proposed_add = str(ord(char))
        proposed_otp_len = otp_len + len(proposed_add)
        if proposed_otp_len == 5 or proposed_otp_len > 6: # Because we will not get anything with one digit if proposed otp len is 5
            continue # Go to the next character
        otp += proposed_add
        otp_len = proposed_otp_len
    return otp
