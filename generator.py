import os
from datetime import date
from jinja2 import Environment, FileSystemLoader
from errors import error_codes


root = os.path.dirname(os.path.abspath(__file__))
parent = os.path.abspath(os.path.join(root, os.pardir))
templates_dir = os.path.join(root, 'templates')
production_dir = os.path.join(root, 'docs')

env = Environment(loader=FileSystemLoader(templates_dir))

today = date.today()
# Textual month, day and year
d = today.strftime("%B %d, %Y")

for dirName, subdirList, fileList in os.walk(templates_dir):
	for fname in fileList:
		template = env.get_template(fname)

		if fname == 'base.html':
			continue
		elif fname == 'error.html':
			for code, description in error_codes.items():
				filename = os.path.join(production_dir, code + '.html')

				with open(filename, 'w') as fh:
					fh.write(template.render(error_code=code, error_description=description, updated_on=d))
		else:
			filename = os.path.join(production_dir, fname)

			with open(filename, 'w') as fh:
				fh.write(template.render(updated_on=d))
