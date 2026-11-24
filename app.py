flask import Flask

@app.route('/')
def home():
    return("initial hotel room reservation page")