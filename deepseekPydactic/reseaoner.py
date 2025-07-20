from pydantic_ai import Agent
import json
from dotenv import load_dotenv

load_dotenv()

# Prompt mejorado que evita markdown
stats_agent = Agent(
    "deepseek:deepseek-reasoner",
    system_prompt=(
        "Eres un generador de datos JSON. "
        "IMPORTANTE: Responde ÚNICAMENTE con JSON válido, sin markdown, sin explicaciones, sin ```json. "
        "Tu respuesta debe comenzar directamente con { y terminar con }. "
        "NO uses formato markdown. Solo JSON puro."
    )
)

problem = """
Genera una salida en formato JSON con los siguientes campos:
- id (número aleatorio)
- nombre (nombre ficticio)
- edad (entre 18 y 30)
- cursos (una lista de 3 cursos ficticios)
- activo (true o false)
"""

# Ejecutar el agente
result = stats_agent.run_sync(problem)


print("📦 Respuesta cruda:")
print(result.output)

# Parsear directamente
try:
    parsed = json.loads(result.output)
    print("\n✅ JSON parseado:")
    print(json.dumps(parsed, indent=4, ensure_ascii=False))
except json.JSONDecodeError as e:
    print("\n❌ No se pudo parsear la salida como JSON:", e)