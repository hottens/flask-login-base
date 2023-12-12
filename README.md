# flask-login-base
Base Flask App with Login Feature

## How to use
First, git clone into your project. Now you are ready to create your `config.ini` by running the following script:

```
import configparser
config = configparser.ConfigParser()

config['FLASK'] = {
    'SECRET_KEY': 42,
    'DATABASE_URL': 'sqlite:///db.sqlite'
}

with open('config.ini', 'w') as configfile:
  config.write(configfile)
```

Run the Flask application as follows: 
```
flask --app ./<application_name> run
```