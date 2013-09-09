__author__ = 'dmitrijdackov'

import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    runTime = time.clock() - start
    return result, runTime

print (time_execution("34 * 53452"))

