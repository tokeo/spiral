from spiral.main import SpiralTest


def test_spiral():
    # test spiral without any subcommands or arguments
    with SpiralTest() as app:
        app.run()
        assert app.exit_code == 0


def test_spiral_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with SpiralTest(argv=argv) as app:
        app.run()
        assert app.debug is True
