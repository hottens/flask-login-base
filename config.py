import configparser
config = configparser.ConfigParser()

config['FLASK'] = {
    'SECRET_KEY': 42,
    'DATABASE_URL': 'sqlite:///db.sqlite'
}

with open('config.ini', 'w') as configfile:
  config.write(configfile)