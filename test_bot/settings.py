import sys
import yaml


class Configs:
    def __init__(self, config_file='./config.yaml'):
        self._conf_file = config_file
        self.config_dict = self._read_config()

    def _read_config(self):
        try:
            with open(self._conf_file, 'r') as f:
                return yaml.load(f)
        except FileNotFoundError as err:
            print("Not Found Error: {}".format(err))
            sys.exit(1)
        except IOError as err:
            print("I/O error: {}".format(err))
            sys.exit(1)
        except Exception:
            print("Unexpected error: ", sys.exc_info()[0])
            sys.exit(1)

    def get_telegram_token(self):
        return self.config_dict['telegram']['token']

    def get_proxy_data(self):
        return {
            'proxy_url': self.config_dict['proxy']['url'],
            'urllib3_proxy_kwargs': {
                'username': self.config_dict['proxy']['username'],
                'password': self.config_dict['proxy']['password'],
            },
        }
