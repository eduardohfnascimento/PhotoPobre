import window

class PhotoPobre():
    def run(self):
        


        im = window.Image.open("Space_187k.jpg")#.save("filhocopy.jpg")

        ima = window.Gtk.Image.new_from_pixbuf(window.image2pixbuf(im))
        win = window.OriginalWindow()
        windows = list()
        images = list()
        images.append(im)
        windows.append(win)
        win.connect("destroy", window.Gtk.main_quit)
        win.add(ima)
        win.show_all()

        win = window.ButtonWindow()
        windows.append(win)
        win.connect("destroy", window.Gtk.main_quit)
        #win.add(ima)
        win.show_all()

        win = window.CopyWindow()
        windows.append(win)
        win.connect("destroy", window.Gtk.main_quit)
        win.show_all()

        window.Gtk.main()
