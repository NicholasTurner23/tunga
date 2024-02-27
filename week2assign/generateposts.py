import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Function to generate a random date within a given range
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Generate 10 random posts
posts = []
for _ in range(10):
    title = fake.sentence(nb_words=6, variable_nb_words=True)
    description = fake.paragraph(nb_sentences=3)
    author = fake.name()
    date_posted = random_date(datetime(2023, 1, 1), datetime(2024, 1, 1))
    date_updated = random_date(date_posted, datetime(2024, 1, 1))
    views = random.randint(0, 1000)
    likes = random.randint(0, 500)

    post = {
        "title": title,
        "description": description,
        "author": author,
        "date_posted": date_posted.strftime('%Y-%m-%d %H:%M:%S'),
        "date_updated": date_updated.strftime('%Y-%m-%d %H:%M:%S'),
        "stats": {
            "views": views,
            "likes": likes
        }
    }
    posts.append(post)


file_name = "random_posts.txt"
with open(file_name, "w") as file:
    for post in posts:
        file.write("Title: {}\n".format(post["title"]))
        file.write("Description: {}\n".format(post["description"]))
        file.write("Author: {}\n".format(post["author"]))
        file.write("Date Posted: {}\n".format(post["date_posted"]))
        file.write("Date Updated: {}\n".format(post["date_updated"]))
        file.write("Views: {}\n".format(post["stats"]["views"]))
        file.write("Likes: {}\n".format(post["stats"]["likes"]))
        file.write("\n")

print("Posts have been written to", file_name)