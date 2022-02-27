def sqlalchemy_repr(org_class):
    def __repr__(self):
       dict = {k: self.__dict__.get(k) for k in self.__dict__ if not k.startswith('_')}
       return ' '.join(f'{k}={v}' for k, v in dict.items())

    org_class.__repr__ = __repr__
    return org_class