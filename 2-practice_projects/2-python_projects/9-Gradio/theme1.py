import gradio as gr


def greet_themed(name):
    return f"Hello, {name}!"


"""
# 示例 1: 使用内置主题
with gr.Blocks(theme=gr.themes.Monochrome()) as demo:
    gr.Markdown("# 单色主题应用")
    name_input = gr.Textbox("World", label="输入你的名字")
    output_text = gr.Textbox(label="问候语")
    name_input.change(greet_themed, inputs=name_input, outputs=output_text)
"""

"""
# 示例 2: 使用另一个内置主题，并通过 set_theme() 全局设置（如果多个 Blocks 则会冲突）
# 通常推荐在 Blocks 构造函数中设置 theme
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 柔和主题应用")
    name_input_soft = gr.Textbox("Gradio", label="输入名字")
    output_text_soft = gr.Textbox(label="问候语")
    name_input_soft.change(
        greet_themed, inputs=name_input_soft, outputs=output_text_soft
    )
"""


# 示例 3: 自定义 CSS
custom_css = """
/* 自定义输入框背景和边框 */
.gradio-container .gr-form {
    background-color: #f0f8ff; /* AliceBlue */
    border: 2px dashed #4682b4; /* SteelBlue */
    padding: 20px;
    border-radius: 10px;
}
/* 自定义按钮颜色 */
.gradio-container button.gr-button {
    background-color: #2e8b57; /* SeaGreen */
    color: white;
    border-radius: 5px;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Default()) as demo:
    gr.Markdown("# 自定义 CSS 样式")
    name_input_css = gr.Textbox("CSS World", label="输入名字")
    output_text_css = gr.Textbox(label="问候语")
    process_btn = gr.Button("点击问候")
    process_btn.click(greet_themed, inputs=name_input_css, outputs=output_text_css)


demo.launch()
