import gradio as gr
from PIL import Image, ImageFilter


def blur_image(image: Image.Image, radius: int) -> Image.Image:
    if image is None:
        return None
    return image.filter(ImageFilter.GaussianBlur(radius))


demo = gr.Interface(
    fn=blur_image,
    inputs=[
        gr.Image(label="Upload Image", type="pil"),
        gr.Slider(0, 10, step=1, label="Blur Radius", value=2),
    ],
    outputs=gr.Image(label="Blurred Image", type="pil"),
    title="Image Blurring Tool",
    description="Upload an image and apply a Gaussian blur effect.",
    theme=gr.themes.Soft(),
    examples=[["datas/cat.jpeg", 5], ["datas/dog.jpg", 8]],
)

demo.launch()
