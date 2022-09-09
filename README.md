### About Project 

This is a skill demonstration project.

I have built a simple web applications using python based FLASK framework (FLASK). It's not a fullstack application. It just has 
frontend and middle application layer. It accepts user's name as input and then greets them by calling there name. 

### How To Run

Open a terminal in the project root directory and run the following commands 

1. Install `virtualenv`:
```
$ pip install virtualenv
```

2. Create virtual environment:
```
$ virtualenv env
```

3. Then run the command:
```
$ .\env\Scripts\activate
```

4. Then install the dependencies:
```
$ (env) pip install -r requirements.txt
```

5. Finally start the web server:
```
$ (env) python app.py
```

This server will start on port 5000 by default. You can change this in `app.py` by changing the following line to this:

```python
if __name__ == "__main__":
    app.run(debug=True, port=<desired port>)
```