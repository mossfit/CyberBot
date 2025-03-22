import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_advisory(query, retrieved_docs):
    """
    Generates a detailed security advisory for the given query and retrieved documents.
    Also provides an assessment of threat severity (scale 1-5).
    """
    # Build the context from retrieved documents
    context = "\n\n".join(
        [f"Title: {doc['title']}\nDescription: {doc['description']}" for doc in retrieved_docs]
    )
    prompt = (
        f"You are a cybersecurity expert. Based on the following information:\n\n"
        f"{context}\n\n"
        f"Provide a detailed security advisory for the query: '{query}'. "
        "Include an assessment of threat severity on a scale of 1 (low) to 5 (high)."
    )
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a cybersecurity expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    
    advisory_text = response.choices[0].message['content']
    return advisory_text

if __name__ == "__main__":
    sample_docs = [
        {"title": "CVE-XXXX", "description": "Sample vulnerability description."},
        {"title": "Security Report", "description": "New threat detected in XYZ."}
    ]
    query = "What should organizations do about the latest threat?"
    advisory = generate_advisory(query, sample_docs)
    print("Generated Advisory:\n", advisory)
