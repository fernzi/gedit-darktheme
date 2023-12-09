# Copyright © 2015-2023 Fern Zapata
# This program is subject to the terms of the GNU GPL, version 3
# or, at your option, any later version. If a copy of it was not
# included with this file, see https://www.gnu.org/licenses/.

from gi.repository import GObject, Gtk, Gedit

class GeditDarkThemePlugin(GObject.Object, Gedit.AppActivatable):

  app  = GObject.Property(type=Gedit.App)
  prop = 'gtk-application-prefer-dark-theme'

  def __init__(self):
    super().__init__()
    self.settings = Gtk.Settings.get_default()

  def do_activate(self):
    self._orig = self.settings.get_property(self.prop)
    self.settings.set_property(self.prop, True)

  def do_deactivate(self):
    self.settings.set_property(self.prop, self._orig)
