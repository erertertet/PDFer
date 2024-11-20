from nerif.agent import VisionAgent, MessageType

from PIL import Image
import base64
import io

import webbrowser

def png_to_base64(filename):
    with Image.open(filename) as img:
        img = img.convert('RGB')
        with io.BytesIO() as output_bytes:
            img.save(output_bytes, format='JPEG')
            bytes_data = output_bytes.getvalue()
            base64_str = base64.b64encode(bytes_data).decode('utf-8')

            return base64_str

image = 'test.png'

agent = VisionAgent()
agent.append_message(MessageType.IMAGE_BASE64, png_to_base64(image))
agent.append_message(MessageType.TEXT, 'recognize the text and response in formatted html')

res = agent.chat()

with open('out.html', 'w', encoding='utf-8') as file:
    with open('html/template.html') as temp:
        s = temp.read() % (image, res, res)
        file.write(s)

webbrowser.open('out.html')