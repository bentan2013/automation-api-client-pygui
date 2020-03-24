from tkinter import *

root = Tk()
root.wm_title("Automation API")

#region FUNC
def get_camera():
    input = input_text.get()
    output_text.insert("start")
    pass

def set_camera():
    pass

def fly_to():
    pass

def add_layer():
    pass

def get_layer_load_status():
    pass

def remove_layer():
    pass

def clear_layer():
    pass

def import_workspace():
    pass

def clear_workspace():
    pass

def clear_input_box():
    pass

def clear_output_box():
    pass

def get_snapshot():
    pass
#endregion


#region GUI
root.minsize(200, 200)

input_text = Text(root)
input_text.pack()

get_camera_btn = Button(root, text="Get Camera", command=get_camera)
get_camera_btn.pack()
set_camera_btn = Button(root, text="Set Camera", command=set_camera)
set_camera_btn.pack()
fly_to_btn = Button(root, text="Fly To", command=fly_to)
fly_to_btn.pack()

add_layer_btn = Button(root, text="Add Layer", command=add_layer)
add_layer_btn.pack()
get_layer_load_status_btn = Button(root, text="Get Layer Load Status", command=get_layer_load_status)
get_layer_load_status_btn.pack()
remove_layer_btn = Button(root, text="Remove Layer", command=remove_layer)
remove_layer_btn.pack()
clear_layer_btn = Button(root, text="Clear Layer", command=clear_layer)
clear_layer_btn.pack()

import_workspace_btn = Button(root, text="Import Workspace", command=import_workspace)
import_workspace_btn.pack()
clear_workspace_btn = Button(root, text="Clear Workspace", command=clear_workspace)
clear_workspace_btn.pack()

clear_input_box_btn = Button(root, text="Clear Input Box", command=clear_input_box)
clear_input_box_btn.pack()
clear_output_box_btn = Button(root, text="Clear Output Box", command=clear_output_box)
clear_output_box_btn.pack()
get_snapshot_btn = Button(root, text="Get Snapshot", command=get_snapshot)
get_snapshot_btn.pack()

help_btn = Button(root, text="Help", command=help)
help_btn.pack()

output_text = Text(root)
output_text.pack()
#endregion

 
root.mainloop()