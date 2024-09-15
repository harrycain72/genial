import os
from langchain.chat_models import init_chat_model
from loguru import logger

# ENVIRONMENT VARIABLES
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


def get_connection_for_llm(provider_name, model_name):

    if provider_name == "openai":
        if model_name == "3.5-turbo":
            try:
                llm = init_chat_model("gpt-3.5-turbo", model_provider="openai", temperature=0)
                logger.success("OpenAI model initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing OpenAI model: {str(e)}")
                raise

        elif model_name == "4o":
            try:
                llm = init_chat_model("chatgpt-4o-latest", model_provider="openai", temperature=0)
                logger.success(f"OpenAI model {model_name} initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing OpenAI model: {str(e)}")
                raise
        elif model_name == "4o-mini":
            try:
                llm = init_chat_model("gpt-4o-mini", model_provider="openai", temperature=0)
                logger.success(f"OpenAI model {model_name} initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing OpenAI model: {str(e)}")
                raise
        elif model_name == "o1-preview":
            try:
                llm = init_chat_model("o1-preview", model_provider="openai", temperature=0)
                logger.success("OpenAI model {model_name}  initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing OpenAI model: {str(e)}")
                raise
        elif model_name == "01-mini":
            try:
                llm = init_chat_model("o1-mini", model_provider="openai", temperature=0)
                logger.success("OpenAI model {model_name} initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing OpenAI model: {str(e)}")
                raise
        elif model_name == "4-turbo":
            try:
                llm = init_chat_model("gpt-4-turbo", model_provider="openai", temperature=0)
                logger.success("OpenAI model {model_name}  initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing OpenAI model: {str(e)}")
                raise
        elif model_name == "4":
            try:
                llm = init_chat_model("gpt-4", model_provider="openai", temperature=0)
                logger.success("OpenAI model {model_name}  initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing OpenAI model: {str(e)}")
                raise

    elif provider_name == "anthropic":
        if model_name == "haiku-3":
            try:
                llm = init_chat_model("claude-3-haiku-20240307", model_provider="anthropic", temperature=0)
                logger.success("Anthropic model {model_name}  initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing Anthropic model: {str(e)}")
                raise
        elif model_name == "sonnet-3":
            try:
                llm = init_chat_model("claude-3-sonnet-20240229", model_provider="anthropic", temperature=0)
                logger.success("Anthropic model {model_name}  initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing Anthropic model: {str(e)}")
                raise
        elif model_name == "opus-3":
            try:
                llm = init_chat_model("claude-3-opus-20240229", model_provider="anthropic", temperature=0)
                logger.success("Anthropic model {model_name}  initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing Anthropic model: {str(e)}")
                raise
        elif model_name == "sonnet-3-5":
            try:
                llm = init_chat_model("claude-3-5-sonnet-20240620", model_provider="anthropic", temperature=0)
                logger.success("Anthropic model {model_name}  initialized successfully")
                return llm
            except Exception as e:
                logger.error(f"Error initializing Anthropic model: {str(e)}")
                raise

    else:
        logger.error(f"Provider {provider_name} is not supported for model {model_name}")


def show_supported_models():
    supported_models = {
        "openai": ["3.5-turbo", "4o", "4o-mini", "o1-preview", "o1-mini", "4-turbo", "4"],
        "anthropic": ["haiku-3", "sonnet-3", "opus-3", "sonnet-3-5"]
    }
    return supported_models






