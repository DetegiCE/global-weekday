class conv:
    def __init__(self):
        self.EN = 0
        self.KR = 1
        self.wd = {'en': ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI'],
                   'kr': ['토', '일', '월', '화', '수', '목', '금']}

    def weekday_number(self, y:int, m:int, d:int):
        if m <= 2:
            m += 12
            y -= 1
        k = y % 100
        j = y // 100
        h = (d+(26*(m+1)//10)+k+k//4+j//4+5*j)%7
        return h

    def wd_conv(self, y, m, d, lang=None):
        if not lang:
            lang = 0
        LANGMAX = 2
        langkeys = ['en', 'kr']
        if str(type(y)) == '<class \'str\'>':
            y = int(y)
        if str(type(m)) == '<class \'str\'>':
            m = int(m)
        if str(type(d)) == '<class \'str\'>':
            d = int(d)
        if lang < 0 or lang >= LANGMAX:
            raise Exception('language number not supported')
        else:
            return self.wd[langkeys[lang]][self.weekday_number(y, m, d)]

