#!/usr/bin/env python
# Copyright 2016 Franz Zapata
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

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
