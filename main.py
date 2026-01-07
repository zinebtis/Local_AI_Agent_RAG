from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever



model = OllamaLLM(model="llama3.2")

template ="""
you are a expert in answering questions about a pizza restaurant
here are some reviews from customers:{reviews}
here is the question to answer:{question}
provide a detailed answer based on the reviews.

"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
    question = input("Enter your question about the pizza restaurant:\n ")
    if question.lower() in ["exit", "quit"]:
        break
    print("\n -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-\n")
    reviews = retriever.invoke(question)
    response = chain.invoke({"reviews": reviews, "question": question})
    print(response)
