"""list of adapters
"""

BAD_WORDS = [
    "fuck",
    "fucking",
]


storage_adapter = {
    "import_path": "chatterbot.storage.SQLStorageAdapter",
    "database_uri": "sqlite:///dori.db"
}

bestmatch = {
    "import_path": "chatterbot.logic.BestMatch",
    "excluded_words": BAD_WORDS
}

timelogic = {
    "import_path": "chatterbot.logic.TimeLogicAdapter",
    "negative": [
        "How are you?",
        "How old are you?",
        "What is 2 + 2",
        "What is 4 / 4",
        "What is 5 plus 5"
    ]
}

specific_response = {
    "import_path": "chatterbot.logic.SpecificResponseAdapter",
    "input_text": "Wow",
    "output_text": "Yes :)"
}

logic_adapters = [
    bestmatch,
    timelogic,
    "chatterbot.logic.MathematicalEvaluation",
    specific_response,
]
