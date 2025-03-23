"""
Spiral main module providing CLI application framework.

This module defines the main Spiral application classes and
entry point. It leverages the Cement framework to create a robust and
extensible CLI application with support for various extensions and handlers.

"""

import os
from cement import App, TestApp
from cement.utils import fs
from cement.core.exc import CaughtSignal
from .core.exc import SpiralError
from .controllers.base import BaseController
from .controllers.emit import EmitController
from .controllers.grpccall import GrpcCallController


class Spiral(App):
    """
    The Spiral CLI application core class.

    Extends the Cement App class to provide a configurable and extensible
    CLI application framework. Spiral applications use the
    Cement framework for command-line parsing, configuration management,
    logging, and more.

    ### Notes:

    - The application includes several extensions by default:
        colorlog, generate, pdoc, print, jinja2, yaml and others
    - The application's configuration is loaded from YAML files
    - Signal handling (SIGINT, SIGTERM) is automatically managed

    """

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
            'tokeo.ext.pdoc',
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
    """
    A specialized subclass of Spiral designed for testing purposes.

    This class extends both TestApp from the Cement framework and
    the Spiral application class to provide a testing environment
    for Spiral applications. It modifies various settings to be more
    suitable for automated testing.

    ### Usage:

    ```python
    # Basic test setup
    from .main import SpiralTest

    with SpiralTest() as app:
        app.run()
        # Perform assertions on app state

    ```

    ### Notes:

    - Uses standard logging instead of colorlog for cleaner test output
    - Includes a smaller set of extensions to reduce test complexity
    - Appends '_test' to the app label to distinguish from production instances

    """

    class Meta:
        # this app test name
        label = f'{Spiral.Meta.label}_test'


def dramatiq():
    """
    Entry point for Dramatiq worker processes.

    This function initializes the application with Dramatiq configuration
    and settings when the application is started as a Dramatiq worker.
    It sets up the necessary environment without running the full
    CLI application stack.

    ### Used by Spiral CLI for the dramatiq workers:

    ```bash
    spiral dramatiq serve
    ```

    ### Notes:

    - Initializes the application without command processing
    - Disables signal handling as Dramatiq manages its own signals
    - Sets up configuration, handlers, and hooks for task processing
    - Does not block or run the event loop (Dramatiq handles that)
    - Dramatiq will find and register all tasks automatically

    """
    # instantiate app to get config etc. when starting as module via dramatiq
    app = Spiral()
    # disable signal catching when started as module by dramatiq
    app._meta.catch_signals = None
    # run setup to inintializes config, handlers and hooks
    app.setup()


def main():
    """
    Main entry point for the Spiral application.

    Creates a Spiral application instance, runs it, and handles
    any exceptions that may occur during execution. This function serves as
    the primary entry point when running Spiral as
    a command-line application.

    ### Returns:

    - **int**: Exit code indicating success (0) or failure (non-zero)

    ### Raises:

    - **AssertionError**: When an assertion fails during application execution
    - **SpiralError**: When a Spiral-specific
        error occurs
    - **CaughtSignal**: When a signal (e.g., SIGINT, SIGTERM) is caught

    """
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
