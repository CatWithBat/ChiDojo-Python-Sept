from flask import Flask, render_template, request, url_for, redirect, session
import random
app =Flask(__name__)
app.secret_key = 'Froot Luips'

@app.route('/')
def loop():
	try:
		session['total_gold']
	except:
		session['total_gold'] = 0
	return render_template('ninjagold.html')

@app.route('/process_money', methods=['POST'])
def process_money():
	if request.form['building'] == 'farm':
		gold = random.randrange(10,21) 
		message ='farm earned you' + str(gold) + 'gold'
	elif request.form['building'] == 'cave':
		gold = random.randrange(5,11)
		message = 'cave earned you' + str(gold) + 'gold'
	elif request.form['building'] == 'house':
		gold = random.randrange(2,6)
		message = 'house earned you ' + str(gold) + 'gold'
	elif request.form['building'] == 'casino': 
		gold = random.randrange(-50,51)
		message = 'casino earned you' + str(gold) + 'gold'
	session['total_gold'] += gold
	session['message'] = []
	session['message'].append(message)
	return redirect('/')

app.run(debug=True)