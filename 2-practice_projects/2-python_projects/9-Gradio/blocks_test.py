import gradio as gr


with gr.Blocks(css_paths=["style.css"]) as demo:
    with gr.Tab(label="txt2img"):
        with gr.Row(equal_height=False):
            with gr.Column(scale=15):
                txt1 = gr.Textbox(lines=2, label="")
                txt2 = gr.Textbox(lines=2, label="")

            with gr.Column(scale=1, min_width=1):
                button1 = gr.Button(value="1", elem_classes="btn")
                button2 = gr.Button(value="2", elem_classes="btn")
                button3 = gr.Button(value="3", elem_classes="btn")
                button4 = gr.Button(value="4", elem_classes="btn")

            with gr.Column(scale=6):
                generate_button = gr.Button(
                    value="Generate", variant="primary", scale=1
                )
                with gr.Row(equal_height=False):
                    dropdown1 = gr.Dropdown(
                        ["1", "2", "3", "4"], label="Style1", interactive=True
                    )
                    dropdown2 = gr.Dropdown(
                        ["1", "2", "3", "4"], label="Style2", interactive=True
                    )
        with gr.Row():
            with gr.Column():
                with gr.Row():
                    dropdown3 = gr.Dropdown(
                        ["1", "2", "3", "4"], label="Sampling method", interactive=True
                    )
                    slider1 = gr.Slider(minimum=0, maximum=100, label="Sampling steps")
                checkboxgroup = gr.CheckboxGroup(
                    ["Restore faces", "Tiling", "Hires.fix"], label=""
                )
                with gr.Row():
                    slider2 = gr.Slider(minimum=0, maximum=100, label="Width")
                    slider3 = gr.Slider(minimum=0, maximum=100, label="Batch count")
                with gr.Row():
                    slider4 = gr.Slider(minimum=0, maximum=100, label="Height")
                    slider5 = gr.Slider(minimum=0, maximum=100, label="Batch size")
                slider6 = gr.Slider(minimum=0, maximum=100, label="CFG scale")
                with gr.Row(equal_height=True):
                    number1 = gr.Number(label="Seed", scale=5)
                    button5 = gr.Button(value="Randomize", min_width=1)
                    button6 = gr.Button(value="Reset", min_width=1)
                    checkbox1 = gr.Checkbox(label="Extra", min_width=10)
                dropdown4 = gr.Dropdown(
                    ["1", "2", "3", "4"], label="Script", interactive=True
                )
            with gr.Column():
                with gr.Accordion("Gallery"):
                    gallery = gr.Gallery(
                        [
                            "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-003.jpg",
                            "https://img.etimg.com/thumb/msid-50159822,width-650,imgsize-129520,,resizemode-4,quality-100/.jpg",
                            "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-002.jpg",
                            "https://img.etimg.com/thumb/msid-50159822,width-650,imgsize-129520,,resizemode-4,quality-100/.jpg",
                            "https://nationalzoo.si.edu/sites/default/files/animals/cheetah-002.jpg",
                        ],
                        columns=3,
                        label="",
                    )
                with gr.Row(equal_height=True):
                    with gr.Group():
                        button7 = gr.Button(value="Save", min_width=1)
                        button8 = gr.Button(value="Zip", min_width=1)
                    button6 = gr.Button(value="Save", min_width=1)
                    button7 = gr.Button(value="Save", min_width=1)
                    button8 = gr.Button(value="Zip", min_width=1)
                    button9 = gr.Button(value="Send to img2img", min_width=1)
                    button10 = gr.Button(value="Send to inpaint", min_width=1)
                    button11 = gr.Button(value="Send to extras", min_width=1)
                text3 = gr.Textbox(lines=4, label="")
    with gr.Tab(label="img2img"):
        ...

demo.launch(server_name="0.0.0.0")
