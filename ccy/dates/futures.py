
future_month_list = ['F', 'G', 'H', 'J', 'K', 'M',
                     'N', 'Q', 'U', 'V', 'X', 'Z']
short_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def date_to_code(dte):
    '''Obtain a future code from a date.

    For example december 2010 will result in Z10.
    '''
    return '%s%s' % (future_month_list[dte.month-1], str(dte.year)[2:])

short_to_number = {}
c = 0
for i in short_month:
    c += 1
    short_to_number[i] = c


future_month_dict = dict((future_month_list[i],
                          (i+1, short_month[i])) for i in range(0, 12))
