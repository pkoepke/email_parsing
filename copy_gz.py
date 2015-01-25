import os

to_directory = "H:\Programming\Python\email parsing\all_emails_zipped\gz no folders python copy"
from_directory = "H:\Programming\Python\email parsing\all_emails_zipped\temp"

for current_file in from_directory:
	if current_file.endswith(".gz"):
		print "yes"