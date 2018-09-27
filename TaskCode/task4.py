__author__ = 'YangJun'


def Mysort(dat):
    newlist = []
    if type(dat) is list:
        while len(dat) > 0:
            Min = dat[0]
            for i in range(0, len(dat)):
                if Min >= dat[i]:
                    Min = dat[i]
                    # if i == len(dat) - 1:
                    #     print 'test'
            newlist.append(Min)
            dat.remove(Min)
        return newlist
    else:
        print 'The incoming parameter is incorrect'


if __name__ == "__main__":
    b = [8, 3, 9, 2, 5, 5, 11, 1]
    c = 3
    data = Mysort(b)
    print data
