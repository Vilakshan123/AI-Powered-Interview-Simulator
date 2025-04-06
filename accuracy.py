from langchain.chat_models import ChatOpenAI

def evaluate_candidate_response(query, reply):
    instruction = f"""
    Rate the candidate's answer from 1 to 10.
    Question: {query}
    Answer: {reply}
    Also, include a short explanation for the rating.
    """
    language_model = ChatOpenAI()
    evaluation_result = language_model.predict(instruction)
    return evaluation_result
