from pathlib import Path
from typing import Dict, Optional, List
from pylatex import Document, Section, Math, Command, Enumerate, Itemize
from pylatex.utils import italic, NoEscape
import time

def latex_generator(
    problem_statement: str,
    solution_steps: List[str],
    final_answer: str,
    filename: Optional[str] = None,
    packages: List[str] = ["amsmath", "amssymb"],
    title: str = "Solución Matemática",
    author: str = "Asistente de Álgebra"
) -> Dict[str, str]:
    """
    Genera un archivo LaTeX profesional con la solución matemática.
    
    Args:
        problem_statement: Ecuación o problema original
        solution_steps: Lista de pasos de solución
        final_answer: Respuesta final
        filename: Nombre del archivo (sin extensión)
        packages: Lista de paquetes LaTeX a incluir
        title: Título del documento
        author: Autor del documento
        
    Returns:
        dict: {
            "status": "success"|"error",
            "filepath": str,
            "latex_code": str,
            "message": str
        }
    """
    try:
        # Configuración inicial
        filename = filename or f"math_solution_{int(time.time())}"
        doc = Document(filename)
        
        # Metadatos y paquetes
        doc.preamble.append(Command('title', title))
        doc.preamble.append(Command('author', author))
        doc.preamble.append(Command('date', NoEscape(r'\today')))
        doc.append(NoEscape(r'\maketitle'))
        
        for pkg in packages:
            doc.preamble.append(Command('usepackage', pkg))
        
        # Contenido del documento
        with doc.create(Section('Problema Original')):
            doc.append(Math(data=[problem_statement], escape=False))
        
        with doc.create(Section('Solución Paso a Paso')):
            with doc.create(Enumerate()) as enum:
                for step in solution_steps:
                    enum.add_item(NoEscape(step))
                    # Si el paso contiene ecuaciones, las añadimos
                    if '=' in step:
                        doc.append(Math(data=[step.split(':')[-1].strip()], escape=False))
        
        with doc.create(Section('Resultado Final')):
            doc.append(Math(data=[final_answer], escape=False))
            doc.append(NoEscape(r'\boxed{' + final_answer + '}'))
        
        # Generar archivo
        doc.generate_tex()
        
        # Leer el contenido generado
        tex_content = Path(f"{filename}.tex").read_text(encoding='utf-8')
        
        return {
            "status": "success",
            "filepath": str(Path(f"{filename}.tex").absolute()),
            "latex_code": tex_content,
            "message": "Archivo LaTeX generado correctamente"
        }
        
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "message": "Error al generar el archivo LaTeX"
        }

# Versión simplificada para usar como tool del agente
def latex_generator_tool(
    problem: str,
    steps: List[str],
    solution: str,
    **kwargs
) -> Dict[str, str]:
    """
    Tool para que el agente genere documentos LaTeX.
    
    Args:
        problem: Ecuación o problema original
        steps: Pasos de solución (lista de strings)
        solution: Solución final
        **kwargs: Opciones adicionales (filename, packages, etc.)
        
    Returns:
        dict: Resultado de la generación
    """
    return latex_generator(
        problem_statement=problem,
        solution_steps=steps,
        final_answer=solution,
        **kwargs
    )