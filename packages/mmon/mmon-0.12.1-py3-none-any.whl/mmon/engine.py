from typing import Any, AsyncIterator, List, Optional

import openai
from langchain.agents.agent import AgentExecutor
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent
from langchain.callbacks.base import BaseCallbackHandler
from langchain.chat_models.base import BaseChatModel
from langchain.memory import ConversationBufferMemory
from langchain_core.runnables import RunnableConfig
from langchain_core.runnables.utils import AddableDict
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from loguru import logger

from mmon.config import load_config
from mmon.langchain_callback import LangChainCallbackHandler
from mmon.tools import load_tools


def get_llm() -> ChatOpenAI:
    config = load_config()
    common_openai_params = {
        "temperature": 0,
        "api_key": config.llm.openai_api_key,
        "api_version": config.llm.openai_api_version,
    }
    llm: ChatOpenAI
    if len(config.llm.deployment_id) > 0:
        logger.info(f"Using AzureOpenAI {config.llm.deployment_id}")
        llm = AzureChatOpenAI(
            azure_endpoint=config.llm.openai_api_base,
            deployment_name=config.llm.deployment_id,
            **common_openai_params,  # type: ignore[arg-type,call-arg]
        )
    else:
        logger.info(f"Using OpenAI {config.llm.model}")
        llm = ChatOpenAI(
            base_url=config.llm.openai_api_base,
            model=config.llm.model,
            **common_openai_params,  # type: ignore[arg-type]
        )
    return llm


class Engine:
    executor: AgentExecutor
    callbacks: List[BaseCallbackHandler]

    def __init__(self, llm: Optional[BaseChatModel] = None, verbose_level: int = 0):
        if llm is None:
            llm = get_llm()
        tools = load_tools(llm, verbose_level)
        if verbose_level >= 3:
            openai.log = "debug"  # type: ignore[attr-defined]

        self.executor = create_conversational_retrieval_agent(
            llm=llm,
            tools=tools,
            max_token_limit=2000,
            remember_intermediate_steps=False,
            verbose=verbose_level > 1,
        )
        self.callbacks = [LangChainCallbackHandler()]

    async def arun(self, prompt: str) -> str:
        response: dict[str, Any] = await self.executor.ainvoke(
            {"input": prompt}, callbacks=self.callbacks
        )

        if "output" not in response or not isinstance(response["output"], str):
            raise ValueError(f"Invalid response: {response}")

        return response["output"]

    def astream(self, prompt: str) -> AsyncIterator[AddableDict]:
        # just input prompt without prep_inputs is work, but can't pass type check
        inputs = self.executor.prep_inputs(prompt)
        response = self.executor.astream(
            inputs, RunnableConfig(callbacks=self.callbacks)
        )
        return response
