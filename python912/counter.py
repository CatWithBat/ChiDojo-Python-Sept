from flask import Flask, render_template, request, url_for, redirect, session
app =Flask(__name__)
app.secret_key = 'Froot Luips'
def visit():
	try:
		session['count'] +=1
	except:
		session['count'] =1
@app.route('/')
def counter():
	visit()
	return render_template('counter.html', count=session['count'])
	
app.run(debug=True)