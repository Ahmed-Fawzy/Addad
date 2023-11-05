#!/usr/bin/python
# -*- coding: utf-8 -*-

# Addad program 'عدّاد' 
# Version: 1.0
# Description: A simple app used as Stopwatch and Time Countdown

# License: Addad program is licensed under is licensed GPL license
# http://www.gnu.org/licenses/gpl.html

#import addadindicator
import gtk
import gobject
import pango
import alarm
import os

button_setting = gtk.settings_get_default()
button_setting.set_property("gtk-button-images", True)

class PyApp: 
#(gtk.Window)
	def __init__(self):
		#super(PyApp, self).__init__()

		self.win = gtk.Window()

		self.win.set_size_request(430, 280)
		self.win.set_position(gtk.WIN_POS_CENTER)
		self.win.connect("destroy", gtk.main_quit)
		self.win.set_title("عدّاد - Stop Watch & Time CountDown")
		image_dir = os.path.dirname(os.path.abspath(__file__))
		self.win.set_icon_from_file(image_dir + "/addad-logo.png")

		self.aaaaa = "aaaaaaa"


		global seconds, minutes, hours
		seconds, minutes, hours = 0, 0, 0
		self.st = []
		self.st.append(False)

		table = gtk.Table(1,1,gtk.FALSE)
		self.win.add(table)

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

		label = gtk.Label('StopWatch')
		notebook.append_page(stopwatch_frame, label)

		countdown_frame = gtk.Frame('Time CountDown')
		countdown_frame.set_border_width(10)
		countdown_frame.set_size_request(100, 100)
		countdown_frame.show()

		label = gtk.Label('Time CountDown')
		notebook.append_page(countdown_frame, label)


# Stopwatch "Section"

		image1 = gtk.Image()
		image1.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		button_start = gtk.Button("Start")
		button_start.set_image(image1)
		button_start.set_size_request(90, 35)      
		button_start.connect("clicked", self.started)

		button_pause = gtk.Button(stock=gtk.STOCK_MEDIA_PAUSE)
		button_pause.set_size_request(90, 35)      
		button_pause.connect("clicked", self.paused)

		button_reset = gtk.Button("Reset")
		button_reset.set_size_request(90, 35)      
		button_reset.connect("clicked", self.reset)

		button_about = gtk.Button(stock=gtk.STOCK_ABOUT)
		button_about.set_size_request(80, 35)      
		button_about.connect("clicked", self.about_addad)

		self.Timer = gtk.Label(" 00 : 00 : 00 ")
		TimerFont = pango.FontDescription("Ubuntu italic 24")
		self.Timer.modify_font(TimerFont)

		stopwatch_fix = gtk.Fixed()
		stopwatch_fix.put(button_start, 50, 90)
		stopwatch_fix.put(button_pause, 160, 90)
		stopwatch_fix.put(button_reset, 270, 90)
		stopwatch_fix.put(button_about, 315, 165)
		stopwatch_fix.put(self.Timer, 120, 25)

		stopwatch_frame.add(stopwatch_fix)

# Time CountDown  "Section"

		global down_sec, down_min, down_hour
		down_sec, down_min, down_hour = 0, 0, 0

		self.countdown_run = []
		self.countdown_run.append(False)

		image2 = gtk.Image()
		image2.set_from_stock(gtk.STOCK_MEDIA_PLAY,gtk.ICON_SIZE_BUTTON)
		btn_start_down = gtk.Button('Start')
		btn_start_down.set_image(image2)
		btn_start_down.set_size_request(90, 35)      
		btn_start_down.connect("clicked", self.start_countdown)

		btn_pause_down = gtk.Button(stock=gtk.STOCK_MEDIA_PAUSE)
		btn_pause_down.set_size_request(90, 35)      
		btn_pause_down.connect("clicked", self.pause_countdown)

		btn_reset_down = gtk.Button("Reset")
		btn_reset_down.set_size_request(90, 35)      
		btn_reset_down.connect("clicked", self.reset_countdown)

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
		countdown_fix.put(btn_start_down, 270, 20)
		countdown_fix.put(btn_pause_down, 270, 65)
		countdown_fix.put(btn_reset_down, 270, 110)
		countdown_fix.put(timer_text, 30, 170)
		countdown_fix.put(timer_box, 150, 165)
		countdown_fix.put(button_about, 315, 165)

		countdown_frame.add(countdown_fix)

# ------------------------
		self.win.show_all()
