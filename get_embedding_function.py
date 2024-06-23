from langchain_community.embeddings import BedrockEmbeddings


def get_embedding_function():
    embeddings = BedrockEmbeddings(
        credentials_profile_name="dev", region_name="us-east-1"
    )
    return embeddings
