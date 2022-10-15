# The class is created for the configurations
class DevelopmentConfig:
    DEBUG = True
    MYSQL_HOST = 'us-cdbr-east-06.cleardb.net'
    MYSQL_USER = 'bee0e9755133d2'
    MYSQL_PASSWORD = 'f3e9360a'
    MYSQL_DB = 'heroku_23edc9681868d22'


# The configurations are exported as a dictionary
config = {
    'development': DevelopmentConfig
}