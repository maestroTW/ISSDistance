import tkinter
import tkintermapview

import ISS, User, Distance

# create tkinter window
root_tk = tkinter.Tk()
root_tk.geometry(f"{1920}x{1080}")
root_tk.title("ISSDistance")

# create map widget
map_widget = tkintermapview.TkinterMapView(root_tk, width=1920, height=1080, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# set markers
User_marker = map_widget.set_marker(float(User.Cord[0]), float(User.Cord[1]), text="You")
ISS_marker = map_widget.set_marker(float(ISS.Cord[0]), float(ISS.Cord[1]), text='ISS')
path = map_widget.set_path([User_marker.position, ISS_marker.position])
distance = map_widget.set_marker(Distance.MidDistance[0], Distance.MidDistance[1], text=Distance.Distance)

# start
map_widget.set_zoom(15)
root_tk.mainloop()
