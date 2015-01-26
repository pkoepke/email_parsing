# http://stackoverflow.com/questions/17872094/python-how-to-parse-things-such-as-from-to-body-from-a-raw-email-source-w
# http://stackoverflow.com/a/14773896/3784441
# http://stackoverflow.com/a/5749208/3784441

# unsure whether to use email.parser or email.message
import os, email.message
from email.parser import Parser
from pprint import pprint

# change to working directory
#os.chdir("..\\email_parsing-emails\\all_emails")
os.chdir("..\\email_parsing-emails\\10_emails")
print "Working directory: " + os.getcwd()

# count how many files are in the working directory and print that
number_of_files = len([name for name in os.listdir('.') if os.path.isfile(name)])
files_completed = 0
print str(number_of_files) + " files to parse."

def get_email_address_only(from_string):
	""" removes all text except the email address from the From string """
	# Split the From email so you are left with only the email address, no extra characters. Delineated by < and >
	from_string_split = from_string.split("<")
	return_value = from_string_split[-1].split(">")[0]
	return return_value
	
def get_email_address_domain_only(email_address_string):
	""" returns the domain portion of an email address """
	# Split the email address so we get the From email domain
	return_value = email_address_string.split("@")[-1]
	return return_value

# open the output file. This keeps it open until everything else is done, then closes it properly.
with open ("output_all_fields.csv", "w") as output_file:

	# write the column headers
	output_file.write("from address,from domain,file size,subject,Delivered-to,Date,To,\n")
	
	# iterate over every file in the directory
	for current_email_file in os.listdir(os.getcwd()):
	
		# if the file ends in .eml, use it.
		if current_email_file.endswith(".eml"):
		
			# get the file size. We'll store this along with the From email address.
			current_file_size = os.stat(current_email_file).st_size
		
			# open the file
			with open (current_email_file, "r") as current_email_file_opened:
				
				# dump the entire file into a String variable.
				# This could probably be improved by grabbing parts of the email from the file instead of reading the whole thing in.
				current_email_text = current_email_file_opened.read()
				
				# create an email.message object using the string we just read in.
				current_email_message = email.message_from_string(current_email_text)
				
				"""# Grab all header fields
				for current_field in current_email_message.items():
					print current_field
					#print current_field[0]"""
				
				# Grab the From field in the email and store the from email address and its domain
				from_string = current_email_message['From']
				if (from_string == None):
					from_string = ""
				from_string_email_address_only = get_email_address_only(from_string)
				from_string_domain = get_email_address_domain_only( from_string_email_address_only )
				
				# Get the subject
				subject = current_email_message['Subject']
				if (subject == None):
					subject = ""
				
				# Get Delivered-to email address
				delivered_to_email_string = current_email_message['Delivered-to']
				if (delivered_to_email_string == None):
					delivered_to_email_string = ""
				delivered_to_email_address = get_email_address_only( delivered_to_email_string )
				
				# Get Date. This is the date and time the email was composed/sent
				date_sent = current_email_message['Date']
				
				# Get To
				to_string = current_email_message["To"]
				if (to_string == None):
					to_string = ""
				to_email_address = get_email_address_only( to_string )
				
				# output all details to the CSV file
				output_file.write(from_string_email_address_only + "," + from_string_domain + "," + str(current_file_size) + ",\"" + subject + "\"," + delivered_to_email_address + ",\"" + date_sent + "\"," + to_email_address + "\n")
				
				# iterate the # of files completed
				files_completed += 1
								# every 100 files, print progress
				if (files_completed % 1000 == 0):
					print str(files_completed) + " of " + str(number_of_files) + " files completed. " + str( 100 * round( (files_completed / float(number_of_files) ), 4 )) + "% complete."
				# pprint (vars(current_email_message))"""


print "Finished."