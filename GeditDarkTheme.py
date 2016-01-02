#!/usr/bin/env python
# Copyright 2015 Franz Zapata
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy
# of the License at http://www.apache.org/licenses/LICENSE-2.0

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
