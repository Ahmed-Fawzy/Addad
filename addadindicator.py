#!/usr/bin/python
# -*- coding: utf-8 -*-

import addad
import os
import gtk
import appindicator

class AddadIndicator:
	def __init__(self):
		self.indicator = appindicator.Indicator ("example-simple-client", "indicator-messages", appindicator.CATEGORY_APPLICATION_STATUS)
		self.indicator.set_status (appindicator.STATUS_ACTIVE)
		self.indicator.set_icon("addad-ind")

		self.indicator_menu = gtk.Menu()
        
		show_hide_addad = gtk.MenuItem("Show/Hide Addad")
		show_hide_addad.connect("activate", self.show_hide_addad)
		self.indicator_menu.append(show_hide_addad)

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


	def show_hide_addad(self, widget):
		if self.hide_addad[0] == False :
			calling.win.hide_all()
			self.hide_addad[0] = True

		else :
			calling.win.show_all()
			self.hide_addad[0] = False


	def quit(self, widget):
		gtk.main_quit()


	def about_addad(self, widget):
		about = gtk.AboutDialog()
		about.set_program_name("Addad - عدّاد ")
		about.set_version("2.0")
		about.set_comments("Addad is a nice app used as StopWatch and Time Countdown")
		about.set_copyright("Developed by : Ahmed Fawzy - ahmed.linuxawy@gmail.com")
		about.set_website("http://www.Khawarzmy.blogspot.com")

		licenses = ''' Addad is licensed under GPL V3 License http://www.gnu.org/licenses/gpl.html
Source of alarm sound is ' http://www.freesound.org/people/jackstrebor/sounds/34853/ ' .  '''
		about.set_license(licenses)

		image_dir = os.path.dirname(os.path.abspath(__file__))
		about.set_logo(gtk.gdk.pixbuf_new_from_file(image_dir + "/addad-logo.png"))

		about.run()
		about.destroy()


calling = addad.PyApp()
AddadIndicator()
gtk.main()
