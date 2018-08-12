def makeTeams(n_o_t, n_o_p):
    try:
        if type(n_o_t)!=int or type(n_o_p)!=int:
            raise TypeError('Enter positive numbers')
        elif n_o_p  <= 0:
            raise ValueError('number of players has to be positive')
        elif n_o_t < 0:
            raise ValueError('number of teams has to be positive')
        elif n_o_t == 0:
            raise ZeroDivisionError('number of players can\'t be Zero')
        elif n_o_p < n_o_t:
            raise ValueError('Enter a different set of numbers')
        else:
            rem = n_o_p%n_o_t
            if(rem>0):
                raise ValueError('remove '+str(rem)+' of players')
    except TypeError as te:
        print(te)
    except ValueError as ve:
        print(ve)
    except ZeroDivisionError as ze:
        print(ze)
