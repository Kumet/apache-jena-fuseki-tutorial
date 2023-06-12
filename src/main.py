from fastapi import FastAPI
from SPARQLWrapper import SPARQLWrapper

app = FastAPI()

# Fuseki server's SPARQL endpoint
sparql = SPARQLWrapper("http://localhost:3030/MyData/sparql")
