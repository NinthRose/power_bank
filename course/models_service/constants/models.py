class ModelsConstant(object):

    def __init__(self):
        self.type_id = (int, str)

    def is_id(self, id):
        return isinstance(id, self.type_id)


models_constant = ModelsConstant()
