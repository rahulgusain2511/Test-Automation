from flask import Flask, request, render_template

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route("/", methods=["GET", "POST"])
def prime_numbers():
    if request.method == "POST":
        start = int(request.form.get('start'))
        end = int(request.form.get('end'))
        prime_numbers = [num for num in range(start, end + 1) if is_prime(num)]
        return render_template("result.html", prime_numbers=prime_numbers)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
