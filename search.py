import sqlite3
from typing import Optional
from pydantic import BaseModel
from typing import Literal

DB_PATH = "products.db"

class ProductQuery(BaseModel):
    category: Literal["laptop", "smartphone", "tablet", "other"]
    max_price: Optional[int] = None
    sort_by: Literal["price_asc", "price_desc"] = "price_asc"


def search_products(query: ProductQuery) -> list[dict]:
    """
    Ищет товары по валидированным параметрам.
    category == "other" -> возвращает пустой список (неподдерживаемая категория).
    """
    if query.category == "other":
        return []

    sql = "SELECT id, name, category, price FROM products WHERE category = ?"
    params = [query.category]

    if query.max_price is not None:
        sql += " AND price <= ?"
        params.append(query.max_price)

    if query.sort_by == "price_asc":
        sql += " ORDER BY price ASC"
    else:
        sql += " ORDER BY price DESC"

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql, params)
    rows = [dict(r) for r in cur.fetchall()]
    conn.close()
    return rows


