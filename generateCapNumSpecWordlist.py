import sys

# generate word list:
#
#   python generateWordlist.py
# or
#   python generateWordlist.py use_line_number_column
#

# do not modify literal 'words = [' list -- instead, use remove_words()
#   and add_words() functions down below

def remove_words(all_words, words_to_remove):
	return list(set(all_words) - set(words_to_remove))

def add_words(all_words, words_to_add):
	return list(set(all_words) | set(words_to_add))

# starting point is 3-4 characters words in "2025" version of
#   customized wordlist based on EFF's long wordlist, manually culled
words = [
'abc', 'barn', 'both', 'clue', 'defy', 'each', 'fir', 'gem', 'heap', 'inch',
'able', 'base', 'bow', 'coal', 'deli', 'ear', 'firm', 'gen', 'heat', 'info',
'ace', 'bash', 'bowl', 'coat', 'demo', 'earn', 'fish', 'get', 'heed', 'ink',
'ache', 'bat', 'box', 'cod', 'den', 'ease', 'fist', 'gift', 'heel', 'inn',
'acid', 'bath', 'boxy', 'code', 'dent', 'east', 'fit', 'gig', 'held', 'into',
'acre', 'bay', 'brag', 'coil', 'deny', 'easy', 'five', 'gill', 'helm', 'ion',
'act', 'bead', 'brew', 'coin', 'desk', 'eat', 'fix', 'give', 'help', 'iowa',
'add', 'beak', 'brim', 'coke', 'dev', 'echo', 'flag', 'glad', 'hen', 'irk',
'afar', 'beam', 'brow', 'cola', 'dew', 'edge', 'flap', 'glee', 'herb', 'iron',
'age', 'bean', 'buck', 'cold', 'dial', 'edgy', 'flat', 'glow', 'herd', 'isle',
'aged', 'bear', 'bud', 'colt', 'dice', 'edit', 'flaw', 'glue', 'hero', 'itch',
'ago', 'beat', 'buff', 'com', 'did', 'eel', 'flea', 'gnat', 'hey', 'item',
'ahoy', 'bed', 'bug', 'comb', 'dig', 'egg', 'fled', 'goal', 'hid', 'ivy',
'aid', 'bee', 'bulb', 'come', 'dill', 'ego', 'flee', 'goat', 'hide', 'jab',
'aide', 'beef', 'bulk', 'cone', 'dim', 'elf', 'flew', 'gold', 'high', 'jack',
'aim', 'been', 'bull', 'cook', 'dime', 'elk', 'flex', 'golf', 'hike', 'jade',
'air', 'beep', 'bump', 'cool', 'din', 'elm', 'flip', 'gone', 'hill', 'jail',
'ajar', 'beer', 'bun', 'coop', 'dine', 'else', 'flop', 'gong', 'hint', 'jam',
'all', 'bell', 'bunk', 'cope', 'dip', 'emit', 'flow', 'goo', 'hip', 'jar',
'ally', 'belt', 'burn', 'copy', 'dire', 'emu', 'fly', 'good', 'hire', 'java',
'aloe', 'bend', 'bury', 'cord', 'dirt', 'envy', 'foam', 'goof', 'hit', 'jaw',
'also', 'bent', 'bush', 'core', 'disc', 'epic', 'foe', 'goon', 'hive', 'jazz',
'alto', 'best', 'bust', 'cork', 'dish', 'era', 'fog', 'gosh', 'hoax', 'jeep',
'amid', 'bet', 'busy', 'corn', 'disk', 'etc', 'foil', 'got', 'hog', 'jest',
'amp', 'beta', 'buy', 'cost', 'diva', 'euro', 'fold', 'gown', 'hola', 'jet',
'anew', 'bid', 'buzz', 'cot', 'dive', 'eve', 'folk', 'grab', 'hold', 'jig',
'ant', 'big', 'cab', 'cove', 'doc', 'even', 'fond', 'grad', 'hole', 'jinx',
'any', 'bike', 'cafe', 'cow', 'dock', 'ever', 'font', 'gram', 'home', 'job',
'ape', 'bill', 'cage', 'cozy', 'dog', 'evil', 'food', 'grew', 'honk', 'jog',
'app', 'bin', 'cake', 'crab', 'dole', 'exam', 'fool', 'grid', 'hood', 'join',
'apt', 'bind', 'calf', 'cram', 'doll', 'exit', 'foot', 'grin', 'hoof', 'joke',
'aqua', 'bing', 'call', 'crew', 'dome', 'eye', 'for', 'grip', 'hook', 'jolt',
'arc', 'bio', 'calm', 'crib', 'done', 'face', 'ford', 'grit', 'hoop', 'jot',
'arch', 'bird', 'cam', 'crop', 'door', 'fact', 'fore', 'grow', 'hoot', 'joy',
'are', 'bit', 'camp', 'crow', 'dorm', 'fad', 'fork', 'grub', 'hop', 'judo',
'area', 'bite', 'can', 'crux', 'dose', 'fade', 'form', 'gulf', 'hope', 'jug',
'arm', 'blah', 'cane', 'cub', 'dot', 'fail', 'fort', 'gulp', 'horn', 'july',
'army', 'blew', 'cap', 'cube', 'dove', 'fair', 'fox', 'gum', 'hose', 'jump',
'art', 'blip', 'cape', 'cue', 'down', 'fake', 'free', 'guru', 'host', 'june',
'asap', 'blob', 'car', 'cuff', 'doze', 'fall', 'fret', 'gush', 'hot', 'junk',
'ash', 'blog', 'card', 'cup', 'drab', 'fame', 'frog', 'gut', 'how', 'jury',
'ashy', 'blot', 'care', 'curb', 'draw', 'fan', 'from', 'guy', 'howl', 'just',
'ask', 'blow', 'cart', 'cure', 'drew', 'fang', 'fry', 'gym', 'hub', 'kale',
'ate', 'blue', 'case', 'curl', 'drip', 'far', 'fuel', 'hack', 'huff', 'keen',
'atom', 'blur', 'cash', 'cusp', 'drop', 'farm', 'full', 'had', 'hug', 'keep',
'atop', 'bmw', 'cast', 'cut', 'drug', 'fast', 'fun', 'haha', 'huge', 'keg',
'aura', 'boar', 'cat', 'cyan', 'drum', 'fate', 'fund', 'hail', 'huh', 'kelp',
'auto', 'boat', 'cave', 'dab', 'dry', 'fax', 'funk', 'hair', 'hula', 'kept',
'ave', 'bob', 'cell', 'dad', 'dual', 'feat', 'fur', 'half', 'hulk', 'key',
'avid', 'body', 'cent', 'daft', 'duck', 'fed', 'fuse', 'hall', 'hull', 'kick',
'away', 'bog', 'char', 'damp', 'duct', 'fee', 'fuzz', 'halt', 'hum', 'kid',
'awe', 'boil', 'chat', 'dark', 'dude', 'feed', 'gab', 'ham', 'hunk', 'kiln',
'awry', 'bold', 'chef', 'darn', 'duel', 'feel', 'gag', 'hand', 'hunt', 'kilo',
'aye', 'bolt', 'chew', 'dart', 'duet', 'feet', 'gain', 'hare', 'hurt', 'kilt',
'back', 'bond', 'chin', 'dash', 'dug', 'fell', 'gala', 'harm', 'hush', 'kin',
'bag', 'bone', 'chip', 'data', 'duke', 'felt', 'gale', 'harp', 'hut', 'kind',
'bail', 'bony', 'chop', 'date', 'dull', 'fend', 'game', 'hash', 'hymn', 'king',
'bait', 'boo', 'chug', 'dawn', 'duly', 'fern', 'gap', 'hat', 'hype', 'kit',
'bake', 'book', 'city', 'day', 'dump', 'feud', 'gasp', 'hate', 'ice', 'kite',
'ball', 'boom', 'clad', 'deal', 'dunk', 'few', 'gate', 'haul', 'iced', 'kiwi',
'bam', 'boon', 'clam', 'dean', 'duo', 'fig', 'gave', 'have', 'icky', 'knee',
'ban', 'boot', 'clap', 'debt', 'dupe', 'file', 'gawk', 'hawk', 'icon', 'knew',
'band', 'bore', 'claw', 'deck', 'dusk', 'fill', 'gaze', 'haze', 'icy', 'knit',
'bank', 'borg', 'clay', 'deed', 'dust', 'film', 'gear', 'hazy', 'idea', 'knot',
'bar', 'born', 'clip', 'deem', 'duty', 'find', 'geek', 'head', 'idle', 'know',
'bark', 'bot', 'club', 'deep', 'dvd', 'fine', 'gel', 'heal', 'idly', 'kung',
'lab', 'luck', 'moor', 'okay', 'pike', 'putt', 'rome', 'shop', 'soy', 'tear',
'lace', 'lug', 'mop', 'old', 'pile', 'quad', 'romp', 'show', 'spa', 'tech',
'lack', 'lump', 'more', 'omen', 'pill', 'quit', 'roof', 'shun', 'spam', 'tee',
'lair', 'lung', 'most', 'omit', 'pin', 'quiz', 'rook', 'shut', 'span', 'tell',
'lake', 'lure', 'moth', 'once', 'pine', 'race', 'room', 'shy', 'spew', 'temp',
'lamb', 'lurk', 'move', 'only', 'ping', 'rack', 'root', 'side', 'spin', 'tend',
'lamp', 'lush', 'mow', 'onto', 'pink', 'rad', 'rope', 'sift', 'spit', 'tent',
'land', 'mace', 'much', 'onyx', 'pint', 'raft', 'rose', 'sigh', 'spot', 'term',
'lane', 'made', 'muck', 'ooze', 'pip', 'rag', 'rosy', 'sign', 'spry', 'test',
'lang', 'mail', 'mud', 'oozy', 'pipe', 'rage', 'rot', 'silk', 'spud', 'text',
'lap', 'main', 'mug', 'opal', 'pit', 'raid', 'row', 'silo', 'spun', 'that',
'lard', 'make', 'mule', 'open', 'pity', 'rail', 'rub', 'silt', 'spur', 'thaw',
'lark', 'mall', 'mum', 'opt', 'plan', 'rain', 'ruby', 'sim', 'spy', 'thee',
'lash', 'malt', 'muse', 'orb', 'play', 'rake', 'rue', 'sing', 'star', 'them',
'last', 'mama', 'mush', 'orca', 'plea', 'ram', 'rug', 'sink', 'stat', 'then',
'late', 'many', 'must', 'ore', 'plod', 'ramp', 'ruin', 'sip', 'stay', 'they',
'lava', 'map', 'mute', 'ouch', 'plop', 'ran', 'rule', 'sit', 'stem', 'thin',
'law', 'mar', 'mutt', 'our', 'plot', 'rang', 'run', 'six', 'step', 'thud',
'lawn', 'mark', 'myth', 'out', 'plow', 'rank', 'rung', 'size', 'stew', 'tide',
'lax', 'mart', 'nab', 'oval', 'ploy', 'rare', 'runt', 'ski', 'stir', 'tidy',
'lazy', 'mash', 'nag', 'oven', 'plug', 'rash', 'ruse', 'skid', 'stop', 'tie',
'leaf', 'mask', 'nail', 'over', 'plum', 'rat', 'rush', 'skin', 'stun', 'tied',
'leak', 'mat', 'name', 'owe', 'pod', 'rate', 'rust', 'skip', 'sub', 'tile',
'lean', 'math', 'nap', 'owed', 'poem', 'rave', 'rut', 'sky', 'such', 'till',
'leap', 'maw', 'nape', 'owl', 'poet', 'raw', 'rye', 'slab', 'suit', 'tilt',
'led', 'max', 'navy', 'own', 'pogo', 'ray', 'sack', 'slag', 'sulk', 'time',
'left', 'may', 'nay', 'pace', 'poke', 'read', 'safe', 'slam', 'sum', 'tin',
'leg', 'mayo', 'nba', 'pack', 'pole', 'real', 'saga', 'slaw', 'sun', 'tint',
'lego', 'maze', 'near', 'pact', 'poll', 'ream', 'sage', 'sled', 'sung', 'tiny',
'len', 'meal', 'neat', 'pad', 'polo', 'reap', 'said', 'slim', 'sunk', 'tip',
'lend', 'mean', 'neck', 'page', 'pond', 'rear', 'sail', 'slip', 'sure', 'tire',
'lent', 'meat', 'need', 'paid', 'pong', 'red', 'sake', 'slit', 'surf', 'toad',
'let', 'meet', 'neon', 'pair', 'pony', 'redo', 'sale', 'slop', 'suv', 'toe',
'lid', 'mega', 'nerd', 'pal', 'poof', 'reed', 'salt', 'slot', 'swab', 'tofu',
'life', 'melt', 'nest', 'pale', 'pool', 'reef', 'same', 'slow', 'swam', 'toil',
'lift', 'memo', 'net', 'palm', 'pop', 'reel', 'sand', 'slug', 'swan', 'told',
'like', 'mend', 'new', 'pan', 'pope', 'ref', 'sane', 'slum', 'swap', 'toll',
'limb', 'menu', 'newt', 'pang', 'pork', 'rely', 'sang', 'sly', 'swat', 'tomb',
'lime', 'meow', 'next', 'pant', 'port', 'rent', 'sank', 'smog', 'sway', 'ton',
'limo', 'mere', 'nice', 'par', 'pose', 'rep', 'sap', 'smug', 'swim', 'tone',
'line', 'met', 'nod', 'park', 'posh', 'rest', 'sash', 'snag', 'sync', 'took',
'link', 'mic', 'none', 'part', 'post', 'rib', 'sat', 'snap', 'tab', 'tool',
'lint', 'mice', 'noon', 'path', 'pot', 'rice', 'save', 'snow', 'tack', 'top',
'lion', 'mid', 'nope', 'paw', 'pour', 'rich', 'saw', 'snub', 'taco', 'tore',
'lip', 'mild', 'nor', 'pawn', 'pout', 'rid', 'say', 'snug', 'tag', 'torn',
'list', 'mile', 'norm', 'pay', 'pow', 'ride', 'scam', 'soak', 'tail', 'tour',
'lit', 'milk', 'nose', 'pea', 'pox', 'rift', 'scan', 'soap', 'take', 'tow',
'live', 'mill', 'nosy', 'peak', 'prep', 'rig', 'sea', 'soar', 'tale', 'town',
'load', 'mime', 'not', 'pear', 'prey', 'rim', 'seal', 'sock', 'talk', 'toy',
'loaf', 'min', 'note', 'peck', 'pro', 'rind', 'seat', 'sod', 'tall', 'tram',
'loan', 'mind', 'nova', 'peek', 'prop', 'ring', 'see', 'soda', 'tame', 'trap',
'lock', 'mine', 'now', 'peel', 'pry', 'rink', 'seed', 'sofa', 'tan', 'tray',
'loco', 'mini', 'numb', 'peep', 'puck', 'riot', 'seek', 'soft', 'tang', 'tree',
'loft', 'mink', 'nut', 'peer', 'puff', 'rip', 'seem', 'soil', 'tank', 'trek',
'log', 'mint', 'oaf', 'pelt', 'pug', 'ripe', 'self', 'sold', 'tap', 'trim',
'logo', 'mist', 'oak', 'pen', 'pull', 'rise', 'sell', 'sole', 'tape', 'trio',
'lone', 'mix', 'oat', 'pep', 'pulp', 'risk', 'send', 'solo', 'tar', 'trip',
'long', 'mock', 'oath', 'per', 'puma', 'ritz', 'sent', 'some', 'tarp', 'trot',
'look', 'mode', 'oboe', 'perm', 'pump', 'road', 'set', 'song', 'tart', 'true',
'loop', 'mojo', 'odd', 'peso', 'pun', 'roam', 'sew', 'soon', 'task', 'try',
'loot', 'mold', 'off', 'pest', 'punk', 'roar', 'sewn', 'sora', 'tat', 'tub',
'lose', 'mom', 'ogle', 'pet', 'pup', 'robe', 'sham', 'sort', 'tax', 'tuba',
'lost', 'mono', 'ogre', 'pick', 'pure', 'rock', 'shed', 'soul', 'taxi', 'tube',
'lot', 'moo', 'ohio', 'pie', 'purr', 'rode', 'shin', 'soup', 'tea', 'tuck',
'loud', 'mood', 'oil', 'pier', 'push', 'role', 'ship', 'sour', 'teal', 'tuft',
'love', 'moon', 'oink', 'pig', 'put', 'roll', 'shoe', 'sow', 'team', 'tug',
'tuna', 'use', 'vest', 'vow', 'warp', 'west', 'wig', 'wish', 'worn', 'yet',
'tune', 'used', 'vet', 'waco', 'wary', 'wet', 'wild', 'wit', 'wow', 'yoga',
'turf', 'user', 'veto', 'wad', 'wash', 'wham', 'will', 'with', 'wrap', 'york',
'turn', 'utah', 'via', 'wage', 'wasp', 'what', 'wilt', 'woah', 'yak', 'you',
'tusk', 'vain', 'vial', 'wait', 'wave', 'whee', 'wimp', 'wok', 'yam', 'your',
'tutu', 'van', 'vibe', 'wake', 'wavy', 'when', 'win', 'wolf', 'yank', 'yum',
'tux', 'vary', 'vice', 'walk', 'wax', 'whim', 'wind', 'won', 'yard', 'zap',
'twig', 'vase', 'view', 'wall', 'way', 'whiz', 'wine', 'wood', 'yarn', 'zeal',
'twin', 'vast', 'vile', 'wan', 'wear', 'who', 'wing', 'woof', 'yawn', 'zen',
'type', 'veer', 'vine', 'wand', 'web', 'whom', 'wink', 'wool', 'yay', 'zero',
'ufo', 'vega', 'vip', 'want', 'week', 'why', 'wipe', 'word', 'yeah', 'zip',
'undo', 'veil', 'visa', 'ward', 'well', 'wick', 'wire', 'wore', 'year', 'zone',
'unit', 'vent', 'void', 'warm', 'went', 'wide', 'wiry', 'work', 'yell', 'zoo',
'upon', 'very', 'vote', 'warn', 'were', 'wifi', 'wise', 'worm', 'yelp',
]

