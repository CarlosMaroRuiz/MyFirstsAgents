from provider_model.deepseek_provide import model
from outputs.math_output import ResultMath
from pydantic_ai import Agent
from system_promp.math_prompt import MATH_SYSTEM_PROMPT

# Crear el agente con el modelo y el tipo de salida
agent = Agent(model=model, output_type=ResultMath,system_prompt=MATH_SYSTEM_PROMPT)#usa una prompt base


result = agent.run_sync('2x + x + 1 = 10')

# Imprimir los pasos
print("----- Pasos que siguieron -----")
for step in result.output.step_operation:
    print(step)

# Imprimir el resultado final
print(f"\nResultado final: {result.output.result_final}")