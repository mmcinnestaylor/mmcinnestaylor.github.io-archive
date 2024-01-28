import os
from jinja2 import Environment, FileSystemLoader
from errors import error_codes
from teaching import teaching_appointments


root = os.path.dirname(os.path.abspath(__file__))
parent = os.path.abspath(os.path.join(root, os.pardir))
templates_dir = os.path.join(root, 'templates')
production_dir = os.path.join(parent, 'docs')

env = Environment(loader=FileSystemLoader(templates_dir))

for dirName, subdirList, fileList in os.walk(templates_dir):
	for fname in fileList:
		template = env.get_template(fname)

		if fname == 'base.html':
			continue
		elif fname == 'error.html':
			for code, description in error_codes.items():
				filename = os.path.join(production_dir, code + '.html')

				with open(filename, 'w') as fh:
					fh.write(template.render(error_code=code, error_description=description))
		else:
			filename = os.path.join(production_dir, fname)

			with open(filename, 'w') as fh:
				if fname == 'teaching.html':
					fh.write(template.render(teaching_appointments=teaching_appointments))
				else:
					fh.write(template.render())
