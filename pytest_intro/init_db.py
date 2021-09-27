# This is used to create the db when the server starts

if __name__ == '__main__':
    from pytest_intro.models import Article
    Article.create_table()
