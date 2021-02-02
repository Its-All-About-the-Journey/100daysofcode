with open('C:/100daysofcode/source_code/day024/Input/Letters/starting_letter.txt', 'r') as letter:
	lines = letter.readlines()
with open('C:/100daysofcode/source_code/day024/Input/Names/invited_names.txt', 'r') as names:
	names = names.readlines()

for name in names:
	name = name.strip('\n')
	with open(f'C:/100daysofcode/source_code/day024/Output/ReadyToSend/letter_for_{name}.txt', 'w') as output:
		for line in lines:
			if '[name]' in line:
				line = line.replace('[name]', name)
			output.write(line)
