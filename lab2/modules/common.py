import datetime
import sys
import random
import logging


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

def hundret(trfl):
    if trfl == True:
        for i in range (100):
            if i%2==0:
                print(i, end=' ')
    elif trfl == False:
        for i in range (100):
            if i%2==1:
                print(i, end=' ')
        
def error_func():
    num = 120
    div = random.randint(0,5)
    res = num/div
    print(res)
