from fastapi import FastAPI
import gradio as gr

from AirPlane_ChatBot_LLM.model import airplane_chat
from Medical_Chatbot_LLM.model import medical_chat

app = FastAPI()

# @app.get("/")
# async def root():
#     return 'Gradio app is running at /gradio', 200


app = gr.mount_gradio_app(app, medical_chat, path='/medical')
app = gr.mount_gradio_app(app, airplane_chat, path='/airplane')
