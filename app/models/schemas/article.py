from model.domain.article import article
from pydantic import BaseModel

def get_one_articls(article) -> dict:
    return{
        "id" : str(article.get("_id")),
        "no" : article.get("no"),
        "title" : article.get("title"),
        "user_id" : article.get("user_id"),
        "content" : article.get("content"),
        "views" : article.get("views"),
        "date" : article.get("datetime")
    }
