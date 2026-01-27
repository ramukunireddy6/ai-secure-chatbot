from rag.pgvector_store import query_pgvector
from llm.embeddings import embed
from rag.reranker_cohere import rerank

def retrieve_context(query):
    embedding= embed(query)
    documents = query_pgvector(embedding)
    rerank_docs= rerank(query,documents,top_k=3)
    return rerank_docs