# in the future, when we want to modify the list, add calls to
#   both the remove_words() and add_words() functions below -- this
#   will create a clear way to show the history of the wordlist
words = remove_words(words, [
'evil','lard','you','your',
])

words = sorted(words)


error_found = False

# remove non- 'a-z' characters... if any word does not end up empty, we have an error
valid_chars = set([
'a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z'])
for word in words:
	for char in word:
		if not char in valid_chars:
			error_found = True
			print(f"[{word}] contains one or more invalid characters")
			continue

if error_found:
	print("one or more words contain invalid characters")
	sys.exit(1)

# repeat the list a few times, alternating between lower and title case
new_words = []
capitalized = False
while len(new_words) < 7776:
	if capitalized:
		new_words = new_words + [x.title() for x in words]
	else:
		new_words = new_words + words
	capitalized = not capitalized

words = new_words[0:7776]

# create repeated list of 7,776 numbers/specials
num_specials = ['1','2','3','4','5','6','7','8','9','0','.','-','+',':','?','!','@','#','$','%','^','&','*','~']
new_num_specials = []
while len(new_num_specials) < 7776:
	new_num_specials = new_num_specials + num_specials
num_specials = new_num_specials[0:7776]


# zip the words and num/specials together
words = [f"{w}{ns}" for w,ns in zip(words, num_specials)]

if len(words) != 7776:
	print(f"7,776 words are required (have {len(words):,})")
	sys.exit(1)

# make sure there are no repeats, since we repeated the words and other chars before zipping them
test_set = set(words)
if len(test_set) != 7776:
	print(f"7,776 words are required (have {len(test_set):,} after checking for repeats)")
	sys.exit(1)

use_line_number_column = False
if 'use_line_number_column' in sys.argv:
	use_line_number_column = True

line_num = 0
for a in range(1, 7):
	for b in range(1, 7):
		for c in range(1, 7):
			for d in range(1, 7):
				for e in range(1, 7):
					line_num += 1
					if line_num >= len(words):
						continue
					if use_line_number_column:
						print("%4d\t%d%d%d%d%d\t%s" % (line_num, a, b, c, d, e, words[line_num-1]))
					else:
						print("%d%d%d%d%d\t%s" % (a, b, c, d, e, words[line_num-1]))
