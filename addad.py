#!/usr/bin/python
# -*- coding: utf-8 -*-

# Addad program 'عدّاد' 
# Version: 3.0
# Description: A simple app used as Stopwatch and Time Countdown

# License: Addad program is licensed under is licensed GPL license
# http://www.gnu.org/licenses/gpl.html

import addadindicator
import gtk
import gobject
import pango
import alarm
import os
import pynotify


button_setting = gtk.settings_get_default()
button_setting.set_property("gtk-button-images", True)


class PyApp(gtk.Window): 

	def __init__(self):
		super(PyApp, self).__init__()

		self.set_size_request(430, 280)
		self.set_position(gtk.WIN_POS_CENTER)
		self.connect("destroy", gtk.main_quit)
		self.set_title("عدّاد - Stop Watch & Time CountDown")
		image_dir = os.path.dirname(os.path.abspath(__file__))
		self.set_icon_from_file(image_dir + "/addad-logo.png")

		self.import_indicator = addadindicator.AddadIndicator(self)

		self.seconds = 0
		self.minutes = 0
		self.hours = 0

		self.st = []
		self.st.append(False)

# --- timer monitor ---

		self.stopwatch_monitor = "StopWatch"
		self.countdown_monitor = "Time Countdown"
		self.pomodoro_monitor = "Pomodoro Technique"

#----------------------


		table = gtk.Table(1,1,gtk.FALSE)
		self.add(table)

		notebook = gtk.Notebook()
		notebook.set_tab_pos(gtk.POS_TOP)
		table.attach(notebook, 0,6,0,1)
		notebook.show()
		self.show_tabs = gtk.TRUE
		self.show_border = gtk.TRUE

		stopwatch_frame = gtk.Frame('StopWatch')
		stopwatch_frame.set_border_width(10)
		stopwatch_frame.set_size_request(100, 75)
		stopwatch_frame.show()

		stopwatch_label = gtk.Label('StopWatch')
		notebook.append_page(stopwatch_frame, stopwatch_label)

		countdown_frame = gtk.Frame('Time CountDown')
		countdown_frame.set_border_width(10)
		countdown_frame.set_size_request(100, 100)
		countdown_frame.show()

		countdown_label = gtk.Label('Time CountDown')
		notebook.append_page(countdown_frame, countdown_label)


		pomodoro_frame = gtk.Frame('Pomodoro Tech.')
		pomodoro_frame.set_border_width(10)
		pomodoro_frame.set_size_request(100, 100)
		pomodoro_frame.show()

		pomodoro_label = gtk.Label('Pomodoro Tech.')
		notebook.append_page(pomodoro_frame, pomodoro_label)


# Stopwatch "Section"

		image1 = gtk.Image()
		image1.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		self.button_start = gtk.Button("Start")
		self.button_start.set_image(image1)
		self.button_start.set_size_request(90, 35)      
		self.button_start.connect("clicked", self.started)

		self.button_pause = gtk.Button(stock=gtk.STOCK_MEDIA_PAUSE)
		self.button_pause.set_size_request(90, 35)      
		self.button_pause.connect("clicked", self.paused)

		self.button_reset = gtk.Button("Reset")
		self.button_reset.set_size_request(90, 35)      
		self.button_reset.connect("clicked", self.reset)

		self.button_pause.set_sensitive(False)
		self.button_reset.set_sensitive(False)

		self.button_about = gtk.Button(stock=gtk.STOCK_ABOUT)
		self.button_about.set_size_request(80, 35)      
		self.button_about.connect("clicked", self.about_addad)

		self.Timer = gtk.Label(" 00 : 00 : 00 ")
		TimerFont = pango.FontDescription("Ubuntu italic 24")
		self.Timer.modify_font(TimerFont)

		stopwatch_fix = gtk.Fixed()
		stopwatch_fix.put(self.button_start, 50, 90)
		stopwatch_fix.put(self.button_pause, 160, 90)
		stopwatch_fix.put(self.button_reset, 270, 90)
		stopwatch_fix.put(self.button_about, 315, 165)
		stopwatch_fix.put(self.Timer, 120, 25)

		stopwatch_frame.add(stopwatch_fix)

