rfrom flask import Flask, render_template, request, session, flash, redirect
app = Flask(__name__)
app.secret_key = 'Froot Luips'
@app.route('/')
def form():
	return render_template('dsform.html')

@app.route('/result', methods=["POST"])
def result():
	print request.form
	if len(request.form['name'])< 1:
		flash('Add your name')
	else:
		flash('Nice Name')
	if len(request.form['city']) =='---':
		flash('Where are you from?')
	else:
		flash('nice place')
	if len(request.form['lang']) =='---':
		flash('qerioberivobaegorib')
	else:
		flash('speaking the language')
	if len(request.form['comment'])>120:
		flash('shorten that up now')
	else:
		flash('well said')
	session['name'] = request.form['name']
	session['city'] = request.form['city']
	session['lang'] = request.form['lang']
	session['comment'] = request.form['comment']
	return render_template('dsresults.html')

app.run(debug=True)