# -------------------------

# --- Stopwatch Functions ---

	def stopwatch(self):
		global seconds, minutes, hours

		if self.st[0] == True :

			seconds += 1
			if (seconds == 60):
				seconds = 0
				minutes += 1
			if (minutes == 60):
				minutes = 0
				hours += 1

			self.Timer.set_text(" %02d : %02d : %02d " %(hours, minutes, seconds) )
			return True

		elif self.st[0] == False :
			return False

	def started(self, widget):
		if self.st[0] == False :
			self.st[0] = True
			gobject.timeout_add(1000, self.stopwatch )

	def paused(self, widget):
		self.st[0] = False
		self.Timer.set_text(" %02d : %02d : %02d " %(hours, minutes, seconds) )
		
	def reset(self, widget):
		global seconds, minutes, hours
		self.st[0] = False
		seconds, minutes, hours = 0, 0, 0
		self.Timer.set_text(" %02d : %02d : %02d " %(hours, minutes, seconds) )


# --- CountDown Functions ---

	def time_countdown(self):
		global down_sec, down_min, down_hour

		if self.countdown_run[0] == True :

			if down_sec == 0:

				if down_min == 0:

					if down_hour == 0:
						self.countdown_run[0] = False
						alarm.Alarm()
						return False

					elif down_hour > 0 :
						down_hour -= 1
						down_min = 59
						down_sec = 59
		
				elif down_min > 0:
					down_min -= 1
					down_sec = 59
		
			elif down_sec > 0 :
				down_sec -= 1

			self.CountDown.set_text(" %02d : %02d : %02d " %(down_hour, down_min, down_sec) )
			return True

		elif self.countdown_run[0] == False :
			return False

			
	def start_countdown(self, widget):
		if self.countdown_run[0] == False :
			if down_hour != 0 or down_min != 0 or down_sec != 0 :
				self.countdown_run[0] = True
				gobject.timeout_add(1000, self.time_countdown)

	def pause_countdown(self, widget):
		self.countdown_run[0] = False
		self.update_CountDown()

	def reset_countdown(self, widget):
		global down_sec, down_min, down_hour
		self.countdown_run[0] = False
		down_sec, down_min, down_hour = 0, 0, 0
		self.update_CountDown()


	def inc_hour(self, widget):
		global down_sec, down_min, down_hour
		if ( down_hour + 1 ) == 24 :
			self.update_CountDown()
		else :
			down_hour += 1
			self.update_CountDown()

	def inc_min(self, widget):
		global down_sec, down_min, down_hour
		if (down_min + 1) == 60 :
			self.update_CountDown()
		else :
			down_min += 1
			self.update_CountDown()

	def inc_sec(self, widget):
		global down_sec, down_min, down_hour
		if (down_sec + 1) == 60 :
			self.update_CountDown()
		else :
			down_sec += 1
			self.update_CountDown()


	def dec_hour(self, widget):
		global down_sec, down_min, down_hour
		if (down_hour - 1) < 0 :
			self.update_CountDown()
		else :
			down_hour -= 1
			self.update_CountDown()

	def dec_min(self, widget):
		global down_sec, down_min, down_hour
		if (down_min - 1) < 0 :
			self.update_CountDown()
		else :
			down_min -= 1
			self.update_CountDown()

	def dec_sec(self, widget):
		global down_sec, down_min, down_hour
		if (down_sec - 1) < 0 :
			self.update_CountDown()
		else :
			down_sec -= 1

			self.update_CountDown()

	def update_CountDown(self):

		self.CountDown.set_text(" %02d : %02d : %02d " %(down_hour, down_min, down_sec) )


	def on_changed(self, widget):
		global down_sec, down_min, down_hour
		distros = ['10 minutes','15 minutes','30 minutes','1 hour']

		i =str( widget.get_active_text() )

		if distros.index(i) == 0 :
			down_sec, down_min, down_hour = 0, 10, 0

		elif distros.index(i) == 1 :
			down_sec, down_min, down_hour = 0, 15, 0

		elif distros.index(i) == 2 :
			down_sec, down_min, down_hour = 0, 30, 0

		elif distros.index(i) == 3 :
			down_sec, down_min, down_hour = 0, 0, 1

		self.CountDown.set_text(" %02d : %02d : %02d " %(down_hour, down_min, down_sec) )


# --- About function ---

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


#-----------------------

#PyApp()
#gtk.main()
