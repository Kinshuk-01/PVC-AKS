from flask  import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage (empty at start)
BOOKS = []
NEXT_ID = 1


@app.route('/')
def home():
    return redirect(url_for('books'))


@app.route('/books', methods=['GET'])
def books():
    return render_template('books.html', books=BOOKS)


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    global NEXT_ID

    if request.method == 'POST':
        book = {
            "id": NEXT_ID,
            "title": request.form.get('title'),
            "author": request.form.get('author'),
            "year": int(request.form.get('year'))
        }

        BOOKS.append(book)
        NEXT_ID += 1

        return redirect(url_for('books'))

    return render_template('add_book.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
