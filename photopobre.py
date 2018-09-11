import window

class PhotoPobre():
    def run(self):
        windows = list()
        images = list()

        im = window.Image.open("Space_187k.jpg")#.save("filhocopy.jpg")
        images.append(im)
        
        im = window.Image.open("Space_187k.jpg")#.save("filhocopy.jpg")
        images.append(im)

        win = window.OriginalWindow()
        win.connect("destroy", window.Gtk.main_quit)
        win.add(window.Gtk.Image.new_from_pixbuf(window.image2pixbuf(im)))
        win.show_all()
        windows.append(win)

        win = window.CopyWindow()
        win.connect("destroy", window.Gtk.main_quit)
        win.show_all()
        windows.append(win)

        win = window.ButtonWindow(windows,images)
        win.connect("destroy", window.Gtk.main_quit)
        win.show_all()

        window.Gtk.main()