# Time CountDown "Section"

		self.down_sec = 0
		self.down_min = 0
		self.down_hour = 0

		self.countdown_run = []
		self.countdown_run.append(False)

		image2 = gtk.Image()
		image2.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		self.btn_start_down = gtk.Button('Start')
		self.btn_start_down.set_image(image2)
		self.btn_start_down.set_size_request(90, 35)      
		self.btn_start_down.connect("clicked", self.start_countdown)

		self.btn_pause_down = gtk.Button(stock=gtk.STOCK_MEDIA_PAUSE)
		self.btn_pause_down.set_size_request(90, 35)      
		self.btn_pause_down.connect("clicked", self.pause_countdown)

		self.btn_reset_down = gtk.Button("Reset")
		self.btn_reset_down.set_size_request(90, 35)      
		self.btn_reset_down.connect("clicked", self.reset_countdown)

		self.btn_pause_down.set_sensitive(False)
		self.btn_reset_down.set_sensitive(False)

		button_about = gtk.Button(stock=gtk.STOCK_ABOUT)
		button_about.set_size_request(80, 35)      
		button_about.connect("clicked", self.about_addad)

		self.CountDown = gtk.Label(" 00 : 00 : 00 ")
		CountDownFont = pango.FontDescription("Ubuntu italic 24")
		self.CountDown.modify_font(CountDownFont)

		timer_text = gtk.Label("Popular Timers") 
		timer_box = gtk.combo_box_new_text()
		timer_box.connect("changed", self.on_changed)

		timer_box.append_text('10 minutes')
		timer_box.append_text('15 minutes')
		timer_box.append_text('20 minutes')
		timer_box.append_text('30 minutes')
		timer_box.append_text('1 hour')

		hour_up_down = gtk.Label("Hours") 
		min_up_down = gtk.Label("Mins") 
		sec_up_down = gtk.Label("Secs") 

		hour_btn_up = gtk.ToolButton(gtk.STOCK_GO_UP)
		min_btn_up = gtk.ToolButton(gtk.STOCK_GO_UP)
		sec_btn_up = gtk.ToolButton(gtk.STOCK_GO_UP)

		hour_btn_up.connect("clicked", self.inc_hour)
		min_btn_up.connect("clicked", self.inc_min)
		sec_btn_up.connect("clicked", self.inc_sec)

		hour_btn_down = gtk.ToolButton(gtk.STOCK_GO_DOWN)
		min_btn_down = gtk.ToolButton(gtk.STOCK_GO_DOWN)
		sec_btn_down = gtk.ToolButton(gtk.STOCK_GO_DOWN)

		hour_btn_down.connect("clicked", self.dec_hour)
		min_btn_down.connect("clicked", self.dec_min)
		sec_btn_down.connect("clicked", self.dec_sec)

		vbox = gtk.VBox() 
		hbox1 = gtk.HBox()
		hbox2 = gtk.HBox()
		hbox3 = gtk.HBox()

		hbox1.pack_start(hour_up_down, True, True, 10)
		hbox1.pack_start(min_up_down, True, True, 10)
		hbox1.pack_start(sec_up_down, True, True, 10)

		hbox2.pack_start(hour_btn_up, True, True, 10)
		hbox2.pack_start(min_btn_up, True, True, 10)
		hbox2.pack_start(sec_btn_up, True, True, 10)

		hbox3.pack_start(hour_btn_down, True, True, 10)
		hbox3.pack_start(min_btn_down, True, True, 10)
		hbox3.pack_start(sec_btn_down, True, True, 10)

		vbox.pack_start(hbox1)
		vbox.pack_start(hbox2)
		vbox.pack_start(hbox3)

		countdown_fix = gtk.Fixed()
		countdown_fix.put(self.CountDown, 50, 15)
		countdown_fix.put(vbox, 50, 70)
		countdown_fix.put(self.btn_start_down, 270, 20)
		countdown_fix.put(self.btn_pause_down, 270, 65)
		countdown_fix.put(self.btn_reset_down, 270, 110)
		countdown_fix.put(timer_text, 30, 170)
		countdown_fix.put(timer_box, 150, 165)
		countdown_fix.put(button_about, 315, 165)

		countdown_frame.add(countdown_fix)


