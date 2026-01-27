from reranker_cohere import rerank
from reranker_bedrock import bedrock_rerank
from reranker_offline import offline_rerank

def rerank_router(query,docs):
    try:
        return rerank(query,docs,top_k=3)
    except:
        try:
            return bedrock_rerank(query,docs)
        except:
            return offline_rerank(query,docs)