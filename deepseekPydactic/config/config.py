"""
Clase que nos permite englobar las configuraciones de nuestro 
sistema
"""
from dotenv import load_dotenv
import os
load_dotenv()
class Config:
    def __init__(self):
        self.deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

#config inicializado para poder compartirse
config_context = Config()