# Pomodoro Tech.  "Section"

		
		self.pomo_sec, self.pomo_min, self.pomo_hour = 0, 0, 0

		self.pomodoro_run = []
		self.pomodoro_run.append(False)

		self.counter = 1
		self.sessions_sum = 0

		self.button_session = gtk.Button("Session")
		self.button_session.set_size_request(100, 40)      
		self.button_session.connect("clicked", self.start_session)

		self.button_sh_break = gtk.Button("Short Break")
		self.button_sh_break.set_size_request(100, 40)      
		self.button_sh_break.connect("clicked", self.short_break)

		self.button_lg_break = gtk.Button("Long Break")
		self.button_lg_break.set_size_request(100, 40)      
		self.button_lg_break.connect("clicked", self.long_break)


		self.button_sh_break.set_sensitive(False)
		self.button_lg_break.set_sensitive(False)

		self.Pomo_Timer = gtk.Label(" 00 : 00 : 00 ")
		Pomo_TimerFont = pango.FontDescription("Ubuntu italic 28")
		self.Pomo_Timer.modify_font(Pomo_TimerFont)

		self.sessions_total = gtk.Label("No. of work sessions :	0") 
		self.shortbreak_total = gtk.Label("No. of short breaks  :		0") 
		self.longbreak_total = gtk.Label("No. of long breaks   :		0") 

		pomodoro_fix = gtk.Fixed()
		pomodoro_fix.put(self.button_session, 35, 30)
		pomodoro_fix.put(self.button_sh_break, 150, 30)
		pomodoro_fix.put(self.button_lg_break, 265, 30)
		pomodoro_fix.put(self.Pomo_Timer, 100, 85)
		pomodoro_fix.put(self.sessions_total, 40, 140)
		pomodoro_fix.put(self.shortbreak_total, 40, 160)
		pomodoro_fix.put(self.longbreak_total, 40, 180)
		pomodoro_frame.add(pomodoro_fix)


# ------------------------
		self.show_all()
# -------------------------

# --- Stopwatch Functions ---

	def stopwatch(self):

		if self.st[0] == True :

			self.seconds += 1
			if (self.seconds == 60):
				self.seconds = 0
				self.minutes += 1
			if (self.minutes == 60):
				self.minutes = 0
				self.hours += 1

			self.Timer.set_text(" %02d : %02d : %02d " %(self.hours, self.minutes, self.seconds) )
			self.import_indicator.showtimer(self.seconds, self.minutes, self.hours, self.stopwatch_monitor)

			return True

		elif self.st[0] == False :
			return False

	def started(self, widget):
		if self.st[0] == False :
			self.st[0] = True
			gobject.timeout_add(1000, self.stopwatch )
			self.button_pause.set_sensitive(True)
			self.button_reset.set_sensitive(True)

	def paused(self, widget):
		self.st[0] = False
		self.Timer.set_text(" %02d : %02d : %02d " %(self.hours, self.minutes, self.seconds) )

		image3 = gtk.Image()
		image3.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		self.button_start.set_label('Resume')
		self.button_start.set_image(image3)
	
	def reset(self, widget):
		self.st[0] = False
		self.seconds, self.minutes, self.hours = 0, 0, 0
		self.Timer.set_text(" %02d : %02d : %02d " %(self.hours, self.minutes, self.seconds) )

		image3 = gtk.Image()
		image3.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		self.button_start.set_label('Start')
		self.button_start.set_image(image3)

		self.button_pause.set_sensitive(False)
		self.button_reset.set_sensitive(False)


