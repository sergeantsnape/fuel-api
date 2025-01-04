# meta class can be considered as a class factory. classes are made from metaclasses. 
# normally a class is made from "type"

class SingletonMetaClass(type):
    """
    factory for creating singleton classes
    """
    _instances = {}

    def __call__(self, *args, **kwargs):
        # attribute based singleton class
        if getattr(self,'attribute_based', False):
            key = (self,args,frozenset(kwargs.items()))
            if key not in self._instances:
                self._instances[key] = super().__call__(*args,**kwargs)
            return self._instances[key]
        
        # normal singleton class
        else:
            if self not in self._instances:
                self._instances[self] = super().__call__(*args,**kwargs)
            return self._instances[self]

        