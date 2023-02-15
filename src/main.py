import sys
import gi

gi.require_version('Gtk', '4.0')

from gi.repository import Gtk, Gio
from .window import PanchoWindow


class PanchoApplication(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='io.github.eslics.Pancho',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = PanchoWindow(application=self)
        win.present()


def main(version):
    app = PanchoApplication()
    return app.run(sys.argv)
