def caching_decorator(cachedict):
    def decorator(func):
        def wrapper(*args, **kwargs):
            value = cachedict.get(str(args) + str(kwargs))
            if value:
                return value
            else:
                value = func(*args, **kwargs)
                cachedict[str(args) + str(kwargs)] = value
                return value
        return wrapper
    return decorator
