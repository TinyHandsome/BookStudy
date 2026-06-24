import json
import gradio as gr
import aiohttp


async def do_chat(message, history):
    all_content = ""
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://10.5.33.10:32801/v1/chat/completions",
            json={
                "model": "qwen3",
                "messages": [{"role": "user", "content": message}],
                "stream": True,
            },
        ) as response:
            async for i in response.content:
                content = json.loads(i.decode("utf-8").replace("data: ", ""))["choices"][0]["delta"]["content"]
                if content:
                    all_content += content
                    yield content



gr.ChatInterface(
    fn=do_chat,
    chatbot=gr.Chatbot(height=500, value=[["你好", "您好，我是蛇皮助手~"]]),
    textbox=gr.Textbox(placeholder="请输入你的问题", container=False, scale=7),
    type="messages",
    title="AI蛇皮助手",
    theme="soft",
    examples=["什么是蛇皮？", "你是什么蛇皮？", "如何蛇皮？"],
    submit_btn="发送",
).queue().launch(server_name="0.0.0.0")
