from flask_env import MetaFlaskEnv


class StaticConfiguration:
    APP_NAME = 'kamko/og-proxy'
    VERSION = '0.0.1'
    USER_AGENT = f'{APP_NAME}:{VERSION}'


class AppConfiguration(metaclass=MetaFlaskEnv):
    DEBUG = False
