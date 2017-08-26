#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gi.repository import Gtk
import sugargame
import sugargame.canvas
from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityToolbarButton
from sugar3.graphics.toolbutton import ToolButton
from sugar3.activity.widgets import StopButton
from gettext import gettext as _
import main

class Activity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.max_participants = 1
        self.actividad = main.game()
        self.build_toolbar()
        self._pygamecanvas = sugargame.canvas.PygameCanvas(self)
        self.set_canvas(self._pygamecanvas)
        self._pygamecanvas.grab_focus()
        self._pygamecanvas.run_pygame(self.actividad.make)

    def build_toolbar(self):

        toolbar_box = ToolbarBox()
        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.show_all()

