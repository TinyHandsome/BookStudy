import gradio as gr

with gr.Blocks() as demo:
    with gr.Tab("图像分类"):
        gr.Markdown("# 图像分类演示")
        with gr.Row():
            input_img = gr.Image(sources=["upload"], label="上传图片", type="pil")
            output_label = gr.Label(num_top_classes=10)

        gr.Examples(["./datas/dog.jpg", "./datas/cat.jpeg"], inputs=[input_img])
        button = gr.Button(value="分类", variant="primary")
        button.click(None, inputs=input_img, outputs=output_label)

demo.launch(server_name="0.0.0.0")
