Articles Project
Overview
This is a command-line interface (CLI) application that manages articles, authors, and magazines. It uses Python classes to model entities and SQLite for persistent data storage. The project demonstrates object-relational mapping (ORM) without an external library, implementing class methods for database CRUD operations and relationships.

Features
Create, update, and retrieve Authors, Articles, and Magazines.

Establish relationships between authors, articles, and magazines.

Query articles by author or magazine.

List magazines by category and their contributors.

List authors contributing more than two articles to a magazine.

Save all data persistently in SQLite database (db.sqlite).

Technologies
Python 3.x

SQLite3

Standard Python libraries (sqlite3)

No external ORM libraries (e.g., SQLAlchemy) used

Installation
Clone the repo:

bash
Copy code
git clone https://github.com/yourusername/articles-project.git
cd articles-project
(Optional) Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
Install any dependencies (if added later):

bash
Copy code
pip install -r requirements.txt
Initialize the database (if you have a script for that, or just run your app and it will create tables as needed).

Usage
Run your CLI or test scripts to interact with the system, for example:

bash
Copy code
python run_cli.py
Or interact directly with the models in Python shell:

python
Copy code
from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

# Create an author
author = Author("John Doe")
author.save()

# Create a magazine
magazine = Magazine("Tech Today", "Technology")
magazine.save()

# Add article
article = author.add_article(magazine, "New Tech Trends")
article.save()

# List author's magazines
print(author.magazines())

# List magazine contributors
print(magazine.contributors())
Project Structure
graphql
Copy code
.
├── lib
│   ├── db
│   │   └── connection.py         # Database connection helper
│   └── models
│       ├── author.py             # Author class
│       ├── article.py            # Article class
│       └── magazine.py           # Magazine class
├── tests                        # (If any tests exist)
├── run_cli.py                   # CLI entry point (if implemented)
├── db.sqlite                   # SQLite database file
└── README.md                   # This file
Database Schema
authors: id (PK), name (text)

magazines: id (PK), name (text), category (text)

articles: id (PK), title (text), author_id (FK), magazine_id (FK)

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

