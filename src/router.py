def route_query(query):
    query = query.lower()

    if "sue" in query or "legal action" in query:
        return "escalate"

    if "should i" in query or "advice" in query:
        return "escalate"

    return "answer"