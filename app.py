from fastapi import FastAPI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_classic.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title= "Mi primer agente")

@tool
def multiplicar(a: int, b: int) -> int:
    """Multiplica dos números enteros."""
    return a * b

tools = [multiplicar]

# LLM Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.5,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Prompt para el agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente útil y preciso. Usa las herramientas cuando sea necesario."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])

# Crear el agente
agent = create_agent(
    # llm, tools, prompt, agent_type="zero-shot-react-description"
    llm,tools
)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Endpoint para interactuar con el agente
class Query(BaseModel):
    pregunta: str

@app.post("/agente")
async def ejecutar_agente(query:Query):
    resultado = agent_executor.invoke({"input": query.pregunta})
    return {"respuesta": resultado["output"]}

@app.get("/")
async def root():
    return {"mensaje": "¡Bienvenido a mi primer agente con FastAPI y Gemini!"}

# Para ejecutar la aplicación, usa el comando: uvicorn app:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)