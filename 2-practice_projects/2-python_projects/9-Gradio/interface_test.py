import gradio as gr
import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


""" test1
def greet(name):
    return f"Hello {name}!"

 iface = gr.Interface(fn=greet, inputs=gr.Textbox(lines=5, placeholder="name here", label="name:"), outputs="text")
"""

"""test2
def turn_gray(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_image
iface = gr.Interface(fn=turn_gray, inputs=gr.Image(), outputs="image")
"""

"""test3
def file_path(input):
    return input

iface = gr.Interface(fn=file_path, inputs=gr.Audio(sources=["microphone"], type="filepath"), outputs="text")
"""


"""test4
def audio_fn(audio):
    hz = audio[0]
    data = audio[1]
    return hz, data

def audio_fn2(audio):
    return audio

iface = gr.Interface(fn=audio_fn, inputs=gr.Audio(type="numpy"), outputs="audio")
iface2 = gr.Interface(fn=audio_fn2, inputs=gr.Audio(type="filepath"), outputs="audio")
"""

"""test5
simple_data = pd.DataFrame({
    "a": [1, 2, 3],
    "b": [4, 5, 6]
})
iface = gr.Interface(fn=None, inputs=None, outputs=gr.BarPlot(simple_data, x='a', y='b'))
"""


"""test6
def process():
    cheetabs = [
        "https://upload.wikimedia.org/wikipedia/commons/0/09/TheCheethcat.jpg",
        "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-003.jpg",
        "https://img.etimg.com/thumb/msid-50159822,width-650,imgsize-129520,,resizemode-4,quality-100/.jpg",
        "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-002.jpg",
        "https://images.theconversation.com/files/375893/original/file-20201218-13-a8h8uq.jpg?ixlib=rb-1.1.0&rect=16%2C407%2C5515%2C2924&q=45&auto=format&w=496&fit=clip",
    ]
    cheetabs = [(c, f"Cheetah {i+1}") for i, c in enumerate(cheetabs)]
    
    return cheetabs

iface = gr.Interface(fn=process, inputs=None, outputs=gr.Gallery(columns=4))
"""


"""test7
def fig_output():
    fs = 8000
    f = 5
    sample = 10
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / fs)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16,9))
    ax1.plot(x, y)
    ax2.bar(x, y)
    
    return plt
iface = gr.Interface(fn=fig_output, inputs=None, outputs=gr.Plot())
"""

"""test8
def fig_output():
    return "hello world"
iface = gr.Interface(fn=fig_output, inputs=None, outputs=gr.Textbox())
"""

"""test9
json_sample = {'name': 'John', 'age': 12, 'city': 'HeBei'}
iface = gr.Interface(fn=None, inputs=None, outputs=gr.Json(json_sample))
"""

iface = gr.Interface(fn=None, inputs=None, outputs=gr.HTML(value="<h1>hello</h1>"))

iface.launch()
