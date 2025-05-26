from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    conn = get_connection()
    cursor = conn.cursor()

    # Clean tables
    cursor.execute("DELETE FROM articles")
    cursor.execute("DELETE FROM authors")
    cursor.execute("DELETE FROM magazines")
    conn.commit()

    # Seed authors
    authors = [Author("Alice Smith"), Author("Bob Johnson"), Author("Carol Lee")]
    for author in authors:
        author.save()

    # Seed magazines
    magazines = [
        Magazine("Tech Today", "Technology"),
        Magazine("Health Weekly", "Health"),
        Magazine("Food Monthly", "Food")
    ]
    for magazine in magazines:
        magazine.save()

    # Seed articles
    articles_data = [
        ("AI Advances", authors[0].id, magazines[0].id),
        ("Healthy Living Tips", authors[1].id, magazines[1].id),
        ("Best Recipes", authors[2].id, magazines[2].id),
        ("Tech Gadgets", authors[0].id, magazines[0].id),
        ("Nutrition Facts", authors[1].id, magazines[1].id),
        ("Gourmet Cooking", authors[2].id, magazines[2].id),
        ("AI Ethics", authors[0].id, magazines[0].id),
        ("Wellness Trends", authors[1].id, magazines[1].id),
    ]

    for title, author_id, magazine_id in articles_data:
        article = Article(title, author_id, magazine_id)
        article.save()

    conn.close()

if __name__ == "__main__":
    seed()
    print("Database seeded successfully.")
