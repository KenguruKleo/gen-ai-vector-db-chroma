import os
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv

load_dotenv()


api_key = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=api_key, ssl_verify=False)

index_name = "developer-quickstart-py"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=8,  # Replace with your model dimensions
        metric="euclidean",  # Replace with your model metric
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    
index = pc.Index(index_name)

# index.upsert(
#   vectors=[
#     {
#       "id": "A", 
#       "values": [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1], 
#       "metadata": {"genre": "comedy", "year": 2020}
#     },
#     {
#       "id": "B", 
#       "values": [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2],
#       "metadata": {"genre": "documentary", "year": 2019}
#     },
#     {
#       "id": "C", 
#       "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
#       "metadata": {"genre": "comedy", "year": 2019}
#     },
#     {
#       "id": "D", 
#       "values": [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4],
#       "metadata": {"genre": "drama"}
#     }
#   ],
#   namespace="example-namespace"
# )

res = index.query(
    namespace="example-namespace",
    vector=[0.0236663818359375,-0.032989501953125, 0, 0, 0, 0, -0.01041412353515625,0.0086669921875], 
    top_k=3,
    include_metadata=True,
    include_values=False
)

print("Query Results:")
print('--------------')
for match in res.matches:
    print(f"ID: {match.id}, Score: {match.score}, Metadata: {match.metadata}")