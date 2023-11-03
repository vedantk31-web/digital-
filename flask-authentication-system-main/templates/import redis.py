import email
import redis

def save_user_data(username, email, password):
    """Save the logged-in user data in Redis.

    Args:
        username: The username of the logged-in user.
        email: The email address of the logged-in user.
        password: The password of the logged-in user.
    """

    r = redis.Redis(host='localhost', port=6379)
    r.set('user:' + username, json.dumps({
        'username': username,
        'email': email,
        'password': password
    }))


from flask import Flask, render_template, request, redirect, url_for, json

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Validate the user credentials.

        # Save the logged-in user data in Redis.
        save_user_data(username, email, password)

        # Redirect the user to the home page.
        return redirect(url_for('index'))

    return render_template('login.html')

# ...

if __name__ == '__main__':
    app.run(debug=True)
