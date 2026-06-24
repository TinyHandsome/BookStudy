import gradio as gr
from PIL import Image


def convert_to_grayscale(image: Image.Image) -> Image.Image:
    if image is None:
        return None
    return image.convert("L")


def rotate_image(image: Image.Image, angle: int) -> Image.Image:
    if image is None:
        return None
    return image.rotate(angle, expand=True)


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Image Processing Tool")
    gr.Markdown(
        "Upload an image and apply transformations like grayscale conversion and rotation."
    )

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(label="Upload Image", type="pil")
            operation_radio = gr.Radio(
                choices=["Grayscale", "Rotate"],
                label="Select Operation",
                value="Grayscale",
            )
            angle_slider = gr.Slider(0, 360, step=1, label="Rotation Angle", value=0)
            process_button = gr.Button("Operation")

        with gr.Column():
            output_image = gr.Image(label="Output Image", type="pil")
            status_text = gr.Textbox(label="Status", interactive=False)

    def process_image(image, operation, angle):
        if image is None:
            return None, "Please upload an image."
        if operation == "Grayscale":
            processed_image = convert_to_grayscale(image)
            return processed_image, "Converted to Grayscale."
        elif operation == "Rotate":
            processed_image = rotate_image(image, angle)
            return processed_image, f"Rotated by {angle} degrees."
        return None, "Invalid operation."

    operation_radio.change(
        fn=lambda op: gr.update(visible=(op == "Rotate")),
        inputs=operation_radio,
        outputs=angle_slider,
    )
    
    process_button.click(
        fn=process_image,
        inputs=[input_image, operation_radio, angle_slider],
        outputs=[output_image, status_text],
    )


demo.launch()
