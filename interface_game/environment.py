from time import time
import numpy as np
import random
from abc import ABCMeta, abstractmethod

class BaseEnvironment:
    __metaclass__ = ABCMeta

    def __init__(self,path={}):
        pass

    @abstractmethod
    def env_start(self):
        pass

    @abstractmethod
    def env_step(self, action):
        pass

    @abstractmethod
    def env_cleanup(self):
        pass

    @abstractmethod
    def env_message(self, message):
        pass
        
    @abstractmethod
    def reset(self,player,depth,path):
        pass
    
    @abstractmethod
    def check_win(self):
    
    @abstractmethod
    def step(self,action):
        pass
    
    @abstractmethod
    def isValid(self,action):
        pass