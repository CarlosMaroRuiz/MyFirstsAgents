from provider_model.deepseek_provide import model#ya no es obligatorio jsjsjs
from pydantic_ai import Agent
from system_promp.math_prompt import STATISTICS_SYSTEM_PROMPT  
from tools.latex_tools import latex_generator_tool
from outputs.math_output import StatisticsResult

#usando provider apenas descubri que se puede usar sin provider jsjsj
stats_agent = Agent(
    "deepseek:deepseek-chat",
    output_type=StatisticsResult,
    system_prompt=STATISTICS_SYSTEM_PROMPT,
    tools=[latex_generator_tool]
)

problem = """
Se realizó un estudio comparando los puntajes de satisfacción (escala 1-10) entre dos grupos:
- Grupo A (n=30): Media=7.2, DE=1.5
- Grupo B (n=28): Media=5.8, DE=1.8

Realiza:
1. Prueba de hipótesis adecuada
2. Análisis descriptivo
3. Genera documento LaTeX con los resultados
"""


result = stats_agent.run_sync(problem)

#Imprimir resultados
print("----- Análisis Estadístico -----")
for step in result.output.analysis_steps:
    print(f"- {step}")

print(f"\nConclusión Final: {result.output.final_conclusion}")
print("\n----- Código LaTeX Generado -----")
print(result.output.latex_code[:500] + "...")  

print("\nDetalles de Ejecución:")
print(result.output.details_execution)

#Guardar el código LaTeX a un archivo
latex_path = "output_latex.tex"
with open(latex_path, "w", encoding="utf-8") as f:
    f.write(result.output.latex_code)
print(f"\nCódigo LaTeX guardado en: {latex_path}")