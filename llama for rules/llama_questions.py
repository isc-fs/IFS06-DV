from langchain_community.llms import Ollama
from langchain.chains import create_history_aware_retriever
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain

llm = Ollama(model="llama2")

loader = PyPDFLoader("data/FS-Rules_2024_v1.0.pdf")
docs = loader.load_and_split()


embeddings = OllamaEmbeddings()


text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
vector = FAISS.from_documents(documents, embeddings)


prompt = ChatPromptTemplate.from_template(
    """Answer the following question based only on the provided context:

<context>
{context}
</context>

Question: {input}"""
)

document_chain = create_stuff_documents_chain(llm, prompt)


retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)


# MEMORY

# First we need a prompt that we can pass into an LLM to generate this search query

prompt = ChatPromptTemplate.from_messages(
    [
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
        (
            "user",
            "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation",
        ),
    ]
)
retriever_chain = create_history_aware_retriever(llm, retriever, prompt)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Give an answer to the question or Select an option from the multiple answer questions validating each option according to the context given below, only one is correct and give a short answer. This is a test, so answers are not trivial, be sure to read the rules properly. Some answers might be from a general aspect in the rules:\n\n{context}",
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}"),
    ]
)
document_chain = create_stuff_documents_chain(llm, prompt)

retrieval_chain = create_retrieval_chain(retriever_chain, document_chain)

chat_history = [
    HumanMessage(content="Can LangSmith help test my LLM applications?"),
    AIMessage(content="Yes!"),
]

chat_history = []
while True:
    input_text = input("\n\nAsk:\n")
    with open("question.txt", "r", encoding="utf-8") as fh:
        input_text = fh.read()
        print("Asking\n", input_text)
    print(
        retrieval_chain.invoke(
            {
                "chat_history": chat_history,
                "input": "Answer the next question about the formula student reglament: "
                + input_text,
            }
        )["answer"]
    )
