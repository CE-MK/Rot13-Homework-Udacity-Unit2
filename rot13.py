import webapp2
import cgi
"""
html for the Website

"""

rot13_form="""
<center>
<div align="left">
<h1>ROT13 Text Transform</h1>
<p style="font-size:14px"><b>This input field transforms your text in Rot13 and backwards</b><br/>
Do not know what Rot13 is? </p><a target="_blank" href="http://en.wikipedia.org/wiki/ROT13">click here to learn more</a>
</div>
<div id="div1" style="height:1000px;width:1000px">
<form method = "post">
<br>
<div align="left">
<br><br>
<p>Type in some Text you want to Transform.<br>If you submit the form twice you will get the original Text back</p>
<textarea cols="50" rows="25"  name="text">%(fill)s</textarea>
<br>
<input type = "submit" value="Submit" style="background-color:#99cc00;color:#fff;letter-spacing:0.8pt;cursor:pointer;border:medium none; box-shadow:0;font-size:22px;padding:10px;">
</form>
</div>
</div>
</center>
"""

class Rot13(webapp2.RequestHandler):
	"""
		escape method to make sure there is no code getting submitted
	"""
	def escape_html(self, s):
		return cgi.escape(s, quote = True)

	def trans(self, str_in):
		i = 0
		"""
			National characters transcription module
		"""
		listchar = list(str_in)

		for x in listchar:
			"""
				Convert String to ASCII value
			"""
			x = ord(x)
			if x>=65 and x<=77:
				listchar[i] = x+13
			elif x>=78 and x<=90:
				listchar[i] = x-13
			elif x>=97 and x<=109:
				listchar[i] = x+13
			elif x>=110 and x<=122:
				listchar[i] = x-13
			else :
				listchar[i] = x
			i=i+1

		i=0
		for x in listchar:
			"""
				Convert ASCII value to String
			"""
			x = chr(x)
			listchar[i] = x
			i = i + 1
		"""
		Convert a list of characters into a string
		"""
		str_in = ''.join(listchar)

		return str_in


	def write_form(self, f=""):
		self.response.out.write(rot13_form % {"fill": f})

	def get(self):
		"""
			Show the Form
		"""
		self.write_form()

	def post(self):
		text_trans = self.request.get('text')
		"""
			Trasnlate Text
		"""
		if text_trans:
			text_trans = self.trans(text_trans)
			text_trans = self.escape_html(text_trans)
			self.write_form(text_trans)

		else:
			"""
				Print this message if the Input field is empty
			"""
			self.response.out.write("Please fill in some Text")



#
#
#       END!
#
#

app = webapp2.WSGIApplication([('/', Rot13)], debug = True)
