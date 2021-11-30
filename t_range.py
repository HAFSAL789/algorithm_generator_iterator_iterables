def t_range(start, stop, step):
    """
    :param start, stop: positive values, less than 24 hr
    :param step: postive values
    :return: t_range tuple

    """
    for time in start, stop, step:
        if time < (0, 0, 0):
            raise ValueError('negative time')
        if time != step and time > (24, 0, 0):
            raise ValueError('greater than 24 hr')

    while start <= stop:
        yield start
        hrs, mins, secs = start
        s_hrs, s_mins, s_secs = step
        secs += s_secs
        mins += secs // 60
        secs = secs - 60 if secs > 60 else secs
        mins += s_mins
        hrs += mins // 60
        mins = mins - 60 if mins > 60 else mins
        hrs += s_hrs
        start = hrs, mins, secs


for time in t_range((10, 10, 10), (19, 53, 15), (1, 24, 12)):
    print(time)
