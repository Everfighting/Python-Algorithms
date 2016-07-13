#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    person = {"li":25,"wang":20,"zhang":26,"sun":22}
    m = 'li'
    for key in person.keys():
        if person[m] < person[key]:
            m = key

    print '%s,%d' % (m,person[m])