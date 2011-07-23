import sublime, sublime_plugin
import os

syntax_files = []

def find_syntax_files():
	global syntax_files

	new = []

	# Packages folder
	for root, dirs, files in os.walk(sublime.packages_path()):
		for name in files:
			try:
				ext = os.path.splitext(name)[-1]
				if ext == '.tmLanguage':
					path = os.path.join(root, name)
					name = os.path.splitext(os.path.split(path)[1])[0]
					new.append((path, name))
			except:
				pass
	
	# Installed Packages
	for root, dirs, files in os.walk(sublime.packages_path()):
		break # don't know how to address tmLanguage files in zips for set_syntax_file
		try:
			ext = os.path.splitext(name)[-1]
			if ext == '.sublime-package':
				pass
		except:
			pass
	
	new.sort(key=lambda x: x[1])
	syntax_files = new

find_syntax_files()

class SyntaxGet(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view

		items = [name for path, name in syntax_files]

		def callback(idx):
			if idx == -1: return # -1 means the menu was canceled
			view.set_syntax_file(syntax_files[idx][0])

		view.window().show_quick_panel(items, callback)
