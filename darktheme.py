# Copyright © 2015-2023 Fern Zapata
# This program is subject to the terms of the GNU GPL, version 3
# or, at your option, any later version. If a copy of it was not
# included with this file, see https://www.gnu.org/licenses/.

from gi.repository import Gedit, GObject, Gtk


class GeditDarkThemePlugin(GObject.Object, Gedit.AppActivatable):
    app = GObject.Property(type=Gedit.App)
    prop = "gtk-application-prefer-dark-theme"

    def __init__(self):
        super().__init__()
        self.settings = Gtk.Settings.get_default()
        self._shutting_down = False

    def do_activate(self):
        self._orig = self.settings.get_property(self.prop)
        self.settings.set_property(self.prop, True)

        self._id_shutdown = self.app.connect("shutdown", self.on_shutdown)

    def do_deactivate(self):
        self.app.disconnect(self._id_shutdown)
        if not self._shutting_down:
            self.settings.set_property(self.prop, self._orig)

    def on_shutdown(self, *_):
        self._shutting_down = True
