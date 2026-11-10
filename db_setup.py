import sqlite3
import os

DB_PATH = "products.db"

def init_db():
    # Пересоздаём базу с нуля при каждом запуске
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    """)

    products = [
        # --- Ноутбуки (laptop) ---
        ("Lenovo IdeaPad 3",        "laptop",     45000),
        ("ASUS VivoBook 15",        "laptop",     58000),
        ("Acer Aspire 5",           "laptop",     62000),
        ("HP Pavilion 14",          "laptop",     75000),
        ("Apple MacBook Air M1",    "laptop",     89000),
        ("Dell XPS 13",             "laptop",    120000),

        # --- Смартфоны (smartphone) ---
        ("Xiaomi Redmi Note 12",    "smartphone", 18000),
        ("Samsung Galaxy A54",      "smartphone", 32000),
        ("Google Pixel 7a",         "smartphone", 45000),
        ("Apple iPhone 14",         "smartphone", 78000),
        ("Samsung Galaxy S23",      "smartphone", 95000),
        ("Apple iPhone 15 Pro",     "smartphone", 130000),

        # --- Планшеты (tablet) ---
        ("Lenovo Tab M10",          "tablet",     22000),
        ("Samsung Galaxy Tab A8",   "tablet",     30000),
        ("Xiaomi Pad 6",            "tablet",     42000),
        ("Apple iPad 10",           "tablet",     55000),
        ("Samsung Galaxy Tab S9",   "tablet",     85000),
    ]

    cur.executemany(
        "INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
        products
    )

    conn.commit()
    conn.close()
    print(f"База {DB_PATH} создана, добавлено {len(products)} товаров.")

if __name__ == "__main__":
    init_db()