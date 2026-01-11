from database.db import init_db
from services.comment_service import load_comments
from services.reply_service import process_comments
from utils.logger import log

def main():
    log("Initializing database...")
    init_db()

    log("Loading comments...")
    comments = load_comments()

    log("Processing comments...")
    process_comments(comments)

    log("Auto reply system completed.")

if __name__ == "__main__":
    main()
