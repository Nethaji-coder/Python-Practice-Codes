class PinError(Exception):
    pass
correctPin = 6969
pin = int(input())
try:
    if(pin == correctPin):
        print('Account Unblocked')
    else:
        raise PinError('Entered Pin is: ',pin)

except PinError as e:
    print('Incorrect Pin: ',e)