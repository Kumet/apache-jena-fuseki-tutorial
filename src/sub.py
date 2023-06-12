import logging

from SPARQLWrapper import QueryResult, SPARQLWrapper

from common.configs import configs
from common.logger import init_logger

init_logger(configs.LOGGER_CONFIG_PATH)
logger = logging.getLogger(__name__)

sparql = SPARQLWrapper("http://localhost:3030/ds/sparql")


def create_data(subject: str, predicate: str, object: str) -> QueryResult:
    sparql.setQuery(
        f"""
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    INSERT DATA {{
        <{subject}> <{predicate}> <{object}> .
    }}
    """
    )
    sparql.method = "POST"
    return sparql.query()


if __name__ == "__main__":
    res = create_data("subject_test", "predicate_test", "object_test")
    logger.info(res)
    logger.info(type(res))
