from course.common.configuration.config_parser import power_config
from course.models_service.models.models_object import model_lock, pd


def is_session_effective():
    with model_lock:
        if pd.get_session(power_config.get_config('config', 'SESSION_TIMEOUT', int)):
            pd.update_session()
            return True
        return False


def update_session():
    with model_lock:
        pd.update_session()


def clear_session():
    with model_lock:
        pd.clear_session()