# --- CountDown Functions ---

	def time_countdown(self):

		if self.countdown_run[0] == True :

			if self.down_sec == 0:

				if self.down_min == 0:

					if self.down_hour == 0:
						self.countdown_run[0] = False
						alarm.Alarm()
						return False

					elif self.down_hour > 0 :
						self.down_hour -= 1
						self.down_min = 59
						self.down_sec = 59
		
				elif self.down_min > 0:
					self.down_min -= 1
					self.down_sec = 59
		
			elif self.down_sec > 0 :
				self.down_sec -= 1

			self.CountDown.set_text(" %02d : %02d : %02d " %(self.down_hour, self.down_min, self.down_sec) )
			self.import_indicator.showtimer(self.down_sec, self.down_min, self.down_hour, self.countdown_monitor)
			return True

		elif self.countdown_run[0] == False :
			return False

			
	def start_countdown(self, widget):
		if self.countdown_run[0] == False :
			if self.down_hour != 0 or self.down_min != 0 or self.down_sec != 0 :
				self.countdown_run[0] = True
				gobject.timeout_add(1000, self.time_countdown)

				self.btn_pause_down.set_sensitive(True)
				self.btn_reset_down.set_sensitive(True)

	def pause_countdown(self, widget):
		self.countdown_run[0] = False
		self.update_CountDown()

		image3 = gtk.Image()
		image3.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		self.btn_start_down.set_label('Resume')
		self.btn_start_down.set_image(image3)

	def reset_countdown(self, widget):
		self.countdown_run[0] = False
		self.down_sec, self.down_min, self.down_hour = 0, 0, 0
		self.update_CountDown()

		image3 = gtk.Image()
		image3.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		self.btn_start_down.set_label('Start')
		self.btn_start_down.set_image(image3)

		self.btn_pause_down.set_sensitive(False)
		self.btn_reset_down.set_sensitive(False)

	def inc_hour(self, widget):
		if ( self.down_hour + 1 ) == 24 :
			self.update_CountDown()
		else :
			self.down_hour += 1
			self.update_CountDown()

	def inc_min(self, widget):
		if (self.down_min + 1) == 60 :
			self.update_CountDown()
		else :
			self.down_min += 1
			self.update_CountDown()

	def inc_sec(self, widget):
		if (self.down_sec + 1) == 60 :
			self.update_CountDown()
		else :
			self.down_sec += 1
			self.update_CountDown()


	def dec_hour(self, widget):
		if (self.down_hour - 1) < 0 :
			self.update_CountDown()
		else :
			self.down_hour -= 1
			self.update_CountDown()

	def dec_min(self, widget):
		if (self.down_min - 1) < 0 :
			self.update_CountDown()
		else :
			self.down_min -= 1
			self.update_CountDown()

	def dec_sec(self, widget):
		if (self.down_sec - 1) < 0 :
			self.update_CountDown()
		else :
			self.down_sec -= 1
			self.update_CountDown()

	def update_CountDown(self):

		self.CountDown.set_text(" %02d : %02d : %02d " %(self.down_hour, self.down_min, self.down_sec) )


	def on_changed(self, widget):
		distros = ['10 minutes','15 minutes','20 minutes','30 minutes','1 hour']

		i =str( widget.get_active_text() )

		if distros.index(i) == 0 :
			self.down_sec, self.down_min, self.down_hour = 0, 10, 0

		elif distros.index(i) == 1 :
			self.down_sec, self.down_min, self.down_hour = 0, 15, 0

		elif distros.index(i) == 2 :
			self.down_sec, self.down_min, self.down_hour = 0, 20, 0

		elif distros.index(i) == 3 :
			self.down_sec, self.down_min, self.down_hour = 0, 30, 0

		elif distros.index(i) == 4 :
			self.down_sec, self.down_min, self.down_hour = 0, 0, 1

		self.CountDown.set_text(" %02d : %02d : %02d " %(self.down_hour, self.down_min, self.down_sec) )


