from kivy.lang import Builder
from kivymd.app import MDApp

kv = '''

Screen:

	MDRaisedButton:
		text: 'sign up'
		pos_hint: {'center_x': .5, 'center_y': .2}

	MDTextField:
		pos_hint: {'center_x': .5, 'center_y': .8}
		hint_text: 'username'
		size_hint_x: 0.75

	MDTextField:
		pos_hint: {'center_x': .5, 'center_y': .6}
		hint_text: 'password'
		size_hint_x: 0.75
		required: 'True'


	'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)


Main().run()
