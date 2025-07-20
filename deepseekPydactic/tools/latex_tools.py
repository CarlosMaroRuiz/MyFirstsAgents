from pathlib import Path
from typing import Dict, Optional, List, Union, Any
import time
import os
from pydantic_ai import Tool

def latex_generator(
    problem_statement: str,
    solution_steps: List[str],
    final_answer: str,
    statistical_data: Optional[Dict[str, Any]] = None,
    visualizations: Optional[Dict[str, str]] = None,
    filename: Optional[str] = None,
    title: str = "Análisis Estadístico",
    author: str = "DeepSeek Statistical Assistant"
) -> Dict[str, str]:
    """
    Genera código LaTeX para análisis estadístico compatible con Overleaf.
    """
    # Crear nombre de archivo si no se proporciona
    if filename is None:
        timestamp = int(time.time())
        filename = f"estadistica_{timestamp}"
    
    # Generar el código LaTeX directamente como string
    latex_code = []
    
    # Preámbulo
    latex_code.append(r"\documentclass{article}")
    latex_code.append(r"\usepackage[utf8]{inputenc}")
    latex_code.append(r"\usepackage[spanish]{babel}")
    latex_code.append(r"\usepackage{amsmath,amssymb}")
    latex_code.append(r"\usepackage{graphicx}")
    latex_code.append(r"\usepackage{booktabs}")
    latex_code.append(r"\usepackage{xcolor}")
    
    # Configuración de página
    latex_code.append(r"\usepackage[margin=1in]{geometry}")
    
    # Título
    latex_code.append(f"\\title{{{title}}}")
    latex_code.append(f"\\author{{{author}}}")
    latex_code.append(r"\date{\today}")
    
    # Inicio del documento
    latex_code.append(r"\begin{document}")
    latex_code.append(r"\maketitle")
    
    # Problema
    latex_code.append(r"\section{Planteamiento del Problema}")
    latex_code.append(problem_statement)
    
    # Solución paso a paso
    latex_code.append(r"\section{Solución}")
    latex_code.append(r"\begin{enumerate}")
    for step in solution_steps:
        # Reemplazar caracteres especiales de LaTeX
        safe_step = step.replace("_", r"\_").replace("%", r"\%").replace("#", r"\#").replace("&", r"\&")
        latex_code.append(f"\\item {safe_step}")
    latex_code.append(r"\end{enumerate}")
    
    # Datos estadísticos
    if statistical_data:
        latex_code.append(r"\section{Datos Estadísticos}")
        for key, value in statistical_data.items():
            if isinstance(value, (int, float)):
                latex_code.append(f"{key}: {value}\\\\")
            elif isinstance(value, dict):
                # Crear tabla simple
                latex_code.append(r"\begin{center}")
                latex_code.append(r"\begin{tabular}{|l|c|}")
                latex_code.append(r"\hline")
                latex_code.append(f"{key} & Valor \\\\")
                latex_code.append(r"\hline")
                for k, v in value.items():
                    latex_code.append(f"{k} & {v} \\\\")
                latex_code.append(r"\hline")
                latex_code.append(r"\end{tabular}")
                latex_code.append(r"\end{center}")
    
    # Visualizaciones (solo como código LaTeX)
    if visualizations:
        latex_code.append(r"\section{Visualizaciones}")
        for title, tikz_code in visualizations.items():
            latex_code.append(f"\\subsection{{{title}}}")
            if isinstance(tikz_code, str):
                latex_code.append(tikz_code)
            else:
                latex_code.append(f"Visualización: {title}")
    
    # Conclusión
    latex_code.append(r"\section{Conclusión}")
    latex_code.append(final_answer)
    
    # Fin del documento
    latex_code.append(r"\end{document}")
    
    # Unir todo el código
    full_latex_code = "\n".join(latex_code)
    
    # Crear directorio de salida si no existe
    output_dir = Path("outputs/latex")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Guardar el código LaTeX en un archivo
    tex_file = output_dir / f"{filename}.tex"
    with open(tex_file, "w", encoding="utf-8") as f:
        f.write(full_latex_code)
    
    return {
        "latex_code": full_latex_code,
        "file_path": str(tex_file),
        "log": "Archivo LaTeX generado correctamente para Overleaf"
    }


@Tool
def latex_generator_tool(
    problem_statement: str,
    solution_steps: List[str],
    final_answer: str,
    statistical_data: Optional[Dict[str, Any]] = None,
    visualizations: Optional[Dict[str, str]] = None,
    title: str = "Análisis Estadístico"
) -> Dict[str, str]:
    """
    Genera un documento LaTeX profesional con análisis estadístico compatible con Overleaf.
    
    Args:
        problem_statement: Descripción del problema estadístico
        solution_steps: Lista de pasos en la solución
        final_answer: Conclusión del análisis
        statistical_data: Datos estadísticos relevantes (opcional)
        visualizations: Código LaTeX para visualizaciones (opcional)
        title: Título del documento
        
    Returns:
        Diccionario con código LaTeX y ruta al archivo
    """
    return latex_generator(
        problem_statement=problem_statement,
        solution_steps=solution_steps,
        final_answer=final_answer,
        statistical_data=statistical_data,
        visualizations=visualizations,
        title=title
    )