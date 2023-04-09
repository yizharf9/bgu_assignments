import datetime

'''
message format:
msg_i=[
	id:int,
	username:str,
	content:str,
	time_of_send:str(time)
]
'''

#region
def current_time_to_str():
    time = datetime.datetime.now()
    return time.strftime("%H:%M:%S")

def is_member(username, conversation_members):
	return username in conversation_members

def enough_space(msg_content:str, conversation_size:int, max_conversation_size:int)->bool:
	#TODO
	return len(msg_content) + conversation_size <= max_conversation_size

def conversation_is_empty(conversation):
	return len(conversation) == 0

def msg_to_string(msg):
	msg_str = "("+str(msg[0])+") "+msg[3]+" "+msg[1]+": "+msg[2]+"\n"
	return msg_str

def conversation_to_string(conversation:list)->str:
	#TODO
    output = ''
    for msg in conversation:
        output += msg_to_string(msg)
    return output[:-1]

def show_conversation(conversation):
	print(conversation_to_string(conversation))

def send_msg(username:str, msg_content:str, msg_last_id:int, conversation_size:int, max_conversation_size:int, conversation:list):
	#TODO
	if enough_space(msg_content,conversation_size,max_conversation_size):
		conversation_size += len(msg_content)
		msg_last_id += 1
		new_msg = [msg_last_id,username,msg_content,current_time_to_str()]
		conversation.append(new_msg)
		# print(conversation_size)
	# else:
		# print("There is not enough space in the storage!")
	return msg_last_id,conversation_size

def find_msg_index(msg_id, conversation):
	#TODO 
	for i,msg in enumerate(conversation):
		if msg[0] == msg_id:
			return i
	return -1
    
def delete_msg(msg_id, conversation_size, conversation):
	#TODO
	index = find_msg_index(msg_id,conversation)
	if index != -1 :
		deleted_msg = conversation[index]
		conversation_size = conversation_size - len(deleted_msg)
		conversation.pop(index)
		return conversation_size
	else:
		return -1

def star_marking(msg_id, conversation):
	#TODO
	index = find_msg_index(msg_id,conversation)
	if index!=-1:
		if len(conversation[index]) == 4 :
			conversation[index].append('Starred')
		else:
			conversation[index].pop(4)
		return 0 
	else:
		return -1

def print_starred_messages(conversation):
	#TODO
	output = ''
	for msg in conversation:
		if (len(msg) == 5) and (msg[4] == "Starred"):
			output += msg_to_string(msg)
	if len(output) == 0:
		return -1
	else: 
		return output[:-1]

def file_fixing(filename:str):
	#TODO
	if filename.endswith('.txt') :
		fh = open(filename)
		output = ''
		for char in fh.read():
			output = char + output

def count_chars(full_txt:str):
	char_count:dict[str,int] = {}
	for char in full_txt:
		ascii_i = ord(char.upper())
		if ascii_i>=65 and ascii_i<=90 :
			char_count[char.upper()] = char_count.get(char.upper(),0)+1
	sorted_char_count = sorted(char_count,key=lambda key : char_count[key],reverse=True)
	return(sorted_char_count[0],char_count[sorted_char_count[0]])

def contains_abc(conversation:list)->int:
	count = 0
	for msg in conversation:
		contains_all = True
		msg_txt = msg[2] 
		for i in range(65,91):
			if (not chr(i).lower() in msg_txt) and (not chr(i).upper() in msg_txt) :
				contains_all = False
		if contains_all : count += 1
	return count

def internal_check(conversation:list):
	#TODO
	full_abc = contains_abc(conversation)
	
	full_txt = ''
	for msg in conversation:
		msg_txt = msg[2]
		full_txt+= msg_txt
	
	(freq_char,num_of_times) = count_chars(full_txt)
	

	return (full_abc,freq_char,num_of_times)


#endregion

def interactive_system(conversation_members = ("yizhar","Steve", "Bill"), max_conversation_size = 300):
	conversation_size = 0
	conversation = []
	msg_last_id = 0
	while True:
		print("##################################################\nWelcome to UpWhats! What would you like to do?\n\
[0] End conversation\n[1] Show full conversation\n[2] Send new message\n[3] Remove existing message\n\
[4] Star a message\n[5] Show starred messages\n[6] Internal check")
		username = input("Please enter username (only conversation's members are allowed to send/read messages.)\n")
		if is_member(username, conversation_members):
			choice = input("Please type your choice and press ENTER\n")
			if choice not in ["0", "1", "2", "3", "4", "5", "6"]:
				print("Invalid choice")
				continue
			if choice == '0':
				print("Thank you for using UpWhats! See you soon. Bye.")
				break
			elif choice == '1':
				if conversation_is_empty(conversation):
					print("Conversation is empty")
				else:
					show_conversation(conversation)
			elif choice == '2':
				msg_content = input("Please type your message.\n")
				prev_msg_last_id, prev_conversation_size = msg_last_id, conversation_size
				msg_last_id, conversation_size = send_msg(username, msg_content, msg_last_id, conversation_size, max_conversation_size, conversation)
				if prev_msg_last_id == msg_last_id and prev_conversation_size == conversation_size:
					print("There is not enough space in the storage!")
				else:
					print("Message was sent successfully!")
			elif choice == '3':
				msg_id = input("Please enter message id.\n")
				new_size = delete_msg(int(msg_id), conversation_size, conversation)
				if new_size == -1:
					print("There is no message with this identifier")
				else:
					conversation_size = new_size
					print("Message was removed successfully!")
			elif choice == '4':
				msg_id = input("Please enter message id.\n")
				marked = star_marking(int(msg_id), conversation)
				if marked == -1:
					print("There is no message with this identifier")
			elif choice == '5':
				starred_concat = print_starred_messages(conversation)
				if starred_concat == -1:
					print("There are no starred messages")
				else:
					print(starred_concat)
			elif choice == '6':
				internal_check_tuple = internal_check(conversation)
				print("The number of messages that contains all the alphabet is {0}, and the most common char is '{1}' \
which appeared {2} times".format(str(internal_check_tuple[0]), internal_check_tuple[1], internal_check_tuple[2]))
		else:
			print("You're not a member of this group!")

if __name__ == "__main__":
    interactive_system()