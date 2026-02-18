from langchain_core.prompts.chat import ChatPromptTemplate
from pydantic import SecretStr
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

def call_agent(system_prompt: str, human_prompt: str, transcription: str, openai_api_key: str):
    llm = ChatOpenAI(model="gpt-4.1-nano", api_key=SecretStr(openai_api_key))

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", human_prompt)
    ])
    
    chain = prompt | llm | StrOutputParser()
    
    response = chain.invoke({
        "transcription": transcription
    })
    
    return response
    
