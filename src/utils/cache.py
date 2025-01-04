from src.utils.metas import SingletonMetaClass
from redis import Redis
import json

class Cache(metaclass=SingletonMetaClass):
    attribute_based = True     # class variable
    def __init__(self,host='localhost',port=6379,db=0,ttl=3600):
        self.redis = Redis(host,port,db)
        self.ttl = ttl

    def get(self,key):
        value = self.redis.get(key)
        return json.loads(value) if value else None

    def set(self,key,value):
        self.redis.setex(key,self.ttl,json.dumps(value))
