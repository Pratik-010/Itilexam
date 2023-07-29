from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to ITIL"

@app.route('/modules')
def modules():
    module_names = ['FCN', 'PYTHON', 'ITIL&DEVOPS', 'COSA','CYBER FORENSICS','COMPLIANCE AUDIT']
    return ', '.join(module_names)

@app.route('/me')
def about_me():
    prn_no = "123456789"
    name = "PRATIK"
    phone_number = "+918554887913"
    return f"PRN No.: {prn_no}\nName: {name}\nPhone Number: {phone_number}"

if __name__ == '__main__':
    app.run(port=4000)

