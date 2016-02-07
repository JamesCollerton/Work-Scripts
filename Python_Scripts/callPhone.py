import sys
from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run(debug=True)

# def main():

# 	print("Hello")



# if __name__ == "__main__":
#     main()
