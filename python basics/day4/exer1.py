import json


# Exercise 1
def create_prompt(question):

    return f"""
You are a helpful Generative AI assistant.

Answer the following question clearly.

Question:
{question}

Answer:
"""


# Exercise 2
def create_rag_prompt(question, context):

    return f"""
You are a helpful AI assistant.

Answer the question using ONLY the provided context.

Context:
{context}

Question:
{question}

If the answer is not present in the context,
say that you don't have enough information.

Answer:
"""


# Exercise 3
def few_shot_prompt(review):

    return f"""
Classify customer reviews as Positive or Negative.

Examples:

Review:
"I love this product!"
Sentiment:
Positive

Review:
"The product broke immediately."
Sentiment:
Negative

Review:
"Excellent quality."
Sentiment:
Positive

Now classify:

Review:
{review}

Sentiment:
"""


# Exercise 4
def extract_candidate_info(resume):

    return f"""
Extract the following information:

- name
- skills
- experience
- current_role

Return ONLY valid JSON.

Resume:
{resume}
"""


# Test Exercise 1
print("===== EXERCISE 1 =====")

print(
    create_prompt("What are embeddings?")
)


# Test Exercise 2
print("===== EXERCISE 2 =====")

context = """
RAG stands for Retrieval-Augmented Generation.
It retrieves relevant information and provides
that information to an LLM before generating an answer.
"""

print(
    create_rag_prompt(
        "What is RAG?",
        context
    )
)


# Test Exercise 3
print("===== EXERCISE 3 =====")

print(
    few_shot_prompt(
        "The delivery was late but the product is excellent."
    )
)


# Test Exercise 4
print("===== EXERCISE 4 =====")

resume = """
Prakhar is a Java Developer with 4 years of experience.
He works with Java, Spring Boot, Python and AWS.
"""

print(
    extract_candidate_info(resume)
)