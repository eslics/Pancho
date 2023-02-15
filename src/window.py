from gi.repository import Gtk


@Gtk.Template(resource_path='/io/github/eslics/Pancho/window.ui')
class PanchoWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'PanchoWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