# --- Pomodoro Tech. Functions ---

	def start_session(self, widget):

		if self.pomodoro_run[0] == False :
			self.pomo_min = 25
			self.notify()
			self.pomodoro_run[0] = True
			gobject.timeout_add(1000, self.pomodoro_timer)


	def short_break(self, widget):

		if self.pomodoro_run[0] == False :
			self.pomo_min = 5
			self.notify()
			self.pomodoro_run[0] = True
			gobject.timeout_add(1000, self.pomodoro_timer)


	def long_break(self, widget):

		if self.pomodoro_run[0] == False :
			self.pomo_min = 15
			self.notify()
			self.pomodoro_run[0] = True
			gobject.timeout_add(1000, self.pomodoro_timer)


	def pomodoro_timer(self):

		if self.pomodoro_run[0] == True :

			if self.pomo_sec == 0:

				if self.pomo_min == 0:

					if self.pomo_hour == 0:
						self.pomodoro_run[0] = False
						self.switch_pondera()
						return False

					elif self.pomo_hour > 0 :
						self.pomo_hour -= 1
						self.pomo_min = 59
						self.pomo_sec = 59
		
				elif self.pomo_min > 0:
					self.pomo_min -= 1
					self.pomo_sec = 59
		
			elif self.pomo_sec > 0 :
				self.pomo_sec -= 1

			self.Pomo_Timer.set_text(" %02d : %02d : %02d " %(self.pomo_hour, self.pomo_min, self.pomo_sec) )
			self.import_indicator.showtimer(self.pomo_sec, self.pomo_min, self.pomo_hour, self.pomodoro_monitor)

			return True

		elif self.pomodoro_run[0] == False :
			return False


	def switch_pondera(self):

			if (self.counter % 8) == 0 :
				self.longbreak_sum = self.counter / 8
				self.longbreak_total.set_text("No. of long breaks :		%d " %(self.longbreak_sum) )
				self.button_session.set_sensitive(True)
				self.button_lg_break.set_sensitive(False)

				text_alarm = " Your long break ended, go back to your work ^_^"
				alarm.PomoAlarm(text_alarm)

			elif (self.counter % 2) == 0 :
				self.shortbreak_sum = self.counter / 2
				self.shortbreak_total.set_text("No. of short breaks :		%d " %(self.shortbreak_sum) )
				self.button_session.set_sensitive(True)
				self.button_sh_break.set_sensitive(False)

				text_alarm = " Your short break ended, go back to your work ^_^"
				alarm.PomoAlarm(text_alarm)

			else:
				self.sessions_sum += 1
				self.sessions_total.set_text("No. of work sessions :	%d " %(self.sessions_sum) )

				if ((self.counter + 1) % 8 == 0) :
					self.button_session.set_sensitive(False)
					self.button_lg_break.set_sensitive(True)

					text_alarm = " Take a long break, you worked very hard, enjoy ^_^"
					alarm.PomoAlarm(text_alarm)


				else:
					self.button_session.set_sensitive(False)
					self.button_sh_break.set_sensitive(True)

					text_alarm = " Take a short break to refresh yourself, enjoy ^_^"
					alarm.PomoAlarm(text_alarm)


			self.counter += 1


	def notify(self):

		pynotify.init("Pomodoro Technique")

		if self.pomo_min == 25 :

			n = pynotify.Notification(
		        "Pomodoro Technique",
	    	    " Work Session begins",
	    	    "addad-ind")

		elif self.pomo_min == 5 or self.pomo_min == 15 :

			n = pynotify.Notification(
		        "Pomodoro Technique",
	    	    " Break Time begins",
	    	    "addad-ind")

		n.show()


# --- About function ---

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


#-----------------------
PyApp()
gtk.main()
