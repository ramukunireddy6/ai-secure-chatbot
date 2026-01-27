from rag.retriever import retrieve_context
from llm.embeddings import embed
from llm.bedrock import bedrock_embed
from guardrails.pre_guard import pre_guard_check
from guardrails.post_guard import post_guard_check

async def run_agent(query,user):
    pre_guard_check(query)
    embedding = embed(query)
    context = retrieve_context(query)
    response =bedrock_embed(context)
    post_guard_check(response)
    return response