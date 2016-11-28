import gi 
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):
	"""docstring for MyWindow"""
	def __init__(self):
		Gtk.Window.__init__(self, title="WTF")

		self.button = Gtk.Button(label="Click Here")
		self.button.connect("clicked", self.on_button_clicked)
		self.add(self.button)

	def on_button_clicked(self, widget):
		print("Hello World")

win = MyWindow()
win.connect("delete_event", Gtk.main_quit)
win.show_all
Gtk.main()		
