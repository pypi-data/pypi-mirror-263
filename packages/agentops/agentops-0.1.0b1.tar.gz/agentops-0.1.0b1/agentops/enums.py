from enum import Enum


class EventType(Enum):
    LLM = "llms"
    ACTION = "actions"
    API = "apis"
    TOOL = "tools"
    ERROR = "errors"


class Result(Enum):
    SUCCESS = "Success"
    FAIL = "Fail"
    INDETERMINATE = "Indeterminate"


class Models(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_0301 = "gpt-3.5-turbo-0301"
    GPT_3_5_TURBO_0613 = "gpt-3.5-turbo-0613"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT_3_5_TURBO_16K_0613 = "gpt-3.5-turbo-16k-0613"
    GPT_4_0314 = "gpt-4-0314"
    GPT_4 = "gpt-4"
    GPT_4_32K = "gpt-4-32k"
    GPT_4_32K_0314 = "gpt-4-32k-0314"
    GPT_4_0613 = "gpt-4-0613"
    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"


class LLMMessageFormat(Enum):
    STRING = "string"
    CHATML = "chatml"
