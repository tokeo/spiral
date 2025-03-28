from cement import ex  # noqa: F401
from cement.utils.version import get_version_banner as cement_version_banner
from tokeo.ext.argparse import Controller
from tokeo.core.version import get_version as tokeo_get_version
from ..core.version import get_version

DESCRIPTION = """Spiral is easily crafted with Tokeo and is the example app!"""
CEMENT_VERSION, PYTHON_VERSION, OS_VERSION = (cement_version_banner().split('\n') + ['unknown', 'unknown', 'unknown'])[:3]
VERSION_BANNER = f"""
 
┃
┃   {DESCRIPTION}
┃
┃   ✨ Spiral CLI {get_version()} ✨
┃   Crafted with 🚀 Tokeo {tokeo_get_version()}
┃
┃   🔧 Built on {CEMENT_VERSION}
┃   🐍 Powered by {PYTHON_VERSION}
┃   💻 Running on {OS_VERSION}
┃
"""


class BaseController(Controller):

    class Meta:
        label = 'base'

        # disable the ugly curly command doubled listening
        subparser_options = dict(metavar='')

        # text displayed at the top of --help output
        description = DESCRIPTION

        # text displayed at the bottom of --help output
        epilog = 'Example: spiral command --option --param value'

        # short help is empty on base
        help = ''

        # controller level arguments. ex: 'spiral --version'
        arguments = [
            # add a version banner
            (
                ['-v', '--version'],
                dict(
                    action='version',
                    version=VERSION_BANNER,
                ),
            ),
        ]
