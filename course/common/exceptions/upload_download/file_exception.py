from course.common.exceptions.orca_exception import PowerBankException


class OrcaFileException(PowerBankException):

    def __init__(self, *args, **kwargs):
        PowerBankException.__init__(self, *args, **kwargs)
