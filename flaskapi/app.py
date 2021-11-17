from flask import Flask, json, jsonify, request

app = Flask(__name__)

# Users data
with open('users.json') as filename:
    users_list = json.load(filename)


# route for GET and POST
@app.route('/users', methods=['GET','POST'])
def users():
    # Request the GET method
    if request.method == 'GET':
        # encoode the list of users into JSON
        if len(users_list) > 0:
            return jsonify(users_list)
        else:
            'Nothing Found', 404

    
    # Request the POST method
    if request.method == 'POST':
        # Create a new user object and add to list
        new_fname = request.form['first_name']
        new_lname = request.form['last_name']
        new_email = request.form['email']
        # Increase the ID from bottom
        Id = users_list[-1]['id']+1

        # create object with the values and append to list
        get_users ={
            'id':Id,
            'first_name':new_fname,
            'last_name':new_lname,
            'email':new_email
        }

        users_list.append(get_users)

        # encode the list to json
        return jsonify(users_list), 201

# route to get, update and delete by user's id
@app.route('/user/<int:id>',methods=['GET','PUT','DELETE'])
def single_user(id):
    # Get the request
    if request.method=='GET':
        for user in users_list:
            if user['id']==id:
                return jsonify(user)
            pass

    # PUT request method
    if request.method == 'PUT':
        for user in users_list:
            if user['id']==id:
                user['email']=request.form['email']
                user['first_name']=request.form['first_name']
                user['last_name']=request.form['last_name']

                updated_user={
                    'id':id,
                    'email':user['email'],
                    'first_name':user['first_name'],
                    'last_name':user['last_name']
                }
                return jsonify(updated_user)

    # Delete request method
    if request.method == 'DELETE':
        # loop through the users' index and iterate from the users list
        for index, user in enumerate(users_list):
            if user['id']==id:
                users_list.pop(index)
                return jsonify(users_list)


# main section
if __name__=='__main__':
    app.run(debug=True)