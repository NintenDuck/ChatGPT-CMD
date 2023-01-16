import openai

openai.api_key = "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"
model_engine = "text-davinci-002"

def ask_question(question = "Hola"):
    response = openai.Completion.create(engine=model_engine, prompt=question, max_tokens=1024, n=1,stop=None,temperature=0.5)
    ai_response = response["choices"][0]["text"]
    ai_response = ai_response.replace("\n", "")
    return ai_response

