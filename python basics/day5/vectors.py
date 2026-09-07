import math


def cosine_similarity(vector_a, vector_b):

    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = math.sqrt(
        sum(a * a for a in vector_a)
    )

    magnitude_b = math.sqrt(
        sum(b * b for b in vector_b)
    )

    return dot_product / (magnitude_a * magnitude_b)


embeddings = {
    "doc_1": [0.90, 0.80, 0.10],
    "doc_2": [0.20, 0.30, 0.95],
    "doc_3": [0.70, 0.65, 0.25],
}

question_vector = [0.85, 0.75, 0.15]

for doc_id, vector in embeddings.items():

    similarity = cosine_similarity(
        question_vector,
        vector
    )

    print(
        doc_id,
        similarity
    )