def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('ZeroDivisionError Occurred and Handled')
    except NameError:
        print('Name error Occurred and Handled')
    except TypeError:
        print('Type Error Occured and Handled')
    except:
        print('Some error Occured and Handled')
disp(10,'Kodnest')