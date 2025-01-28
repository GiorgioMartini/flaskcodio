from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

def load_blog_posts():
    with open('blogPosts.json', 'r') as file:
        data = json.load(file)
        return data, data['blog_posts']

@app.route('/')
def home():
    data, blog_posts = load_blog_posts()  # Reload data on each request
    return render_template('index.html', posts=blog_posts)

@app.route('/add', methods=['POST', 'GET'])
def add():
    data, blog_posts = load_blog_posts()  # Reload data
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']
        
        new_post = {
            "id": len(blog_posts) + 1,
            "author": author,
            "title": title, 
            "content": content
        }
        
        blog_posts.append(new_post)

        with open('blogPosts.json', 'w') as file:
            json.dump(data, file, indent=2)
    return render_template('add.html')

@app.route('/delete/<post_id>', methods=['POST', 'GET'])
def delete_post(post_id):
    data, blog_posts = load_blog_posts()  # Reload data
    if request.method == 'POST':
        post_id = int(post_id)
        updated_posts = [post for post in blog_posts if post['id'] != post_id]
        data['blog_posts'] = updated_posts
        with open('blogPosts.json', 'w') as file:
            json.dump(data, file, indent=2)
    return redirect('/')

@app.route('/update/<post_id>', methods=['POST', 'GET'])
def update_post(post_id):
    data, blog_posts = load_blog_posts()
    post_id = int(post_id)
    
    if request.method == 'GET':
        # Show the update form
        return render_template('update.html', post=blog_posts[post_id - 1])
    
    elif request.method == 'POST':
        # Handle the update
        author = request.form['author']
        title = request.form['title']
        content = request.form['content']

        updated_post = {
            "id": post_id,
            "author": author,
            "title": title,
            "content": content
        }

        blog_posts[post_id - 1] = updated_post
        data['blog_posts'] = blog_posts
        
        with open('blogPosts.json', 'w') as file:
            json.dump(data, file, indent=2)
        
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
