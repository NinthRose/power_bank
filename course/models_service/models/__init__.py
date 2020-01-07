import pickle


def models_dumps(instance):
    return pickle.dumps(instance)


def models_loads(bytes):
    return pickle.loads(bytes)
