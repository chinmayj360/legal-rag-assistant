from src.graph import graph

while True:
    query = input("Ask your legal question: ")

    result = graph.invoke({"query": query})

    print("\nAnswer:\n", result["answer"])