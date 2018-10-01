import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib, GdkPixbuf
from PIL import Image
import numpy as np
import math
import matplotlib.pyplot as plt
import numpy as np

class ButtonWindow(Gtk.Window):

    def __init__(self, windows, images):
        self.windows = windows
        self.images = images
        
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

        button = Gtk.Button.new_with_mnemonic("Quantizacao")
        button.connect("clicked", self.on_quantization_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Salvar")
        button.connect("clicked", self.on_save_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_mnemonic("Fechar")
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_copy_me_clicked(self, button):
        print("\"Copy me\" button was clicked")
        for row in self.windows[1].get_children():
            self.windows[1].remove(row);

        self.images[0] = self.images[1]
        outima = Gtk.Image.new_from_pixbuf(image2pixbuf(self.images[0]))
        self.windows[1].add(outima)
        self.windows[1].show_all()

    def on_tons_clicked(self, button):
        # print("\"Tons\" button was clicked")
        # if (len(self.windows[1].get_children())):
        #     self.images[0] = imageL2imageRGB(self.images[0])
        #     outima = Gtk.Image.new_from_pixbuf(image2pixbuf(self.images[0]))
        #     for row in self.windows[1].get_children():
        #         self.windows[1].remove(row)

        #     self.windows[1].add(outima)
        #     self.windows[1].show_all()
        x = np.random.normal(size = 1000)
        plt.hist(x, normed=True, bins=30)
        plt.ylabel('Probability');
        plt.show()

    def on_horizontal_clicked(self, button):
        print("\"Horizontal\" button was clicked")
        if (len(self.windows[1].get_children())):
            self.images[0] = self.images[0].transpose(Image.FLIP_LEFT_RIGHT)
            outima = Gtk.Image.new_from_pixbuf(image2pixbuf(self.images[0]))
            for row in self.windows[1].get_children():
                self.windows[1].remove(row)

            self.windows[1].add(outima)
            self.windows[1].show_all()

    def on_vertical_clicked(self, button):
        print("\"Vertical\" button was clicked")
        if (len(self.windows[1].get_children())):
            self.images[0] = self.images[0].transpose(Image.FLIP_TOP_BOTTOM)
            outima = Gtk.Image.new_from_pixbuf(image2pixbuf(self.images[0]))
            for row in self.windows[1].get_children():
                self.windows[1].remove(row)

            self.windows[1].add(outima)
            self.windows[1].show_all()

    def on_quantization_clicked(self, button):
        print("\"Tons\" button was clicked")
        if (len(self.windows[1].get_children())):
            self.images[0] = imageL2imageRGBQ(self.images[0])
            outima = Gtk.Image.new_from_pixbuf(image2pixbuf(self.images[0]))
            for row in self.windows[1].get_children():
                self.windows[1].remove(row)

            self.windows[1].add(outima)
            self.windows[1].show_all()

    def on_save_clicked(self, button):
        print("\"Salvar\" button was clicked")
        self.images[0].save("filhocopy.jpg")

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

class OriginalWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PhotoPobre")

class CopyWindow(Gtk.Window):

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

def imageL2imageRGB(im):
    im = im.convert("L")
    im=np.array(im)
    imRGB = np.repeat(im[:, :, np.newaxis], 3, axis=2)
    return Image.fromarray(imRGB)

def imageL2imageRGBQ(im):
    im = im.convert("L")
    im=np.array(im)
    for x in xrange(im.shape[0]):
        for y in xrange(im.shape[1]):
            im[x][y] = (im[x][y]/12) * 12
    imRGB = np.repeat(im[:, :, np.newaxis], 3, axis=2)
    return Image.fromarray(imRGB)
