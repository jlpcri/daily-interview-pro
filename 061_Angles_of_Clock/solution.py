def calc_angle(h, m):
    '''
    The hour hand turns 360 in 12 hours: 0.5 per minute
    The minute hand rotates 360 in 60 minutes: 6 per minute
    :param h:
    :param m:
    :return:
    '''
    h %= 12
    m %= 60
    # print(h, m)

    h_angle = 0.5 * (60 * h + m)
    m_angle = 6 * m

    angle = int(abs(h_angle - m_angle))
    return angle if angle < 180 else 360 - angle


print(calc_angle(3, 30))
# 75
print(calc_angle(12, 30))
# 165
print(calc_angle(2, 20))
# 50
print(calc_angle(10, 16))
# 148

