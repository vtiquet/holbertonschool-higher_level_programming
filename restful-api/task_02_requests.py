#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder, prints the status code,
    and prints the title of each post if the request is successful.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if (response.status_code == 200):
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves the id, title,
    and body of each post into a CSV file named posts.csv.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if (response.status_code == 200):
        all_posts = response.json()

        posts_to_save = []
        for post in all_posts:
            posts_to_save.append({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            })

        fieldnames = ['id', 'title', 'body']

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_to_save)
