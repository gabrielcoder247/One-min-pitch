class Config:

    SECRET_KEY = 'SECRET'
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://gabrielcoder:12345@localhost/gabpitch'
    '''
    General configuration parent class
    '''
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig,
    # 'test':TestConfig
}