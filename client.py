from tkinter import *
import requests
import json
import time
import os

root = Tk()
root.wm_title("Automation API")

#region config
base_address = "http://localhost:80/Temporary_Listen_Addresses/arcgisearth/api/v1"
camera_info = "{ \"mapPoint\": { \"x\": 113.59647525051167, \"y\": 32.464715999412107, \"z\": 2213290.0751730204, \"spatialReference\": { \"wkid\": 4326 } }, \"heading\": 354.04823651174161, \"pitch\": 19.96239543740441}"
fly_to_info = "{\"camera\":{\"mapPoint\":{\"x\":-92,\"y\":41,\"z\":11000000,\"spatialReference\":{\"wkid\":4326}},\"heading\":0.0,\"pitch\":0.099999999996554886},\"duration\":2}"
add_layer_info = "{\"type\":\"MapService\",\"URI\":\"https://services.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer\",\"target\":\"OperationalLayers\"}"
OUTPUT_SUCESS_MESSAGE = "SUCESS"
OUTPUT_FAILED_MESSAGE = "FAILED"
#endregion

#region FUNC
def get_input_text():
    global input_text
    input_str = input_text.get(1.0, "end")
    return input_str


def set_output_text(output_str):
    global output_text
    output_text.delete(1.0, "end")
    output_text.insert("end", output_str)


def clear_input_box():
    global input_text
    input_text.delete(1.0, "end")


def clear_output_box():
    global output_text
    output_text.delete(1.0, "end")

def help():
    global output_text
    output_text.insert("end", "test")
    global input_text
    input_text.insert("end", "test")

def get_json_result(r):
    if r.status_code == 200:
        content = r.content
        decode_content = content.decode('utf-8')
        json_content = json.loads(decode_content)
        return json_content 
    return OUTPUT_FAILED_MESSAGE


def get_json_field_result(r, field_name):
    json_content = get_json_result()
    if field_name in json_content:
        result = json_content[field_name]
        return result
    return OUTPUT_FAILED_MESSAGE


def get_camera():
    url = base_address + "/camera"
    r = requests.get(url)
    result = get_json_field_result(r, "GetCameraResult")
    set_output_text(result)


def set_camera():
    input_text = get_input_text()
    url = base_address + "/camera/" + input_text
    r = requests.put(url)
    result = get_json_field_result(r, "SetCameraResult")
    set_output_text(result)


def fly_to():
    input_text = get_input_text()
    url = base_address + "/flyto" + input_text
    r = requests.put(url)
    result = get_json_field_result(r, "FlyToResult")
    set_output_text(result)


def add_layer():
    url = base_address + '/layer'
    data = get_input_text()
    headers = {"content-Type": "application/json"}
    r = requests.post(url, data=data, headers=headers)
    layer_id = get_json_field_result(r, "id")
    set_output_text(layer_id)


def get_layer_load_status():
    layer_id = get_input_text()
    result = OUTPUT_FAILED_MESSAGE
    if layer_id is not None:
        url = base_address + "/layer/" + layer_id + "/load_status"
        r = requests.get(url)
        json_result = get_json_result(r)
        result = json_result
    set_output_text(result)


def remove_layer():
    result = OUTPUT_FAILED_MESSAGE
    layer_id = get_input_text()
    if layer_id is not None:
        url = base_address + "/layer/" + layer_id
        r = requests.delete(url)
        result = get_json_result(r)
        
    set_output_text(result)


def clear_layer():
    result = OUTPUT_FAILED_MESSAGE
    layer_info = get_input_text()
    url = base_address + "/layers" + layer_info
    r = requests.delete(url)
    result = get_json_result()
    set_output_text(result)


def get_layers():
    result = OUTPUT_FAILED_MESSAGE
    layer_info = get_input_text()
    # get layers
    url = base_address + "/" + layer_info
    r = requests.get(url)
    result = get_json_result(r)
    set_output_text(result)
    

def import_workspace():
    result = OUTPUT_FAILED_MESSAGE
    url = base_address + "/workspace"
    layers_json = get_input_text()
    data = json.dumps(layers_json)
    r = requests.put(url, data=data, stream=True)
    set_output_text(result)


def clear_workspace():
    result = OUTPUT_FAILED_MESSAGE
    set_output_text(result)
    pass


def get_snapshot():
    url = base_address + "/snapshot"
    r = requests.get(url, stream=True)
    result = get_json_result(r)
    path = "./snaps.jpg"
    if os.path.exists(path):
        os.remove(path)
    with open(path, 'wb') as f:
        for chunk in r:
            f.write(chunk)
#endregion


#region GUI
root.minsize(200, 200)

input_frame = LabelFrame(root, text="Input")
input_frame.pack(side=TOP, fill=X, expand=0)

input_text = Text(master=input_frame)
input_text.pack()


camera_frame = LabelFrame(root, text="Camera")
camera_frame.pack(side=TOP, fill=X, expand=0)
get_camera_btn = Button(camera_frame, text="Get Camera", command=get_camera)
get_camera_btn.pack(side=LEFT)
set_camera_btn = Button(camera_frame, text="Set Camera", command=set_camera)
set_camera_btn.pack(side=LEFT)
fly_to_btn = Button(camera_frame, text="Fly To", command=fly_to)
fly_to_btn.pack(side=LEFT)


layer_frame = LabelFrame(root, text="Layer Operation")
layer_frame.pack(side=TOP, fill=X, expand=0)
add_layer_btn = Button(layer_frame, text="Add Layer", command=add_layer)
add_layer_btn.pack(side=LEFT)
get_layer_load_status_btn = Button(layer_frame, text="Get Layer Load Status", command=get_layer_load_status)
get_layer_load_status_btn.pack(side=LEFT)
remove_layer_btn = Button(layer_frame, text="Remove Layer", command=remove_layer)
remove_layer_btn.pack(side=LEFT)
clear_layer_btn = Button(layer_frame, text="Clear Layer", command=clear_layer)
clear_layer_btn.pack(side=LEFT)

layers_frame = LabelFrame(root, text="Layers Operation")
layers_frame.pack(side=TOP, fill=X, expand=0)
get_layers_btn = Button(layers_frame, text="Get Layers", command=get_layers)
get_layers_btn.pack(side=LEFT)
import_workspace_btn = Button(layers_frame, text="Import Workspace", command=import_workspace)
import_workspace_btn.pack(side=LEFT)
clear_workspace_btn = Button(layers_frame, text="Clear Workspace", command=clear_workspace)
clear_workspace_btn.pack(side=LEFT)


other_frame = LabelFrame(root, text="Other Operation")
other_frame.pack(side=TOP, fill=X, expand=0)
clear_input_box_btn = Button(other_frame, text="Clear Input Box", command=clear_input_box)
clear_input_box_btn.pack(side=LEFT)
clear_output_box_btn = Button(other_frame, text="Clear Output Box", command=clear_output_box)
clear_output_box_btn.pack(side=LEFT)
get_snapshot_btn = Button(other_frame, text="Get Snapshot", command=get_snapshot)
get_snapshot_btn.pack(side=LEFT)

help_btn = Button(other_frame, text="Help", command=help)
help_btn.pack(side=LEFT)

output_frame = LabelFrame(root, text="Output")
output_frame.pack(side=TOP, fill=X, expand=0)
output_text = Text(output_frame)
output_text.pack(side=LEFT)
#endregion

 
root.mainloop()
