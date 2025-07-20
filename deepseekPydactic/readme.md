# 🔄 DeepSeek Statistical Analysis Agent - Flujo del Proyecto

## 📊 Diagrama de Flujo del Sistema

```
┌─────────────────────┐
│   INICIO APLICACIÓN │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ DEFINICIÓN PROBLEMA │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐    ┌─────────────────────┐    ┌─────────────────────┐
│   CONFIG SISTEMA    │───▶│  DEEPSEEK PROVIDER  │───▶│   OPENAI MODEL     │
└──────────┬──────────┘    └─────────────────────┘    └─────────────────────┘
           │
           ▼
┌─────────────────────┐
│ INICIALIZACIÓN      │
│      AGENT          │◄────┐
└──────────┬──────────┘     │
           │                │
           ▼                │
┌─────────────────────┐     │
│  SYSTEM PROMPT      │─────┤
│ (math_prompt.py)    │     │
└─────────────────────┘     │
                            │
┌─────────────────────┐     │
│     TOOLS           │─────┤
│ (latex_generator)   │     │
└─────────────────────┘     │
                            │
┌─────────────────────┐     │
│   OUTPUT TYPE       │─────┘
│ (StatisticsResult)  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  EJECUCIÓN AGENT    │
│   (run_sync)        │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ ANÁLISIS ESTADÍSTICO│
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ GENERACIÓN LATEX    │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ RESULTADO FINAL     │
│   ESTRUCTURADO      │
└─────────────────────┘
```

## 🧩 Arquitectura de Componentes

```
                    DEEPSEEK STATISTICAL ANALYSIS AGENT
                    =====================================

┌─────────────────────────────────────────────────────────────────────────────┐
│                              PYDANTIC AI CORE                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │     AGENT       │    │     MODEL       │    │   SYSTEM PROMPT │         │
│  │  (stats_agent)  │◄──►│   (DeepSeek)    │    │ (math_prompt.py)│         │
│  │                 │    │                 │    │                 │         │
│  └─────────┬───────┘    └─────────────────┘    └─────────────────┘         │
│            │                                                               │
│            ▼                                                               │
│  ┌─────────────────┐    ┌─────────────────────────────────────────────┐   │
│  │     TOOLS       │    │           OUTPUT TYPE                       │   │
│  │(@Tool decorator)│    │        (StatisticsResult)                   │   │
│  │                 │    │                                             │   │
│  └─────────────────┘    └─────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           MÓDULOS DEL SISTEMA                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  config/           system_promp/        tools/              outputs/        │
│  ┌─────────┐      ┌─────────────┐     ┌─────────────┐     ┌─────────────┐   │
│  │ Config  │      │Math Prompts │     │LaTeX Tools  │     │Pydantic     │   │
│  │ (.env)  │      │             │     │             │     │Models       │   │
│  └─────────┘      └─────────────┘     └─────────────┘     └─────────────┘   │
│                                                                             │
│  provider_model/                                                            │
│  ┌─────────────────┐                                                       │
│  │ DeepSeek        │                                                       │
│  │ Provider        │                                                       │
│  └─────────────────┘                                                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

## 🔧 Métodos y Clases de Pydantic AI Utilizados

### 1. 🤖 `Agent` (Clase Principal)

**Ubicación**: `agent_basic_math.py`

```python
from pydantic_ai import Agent

stats_agent = Agent(
    model=model,                    # Modelo de IA (DeepSeek)
    output_type=StatisticsResult,   # Tipo de salida estructurada
    system_prompt=STATISTICS_SYSTEM_PROMPT,  # Prompt del sistema
    tools=[latex_generator_tool]    # Herramientas disponibles
)
```

**Métodos utilizados:**
- **`Agent()`**: Constructor que inicializa el agente
  - `model`: Especifica el modelo de IA a usar
  - `output_type`: Define la estructura de salida usando Pydantic
  - `system_prompt`: Instrucciones base para el agente
  - `tools`: Lista de herramientas disponibles

- **`run_sync()`**: Ejecuta el agente de forma síncrona
  ```python
  result = stats_agent.run_sync(problem)
  ```

### 2. 🛠️ `Tool` (Decorador)

**Ubicación**: `tools/latex_tools.py`

```python
from pydantic_ai import Tool

