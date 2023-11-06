#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import gtk
import appindicator

class AddadIndicator:
	def __init__(self, window):

		self.window = window

		self.indicator = appindicator.Indicator ("example-simple-client", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
		self.indicator.set_status (appindicator.STATUS_ACTIVE)
		self.indicator.set_icon("addad-ind")

		self.indicator_menu = gtk.Menu()
        
		show_hide_addad = gtk.MenuItem("Show/Hide Addad")
		show_hide_addad.connect("activate", self.show_hide_addad)
		self.indicator_menu.append(show_hide_addad)

		choose_timer_menu = gtk.MenuItem("Choose timer monitor")
		timer_submenu = gtk.Menu()


		stopwatch_button = gtk.RadioMenuItem(None, "StopWatch")
		stopwatch_button.connect("toggled", self.callback, "StopWatch")
		countdown_button = gtk.RadioMenuItem(stopwatch_button, "Time Countdown")
		countdown_button.connect("toggled", self.callback, "Time Countdown")
		pomodoro_button = gtk.RadioMenuItem(stopwatch_button, "Pomodoro Technique")
		pomodoro_button.connect("toggled", self.callback, "Pomodoro Technique")
		pomodoro_button.set_active(True)

		none_button = gtk.RadioMenuItem(stopwatch_button, "None")
		none_button.connect("toggled", self.callback, "None")

		timer_submenu.append(none_button)
		timer_submenu.append(stopwatch_button)
		timer_submenu.append(countdown_button)
		timer_submenu.append(pomodoro_button)  

		choose_timer_menu.set_submenu(timer_submenu)
		self.indicator_menu.append(choose_timer_menu)


		aboutaddad = gtk.MenuItem("About")
		aboutaddad.connect("activate", self.about_addad)
		self.indicator_menu.append(aboutaddad)

		close_addad = gtk.MenuItem("Quit")
		close_addad.connect("activate", self.quit)
		self.indicator_menu.append(close_addad)



		self.indicator_menu.show_all()

		self.indicator.set_menu(self.indicator_menu)

		self.hide_addad = []
		self.hide_addad.append(False)


	def showtimer(self, s, m, h, monitor):

		if self.activated_button == monitor :
			vary = "%02d : %02d : %02d" %(h, m, s)
			self.indicator.set_label(vary)


	def callback(self, widget, data):
		self.activated_button = data
		if self.activated_button == "None" :
			vary = ""
			self.indicator.set_label(vary)

	def show_hide_addad(self, widget):

		if self.hide_addad[0] == False :
			self.window.hide_all()
			self.hide_addad[0] = True

		else :
			self.window.show_all()
			self.hide_addad[0] = False


	def quit(self, widget):
		gtk.main_quit()


	def about_addad(self, widget):
		about = gtk.AboutDialog()
		about.set_program_name("Addad - عدّاد ")
		about.set_version("3.0")
		about.set_comments("Addad is a nice app used as StopWatch and Time Countdown")
		about.set_copyright("Developed by : Ahmed Fawzy - ahmed.linuxawy@gmail.com")
		about.set_website("http://www.Khawarzmy.blogspot.com")

		image_dir1 = os.path.dirname(os.path.abspath(__file__))
		f = open(image_dir1 + "/gpl.txt", "r")
		read_license = f.readlines()
		license = ' '.join(read_license)
		f.close()

		licenses = '''Addad is licensed under GPL V3 License http://www.gnu.org/licenses/gpl.html
Source of alarm sound is ' http://www.freesound.org/people/jackstrebor/sounds/34853/ ' .

The Text of GPL V3 License ::

%s  ''' %license

		about.set_license(licenses)

		image_dir = os.path.dirname(os.path.abspath(__file__))
		about.set_logo(gtk.gdk.pixbuf_new_from_file(image_dir + "/addad-logo.png"))

		about.run()
		about.destroy()


