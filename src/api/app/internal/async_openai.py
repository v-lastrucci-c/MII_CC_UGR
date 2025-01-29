import os
import yaml

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_openai import ChatOpenAI
from app.logger_config import logger

from dotenv import load_dotenv
load_dotenv(override=True)

class AsyncOpenAi:
    def __init__(self):
        
        self.llm = ChatOpenAI(
            model = "gpt-4o-mini",
            api_key= os.getenv("OPENAI_API_KEY"),
            max_tokens=4096,
            timeout=30,
            max_retries=3,
        )
    
    async def llm_response(self, user_question: str):
        try:
            system_prompt, user_prompt = self.prepare_llm_prompt(user_question)
            prompt = self._create_prompt_template(system_prompt, user_prompt)
            chain = self._create_chain(prompt)
            response = await self._execute_chain(chain)
            return response
        
        except Exception as error:
            self._handle_exception(error)
    
    @staticmethod
    def _create_prompt_template(system_prompt: list[str], user_prompt: list[str]):
        
        return ChatPromptTemplate.from_messages([
            ("system", system_prompt), ("human", user_prompt)
        ])
        
    def _create_chain(self, prompt):
        return prompt | self.llm | StrOutputParser()

    @staticmethod    
    async def _execute_chain(chain: ChatPromptTemplate):
        return await chain.ainvoke({})
    
    
    def _handle_exception(self, error):
        logger.error(f"Error en la llamada a OpenAI: {error}")
        raise RuntimeError(
            f"{self.llm_response.__qualname__}.{self.llm}: con Error -> {error}"
        ) from error
    
    @staticmethod
    def read_system_prompt() -> tuple[str, str]:
        with open(os.getenv("AICHRONOS_PROMPT_PATH"), "r") as file:
            data = yaml.safe_load(file)
        
        system_prompt = data.get("system_prompt", "")
        user_prompt = data.get("user_prompt", "")
        
        return system_prompt, user_prompt
    
    def prepare_llm_prompt(self, user_question: str):
        system_prompt, user_prompt = self.read_system_prompt()
        
        user_prompt = user_prompt.replace("{USER_QUESTION}", user_question)
        
        return system_prompt, user_prompt