#!/usr/bin/python

import gtk
import gst
import os, time
import pynotify

class Alarm(gtk.Window):
	def __init__(self):
		super(Alarm, self).__init__()

# Running Alarm Tone
		self.player = gst.element_factory_make("playbin2", "player")
		fakesink = gst.element_factory_make("fakesink", "fakesink")
		self.player.set_property("video-sink", fakesink)

		file_dir = os.path.dirname(os.path.abspath(__file__))
		filepath = file_dir + "/alarmclock.ogg"

		self.player.set_property("uri", "file://" + filepath)
		self.player.set_state(gst.STATE_PLAYING)

# --- Notification Indicator ---

		pynotify.init("Addad App")
		n = pynotify.Notification(
	        "Addad",
    	    " Time CountDown is Over",
    	    "addad-ind")
		n.show()


# --- Notificaton Dialog box ---

		text = "Timer Countdown is over At %s" %(time.strftime(' %l:%M:%S %p '))
		md = gtk.MessageDialog(self, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, text)
		md.run()
		md.destroy()

		if md.destroy() == None:
			self.player.set_state(gst.STATE_NULL)

