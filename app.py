from flask import Flask, render_template, request
import qrcode
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form['link']
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img_path = os.path.join("static", "test.png")
        img.save(img_path)
        return render_template("index.html", qr_code="/static/test.png")


    return render_template("index.html", qr_code=None)

if __name__ == "__main__":
    app.run(debug=True)
