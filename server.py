from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

# create dynamic routes:
@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# create a text file to store the contact form data:
def write_to_file(data): # create a function which is writing the data of the contact form into file: database.txt
    with open('database.txt', mode='a') as database:  # file is already existing
        email = data['email'] # grap the data 'email' of the dictionary 'data'
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}') 


# create a csv file to store the contact form data:
def write_to_csv(data):
    with open('database.csv', mode='a') as database_csv:
        email = data['email'] 
        subject = data['subject']
        message = data['message']
        csv_file = csv.writer(database_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)  
            # csv.writer(name_of_database, options: delimiter=',' means is separating every value with a comma, 
            # quotechar='"' means quotes around the values)
        csv_file.writerow([email,subject,message]) # writerow will contain the data we want 


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()  # grap the data from the sent form and convert it into a dictionary
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try it again'








    