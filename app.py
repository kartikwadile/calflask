from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask"

@app.route('/cal',methods=["Get"])
def math_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2=request.json["number2"]
    
    if operation=="add":
        result=int(number1)+int(number2)
    elif operation=="multiply":
        result=int(number1)*int(number2)
    elif operation=="division":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)
    return "the operation is {} and the result is {}".format(operation,result)

if __name__=='__main__':
    app.run()