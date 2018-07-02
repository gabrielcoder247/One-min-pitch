class Config:
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa2018:12345@localhost/gabpitch'



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

# config_options ={
#     'development':DevConfig,
#     'production':ProdConfig,
#     'test':TestConfig
# }