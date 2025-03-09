import os
from cement import App, TestApp
from cement.utils import fs
from cement.core.exc import CaughtSignal
from .core.exc import SpiralError
from .controllers.base import BaseController
from .controllers.emit import EmitController
from .controllers.grpccall import GrpcCallController


class Spiral(App):
    """The Spiral primary application."""

    class Meta:
        # this app name
        label = 'spiral'

        # this app main path
        main_dir = os.path.dirname(fs.abspath(__file__))

        # configuration defaults
        config_defaults = dict(
            debug=False,
        )

        # call sys.exit() on close
        exit_on_close = True

        # load additional framework extensions
        extensions = [
            'colorlog',
            'tokeo.ext.yaml',
            'tokeo.ext.appenv',
            'tokeo.ext.print',
            'tokeo.ext.jinja2',
            'tokeo.ext.appshare',
            'tokeo.ext.smtp',
            'tokeo.ext.diskcache',
            'tokeo.ext.dramatiq',
            'tokeo.ext.grpc',
            'tokeo.ext.scheduler',
            'tokeo.ext.nicegui',
            'tokeo.ext.pocketbase',
            'tokeo.ext.automate',
        ]

        # register handlers
        handlers = [
            BaseController,
            EmitController,
            GrpcCallController,
        ]

        # configuration file suffix
        config_file_suffix = '.yaml'

        # set the log handler
        log_handler = 'colorlog'


class SpiralTest(TestApp, Spiral):
    """A sub-class of Spiral that is better suited for testing."""

    class Meta:
        # this app test name
        label = f'{Spiral.Meta.label}_test'


def dramatiq():
    # instantiate app to get config etc. when starting as module via dramatiq
    app = Spiral()
    # disable signal catching when started as module by dramatiq
    app._meta.catch_signals = None
    # run setup to inintializes config, handlers and hooks
    app.setup()


def main():
    with Spiral() as app:
        try:
            app.run()

        except AssertionError as e:
            print(f'AssertionError > {e.args[0]}')
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except SpiralError as e:
            print(f'SpiralError > {e.args[0]}')
            app.exit_code = 1

            if app.debug is True:
                import traceback

                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            if e.signum == 2:
                print('\nstopped by Ctrl-C')
            elif e.signum == 15:
                print('\nterminated by SIGTERM')
            else:
                print(f'\n{e}')
            app.exit_code = 0


if __name__ == '__main__':
    main()
