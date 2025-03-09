from cement.utils.misc import init_defaults
from spiral.main import SpiralTest


defaults = init_defaults('')


class SpiralTestApp(SpiralTest):

    class Meta:
        # set framework extensions
        extensions = [
            'colorlog',
            'tokeo.ext.yaml',
            'tokeo.ext.appenv',
            'tokeo.ext.print',
            'tokeo.ext.jinja2',
            'tokeo.ext.appshare',
        ]


def test_spiral():
    # test spiral without any subcommands or arguments
    with SpiralTestApp(config_defaults=defaults) as app:
        app.run()
        assert app.exit_code == 0


def test_spiral_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with SpiralTestApp(argv=argv, config_defaults=defaults) as app:
        app.run()
        assert app.debug is True
