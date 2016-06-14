
from configparser import ConfigParser

CONFIG_FILE = 'settings.cfg'

app_config = ConfigParser()
app_config.read(CONFIG_FILE)
print(app_config.sections())
