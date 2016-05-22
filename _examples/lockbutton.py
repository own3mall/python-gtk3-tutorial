#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject
from gi.repository import Polkit
from gi.repository import Gio
import os

def check_authorization(lockbutton):
    authority.check_authorization(subject, action_id, None, Polkit.CheckAuthorizationFlags.ALLOW_USER_INTERACTION, cancellable, check_authorization_cb, mainloop)

def check_authorization_cb(authority, res, loop):
    try:
        result = authority.check_authorization_finish(res)
        if result.get_is_authorized():
            print("Authorized")
        elif result.get_is_challenge():
            print("Challenge")
        else:
            print("Not authorized")
    except GObject.GError as error:
         print("Error checking authorization: %s" % error.message)

if __name__ == "__main__":
    action_id = "org.freedesktop.policykit.exec"

    mainloop = GObject.MainLoop()
    authority = Polkit.Authority.get()
    cancellable = Gio.Cancellable()
    subject = Polkit.UnixProcess.new(os.getppid())

    window = Gtk.Window()
    window.connect("destroy", Gtk.main_quit)

    lockbutton = Gtk.LockButton()
    lockbutton.connect("clicked", check_authorization)
    window.add(lockbutton)

    window.show_all()

    mainloop.run()
