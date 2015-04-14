from errbot import BotPlugin, botcmd

import requests
import random
import logging

log = logging.getLogger(name='errbot.plugins.Giphy')

class Giphy(BotPlugin):

    def get_configuration_template(self):
        """ configuration entries """
        config = {
            'api_key': '',
        }
        return config

    def _check_config(self, option):

        # if no config, return nothing
        if self.config is None:
            return None
        else:
            # now, let's validate the key
            if option in self.config:
                return self.config[option]
            else:
                return None

    @botcmd
    def giphy(self, msg, args):
        """ Return a gif based on search """

        api_key = self._check_config('api_key') or 'dc6zaTOxFJmzC'
        gif_size = 'original'
        max_image_size = 8000000

        params = {
            'q': args,
            'limit': 100,
            'api_key': api_key,
        }

        r = requests.get('http://api.giphy.com/v1/gifs/search', params=params)
        log.debug('url sent: {}'.format(r.url))

        results = r.json()
        results_count = len(results['data'])
        log.debug('results found: {}'.format(results_count))

        if results_count != 0:
            response = None
            while response is None:
                image_number = random.randrange(0, results_count)
                image_size = results['data'][image_number]['images'][gif_size]['size']
                # Restricting to max size limit
                if image_size < max_image_size:
                    response = results['data'][image_number]['images'][gif_size]['url']
        else:
            response = 'No results found.'

        self.send(msg.frm,
                  response,
                  message_type=msg.type,
                  in_reply_to=msg,
                  groupchat_nick_reply=True)
