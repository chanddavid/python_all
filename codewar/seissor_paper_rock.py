
def rps(p1, p2):
    """rock papper scissor gaem
    Args:
        p1 (_type_): polayer 1
        p2 (_type_): player 2
    Returns:
        _type_: winner
    """
    if p1=='paper' and p2=='rock' or p1=='scissors' and p2=='paper' or p1=='rock' and p2=='scissors' :
        return 'Player 1 won!'
    elif p1=='rock' and p2=='paper' or p1=='paper' and p2=='scissors' or p1=='scissors' and p2=='rock':
        return 'Player 2 won!'            
    else:
        return 'Draw!'
x=rps('scissors','paper')
print(x)