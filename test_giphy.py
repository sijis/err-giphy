import giphy

pytest_plugins = ["errbot.backends.test"]
extra_plugin_dir = '.'

class TestMyPluginBot(object):
    extra_plugin_dir = '.'

    def test_giphy(self, testbot):
        testbot.push_message('!giphy')
        assert 'No results found.' in testbot.pop_message()

    def test_giphy_ids(self, testbot):
        testbot.push_message('!giphy_ids HyoZkHKDJxGms')
        assert 'http://media0.giphy.com/media/HyoZkHKDJxGms/giphy.gif' in testbot.pop_message()
