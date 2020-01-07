from course.common.exceptions.models.models_exception import PowerBankModelsException


class PowerBankUserException(PowerBankModelsException):

    def __init__(self, *args, **kwargs):
        PowerBankModelsException.__init__(self, *args, **kwargs)
