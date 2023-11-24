import configparser
import os

config = configparser.ConfigParser()
config_file_path = (
        os.path.dirname(os.path.abspath(__file__)) + os.sep + "data" + os.sep + "config.ini"
)
config.read(config_file_path)

# get all vars and typecast

config_str_square_database_protocol = config.get("ENVIRONMENT", "SQUARE_DATABASE_PROTOCOL")
config_str_square_database_ip = config.get("ENVIRONMENT", "SQUARE_DATABASE_IP")
config_int_square_database_port = int(config.get("ENVIRONMENT", "SQUARE_DATABASE_PORT"))
