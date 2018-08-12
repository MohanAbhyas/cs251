def makeTeams(n_o_t, n_o_p):
    if n_o_t == 0:
        raise ZeroDivisionError('number of players in team can\'t be Zero')
    rem = n_o_p%n_o_t
    if rem != 0:
        raise ValueError('remove '+str(rem)+' of players')
