class Config:
<<<<<<< HEAD
   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa2018:12345@localhost/gabpitch'
=======
    '''
    General configuration parent class
    '''
    pass
>>>>>>> e093d9df398ee9518dc278a60a359257df126007



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