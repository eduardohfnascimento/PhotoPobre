import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GdkPixbuf
from PIL import Image
import numpy as np


out = Image.open("Space_187k.jpg")

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PhotoPobre")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Copiar Imagem")
        button.connect("clicked", self.on_copy_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Tons de Cinza")
        button.connect("clicked", self.on_tons_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Espelhamento Horizontal")
        button.connect("clicked", self.on_horizontal_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Espelhamento Vertical")
        button.connect("clicked", self.on_vertical_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Fechar")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_copy_me_clicked(self, button):
        print("\"Copy me\" button was clicked")
        for row in windows[2].get_children():
            windows[2].remove(row);
        outima = Gtk.Image.new_from_pixbuf(image2pixbuf(out))
        print (outima)
        windows[2].add(outima)
        windows[2].show_all()

    def on_tons_clicked(self, button):
        print("\"Tons\" button was clicked")
        if (len(windows[2].get_children())):
            images[0] = images[0].convert("L")
            images[0]=np.array(images[0])
            imRGB = np.repeat(images[0][:, :, np.newaxis], 3, axis=2)
            images[0] = Image.fromarray(imRGB)
            outima = Gtk.Image.new_from_pixbuf(image2pixbuf(images[0]))
            for row in windows[2].get_children():
                windows[2].remove(row);
            windows[2].add(outima)
            windows[2].show_all()

    def on_horizontal_clicked(self, button):
        print("\"Horizontal\" button was clicked")
        if (len(windows[2].get_children())):
            #im = Image.open("Space_187k.jpg")
            images[0] = images[0].transpose(Image.FLIP_LEFT_RIGHT)
            outima = Gtk.Image.new_from_pixbuf(image2pixbuf(images[0]))
            for row in windows[2].get_children():
                windows[2].remove(row);
            windows[2].add(outima)
            windows[2].show_all()

    def on_vertical_clicked(self, button):
        print("\"Vertical\" button was clicked")
        if (len(windows[2].get_children())):
            #im = Image.open("Space_187k.jpg")
            images[0] = images[0].transpose(Image.FLIP_TOP_BOTTOM)
            outima = Gtk.Image.new_from_pixbuf(image2pixbuf(images[0]))
            for row in windows[2].get_children():
                windows[2].remove(row);
            windows[2].add(outima)
            windows[2].show_all()

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PhotoPobre")

class MyWindowCopy(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PhotoPobre")

        
def image2pixbuf(im):
    """Convert Pillow image to GdkPixbuf"""
    data = im.tobytes()
    w, h = im.size
    data = GLib.Bytes.new(data)
    pix = GdkPixbuf.Pixbuf.new_from_bytes(data, GdkPixbuf.Colorspace.RGB,
            False, 8, w, h, w * 3)
    return pix

im = Image.open("Space_187k.jpg")#.save("filhocopy.jpg")

ima = Gtk.Image.new_from_pixbuf(image2pixbuf(im))
win = MyWindow()
windows = list()
images = list()
images.append(im)
windows.append(win)
win.connect("destroy", Gtk.main_quit)
win.add(ima)
win.show_all()

win = ButtonWindow()
windows.append(win)
win.connect("destroy", Gtk.main_quit)
#win.add(ima)
win.show_all()

win = MyWindowCopy()
windows.append(win)
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()