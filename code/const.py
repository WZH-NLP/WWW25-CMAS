model_list = {
    "gpt-3.5-turbo": {"abbr": "tb", "publisher": "openai", "max_tokens": 4096},
    "gpt-3.5-turbo-16k": {"abbr": "tb", "publisher": "openai", "max_tokens": 4096 * 4},
    "gpt-3.5-turbo-0613": {"abbr": "tb0613", "publisher": "openai", "max_tokens": 4096},
    "gpt-3.5-turbo-0125": {"abbr": "tb", "publisher": "openai", "max_tokens": 4096 * 4},
    "gpt-3.5-turbo-instruct": {"abbr": "tbinstruct", "publisher": "openai", "max_tokens": 4096},
    "gpt-3.5-turbo-1106": {"abbr": "tb1106", "publisher": "openai", "max_tokens": 4096 * 4},
    "text-davinci-003": {"abbr": "d3", "publisher": "openai", "max_tokens": 4097},
}

dataset_language_map = {
    "wikigold": "en",
    'genia': 'en',
    'conll2003': 'en',
    'conll2003_300_42': 'en',
    'conll2003_300_52': 'en',
    'genia_300_42': 'en',
    'genia_300_52': 'en',
    'msra': 'en',
    'ontonotes4': 'en',
    'wnut17': 'en',
    'bionlp11id': 'en',
}

my_openai_api_keys = [
    {"key": "<api-key>", "set_base": True,
     "api_base": "<base-url>"},
    {"key": "<api-key>", "set_base": True,
     "api_base": "<base-url>"},
]