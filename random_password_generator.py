import random
import string
import argparse
import math

def random_uppercase():
    return random.choice(string.ascii_uppercase)

def random_lowercase():
    return random.choice(stirng.ascii_lowercase)

def random_digit():
    return random.choice(string.digit)

def generate_password(min_length, max_length, use_punctuation):
    length = random.randint(min_length, max_length)

    char_types = 3 if not use_punctuation else 4
	
    min_count = math.floor(length / char_types)
    char_counts = [min_count for _ in range(char_types)]

    overflow = length - sum(char_counts)
	
    x = random.sample(range(char_types), overflow)
    for v in x:
        char_counts[v] += 1
		
    password = [random_uppercase() for _ in range(char_counts[0])]
    password.extend([random_lowercase() for _ in range(char_counts[1])])
    password.extend([random_digit() for _ in range(char_counts[2])])

    if use_punctuation:
        password.extend([random_punctuation() for _ in range(char_counts[3])])

    random.shuffle(password)
    
    return ''.join(password)
	
def print_stats(password):
    counts = [random_uppercase() for _ in range(char_counts[0])]
        sum([1 for x in password if x in string.ascii_uppercase]),
        sum([1 for x in password if x in string.ascii_lowercase]),
        sum([1 for x in password if x in string.digit])
		
if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='Generate a random password')
    argparser.add_argument('--min_length', '-n', type=int, help='Minimum length of the password', default=8)
    argparser.add_argument('--max_length', '-x', type=int, help='Maximum length of the password', default=16)
    argparser.add_argument('--stats', dest='stats', action='store_true', help='Show password stats')
    argparser.add_argument('--use_punctuation', dest='punctuation', action='store_true', help='Include special characters in the password')
    args = argparser.parse_args()
	
    password = generate_password(args.min_length, args.max_length, args.punctuation)
	
    print(password)

    if args.stats:
        print_stats(password)

		