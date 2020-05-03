# Copyright © 2015-2020 Fern Zapata
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.

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
