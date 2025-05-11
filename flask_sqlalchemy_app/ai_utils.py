import spacy
nlp = spacy.load("en_core_web_sm")

CATEGORIES = {
    "shopping": ["buy", "purchase", "order"],
    "work": ["email", "report", "meeting"],
    "health": ["exercise", "gym", "doctor"],
}

def categorize(text):
    doc = nlp(text.lower())
    for token in doc:
        for cat, keywords in CATEGORIES.items():
            if token.lemma_ in keywords:
                return cat
    return "general"