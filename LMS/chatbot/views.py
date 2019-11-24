from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


def about(request):
    return render(request, 'chatbot/about.html')

def courses(request):
    return render(request, 'chatbot/courses.html')


chatbot = ChatBot('LMS', logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch',
'threshold': 0.70,
'default_response': 'Sorry! I didnot understand' 
}])

trainer = ListTrainer(chatbot)

trainer.train([
	"Hi there!",
	"Hello",
])
trainer.train([
	"hi there",
	"Hello",
])
trainer.train([
	"how are you?",
	"I am doing well, how about you?",
])
trainer.train([
	"I'm also good.",
	"That's good to hear.",
])
trainer.train([
	"Hello",
	"Hi there!",
])
trainer.train([
	"How are you doing?",
	"I am doing well.",
])
trainer.train([
	"Can you help me?",
	"Of course! I can help you.",
])
trainer.train([
	"I have a question",
	"What is your question?",
])
trainer.train([
	"I want to learn about courses.",
	"What is your field of study?",
])
trainer.train([
	"science",
	"which branch (Physics Chemistry or Biology)?",
])
trainer.train([
	"physics",
	"try PHY101 Physics",
])
trainer.train([
	"tell me more about physics",
	"try PHY301 Circuit Theory",
])
trainer.train([
	"biology",
	"try BIO201 Cell Biology",
])
trainer.train([
	" tell me more about biology",
	"try BIO202 Biochemistry-1",
])
trainer.train([
	"something more about biology",
	"try BIO302 Molecular Biology",
])
trainer.train([
	"Chemistry",
	"try BIO202 Biochemistry-1",
])

trainer.train([
	"management",
	"which branch (Administration, Production or Human Resourse)?",
])

trainer.train([
	"human resourse",
	"try HRM617 Training and Development",
])
trainer.train([
	"more about human resourse",
	"try HRM625 Conflict Management",
])
trainer.train([
	"some thing related to human resourse",
	"try HRM627 Human Resourse Development",
])
trainer.train([
	"administration",
	"try MGMT622 Management Skills",
])
trainer.train([
	"tell me changed management",
	"try MGMT625 Changed Management",
])
trainer.train([
	"Project management",
	"try MGMT627 Project Management",
])
trainer.train([
	"urdu",
	"try URD101 Urdu",
])
trainer.train([
	"tell me about reserch methods",
	"try STA630 Advance Research Methods",
])
trainer.train([
	"statistics",
	"try STA301 Probability & Statistics",
])
trainer.train([
	"computer science",
	"We offer many courses of computer",
])
trainer.train([
	"tell me about computer",
	"try CS101 Introduction to Computing",
])
trainer.train([
	"I want to learn programming",
	"try CS201 Introduction to Programming",
])
trainer.train([
	"mathematics",
	"try MTH101 Calcus and analytical mathematics",
])
trainer.train([
	"Accounting",
	"try MGT101 Financial Accounting",
])
trainer.train([
	"How are you doing?",
	"I am doing well, how about you?",
])
trainer.train([
	"I am also good.",
	"That's good.",
])
trainer.train([
	"Have you heard the news?",
	"What good news?",
])
trainer.train([
	"What is your favorite book?",
	"I can't read.",
])
trainer.train([
	"So what's your favorite color?",
	"Black",
])
trainer.train([
	"Who are you?",
	"Who? Who is but a form following the function of what",
])
trainer.train([
	"What are you then?",
	"A man in a mask.",
])
trainer.train([
	"Are you a robot?",
	"Yes I am.",
])




@csrf_exempt
def get_response(request):
	response = {'status': None}

	if request.method == 'POST':
		data = json.loads(request.body)
		message = data['message']

		chat_response = chatbot.get_response(message).text
		response['message'] = {'text': chat_response, 'user': False, 'chat_bot': True}
		response['status'] = 'ok'

	else:
		response['error'] = 'no post data found'

	return HttpResponse(
		json.dumps(response),
			content_type="application/json"
		)
def home(request, template_name="chatbot/home.html"):
	context = {'title': 'LMS Chatbot Version 1.0'}
	return render_to_response(template_name, context, request)