@Tool
def latex_generator_tool(
    problem_statement: str,
    solution_steps: List[str],
    final_answer: str,
    statistical_data: Optional[Dict[str, Any]] = None,
    visualizations: Optional[Dict[str, str]] = None,
    title: str = "Análisis Estadístico"
) -> Dict[str, str]:
```

**Características:**
- **`@Tool`**: Decorador que registra una función como herramienta del agente
- **Validación automática**: Los parámetros se validan automáticamente
- **Documentación**: La docstring se usa para describir la herramienta al LLM

### 3. 📤 `BaseModel` (Pydantic)

**Ubicación**: `outputs/math_output.py`

```python
from pydantic import BaseModel

class StatisticsResult(BaseModel):
    analysis_steps: list[str]      # Lista de pasos del análisis
    final_conclusion: str          # Conclusión final
    latex_code: str               # Código LaTeX generado
    details_execution: str        # Detalles de ejecución
```

**Características:**
- **Validación automática**: Valida tipos de datos
- **Serialización**: Convierte automáticamente la salida del LLM
- **Documentación**: Proporciona estructura clara al modelo

### 4. 🔗 `OpenAIModel` y `DeepSeekProvider`

**Ubicación**: `provider_model/deepseek_provide.py`

```python
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.deepseek import DeepSeekProvider

model = OpenAIModel(
    'deepseek-chat',
    provider=DeepSeekProvider(api_key=config_context.deepseek_api_key),
)
```

**Componentes:**
- **`OpenAIModel`**: Wrapper para modelos compatibles con OpenAI API
- **`DeepSeekProvider`**: Proveedor específico para DeepSeek
- **Configuración**: Maneja autenticación y conexión

## 🔄 Flujo de Ejecución Detallado

### Fase 1: Inicialización
1. **Carga de configuración** (`config/config.py`)
   - Variables de entorno
   - API keys

2. **Configuración del modelo** (`provider_model/deepseek_provide.py`)
   - DeepSeek provider
   - OpenAI model wrapper

3. **Creación del agente** (`agent_basic_math.py`)
   - Registro de herramientas
   - Configuración de tipos de salida
   - System prompt

### Fase 2: Procesamiento
1. **Recepción del problema**
   - Input del usuario con problema estadístico

2. **Análisis por DeepSeek**
   - Procesamiento del system prompt
   - Razonamiento estadístico
   - Identificación de herramientas necesarias

3. **Uso de herramientas**
   - Llamada a `latex_generator_tool`
   - Generación de código LaTeX
   - Guardado de archivos

### Fase 3: Salida
1. **Estructuración de resultados**
   - Validación con `StatisticsResult`
   - Formateo automático

2. **Generación de archivos**
   - Archivo LaTeX en `outputs/latex/`
   - Código estructurado

## 🎯 Ventajas del Enfoque Pydantic AI

### ✅ Beneficios Clave

1. **Validación Automática**
   - Los tipos se validan automáticamente
   - Errores claros en caso de problemas

2. **Estructura Clara**
   - Salidas consistentes y predecibles
   - Fácil integración con otros sistemas

3. **Herramientas Tipadas**
   - IntelliSense completo
   - Menos errores en tiempo de desarrollo

4. **Escalabilidad**
   - Fácil añadir nuevas herramientas
   - Modificación simple de tipos de salida

### 🔧 Puntos de Extensión

1. **Nuevas herramientas**: Decorar con `@Tool`
2. **Nuevos tipos de salida**: Extender `BaseModel`
3. **Diferentes modelos**: Cambiar provider en configuración
4. **Prompts especializados**: Modificar system prompts

## 📋 Ejemplo de Uso Completo

```python
# 1. Inicialización automática del agente
from deepseekPydantic.agent_basic_math import stats_agent

# 2. Definición del problema
problem = """
Problema estadístico aquí...
"""

# 3. Ejecución (Pydantic AI maneja toda la validación)
result = stats_agent.run_sync(problem)

# 4. Acceso a resultados estructurados
print("Pasos:", result.output.analysis_steps)
print("Conclusión:", result.output.final_conclusion)
print("LaTeX:", result.output.latex_code)
```

## 🔍 Métodos Específicos de Pydantic AI

| Método/Clase | Ubicación | Propósito |
|--------------|-----------|-----------|
| `Agent()` | `pydantic_ai` | Constructor principal del agente |
| `run_sync()` | `Agent` | Ejecución síncrona |
| `@Tool` | `pydantic_ai` | Decorador para herramientas |
| `BaseModel` | `pydantic` | Modelos de datos estructurados |
| `OpenAIModel` | `pydantic_ai.models.openai` | Wrapper de modelos |
| `DeepSeekProvider` | `pydantic_ai.providers.deepseek` | Proveedor específico |

---

**🎯 Este flujo garantiza un análisis estadístico robusto, validado y reproducible usando las mejores prácticas de Pydantic AI.**