from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def initialize_rag_pipeline(index_path):
    embedding_model = OpenAIEmbeddings()
    vector_store = FAISS.load_local(index_path, embedding_model)
    retriever_tool = vector_store.as_retriever()
    language_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    rag_chain = RetrievalQA.from_chain_type(llm=language_model, retriever=retriever_tool)
    return rag_chain
