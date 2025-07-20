"""
Este es un script que su principal funcionamiento es realizar un wrapper
para poder usar deepseek ya que en existe compatibilidad entre la libreria de 
openAi y deepseek
"""
#OpenAiModel no servira para poder encapsular a nuestro provedor de deepseek
from pydantic_ai.models.openai import OpenAIModel
#deepseek provider nos permitira realizar la configuraciones necesarias para poder usarse
from pydantic_ai.providers.deepseek import DeepSeekProvider
from config.config import config_context

"""
Podemos usar los diversos modelos que este disponga los mas conocidos serian:
deepseek-chat
deepseek-reseaoner 
"""
model = OpenAIModel(
    "deepseek-chat",
    provider=DeepSeekProvider(api_key=config_context.deepseek_api_key,),
    
)