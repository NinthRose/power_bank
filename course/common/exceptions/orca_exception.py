class PowerBankException(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class TestException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class BadRequest(Exception):
    code = 400

    def __init__(self, *args, **kwargs):
        pass


class Conflict(Exception):
    code = 409

    def __init__(self, *args, **kwargs):
        pass


class Forbidden(Exception):
    code = 403

    def __init__(self, *args, **kwargs):
        pass


class InternalServerError(Exception):
    code = 500

    def __init__(self, *args, **kwargs):
        pass
