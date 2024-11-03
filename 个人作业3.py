class CollectionOfCards:
    def __init__(self, card_strings):
        # Convert a list of strings into a collection of Card objects.
        self.collection = []
        for card in card_strings:
          card_list=card.split()
          colour=card_list[0]
          number=int(card_list[1])
          self.collection.append(Card(colour,number))
    def is_valid_group(self):
        # store different numbers with same colour in a dictionary
        same_colour = {}
        for card in self.collection:
            if card.colour not in same_colour:
                same_colour[card.colour] = []
            same_colour[card.colour].append(card.number)
        # Traverse the color groups,
        #check for the existence of a valid group with consecutive numbers of the same color
        for numbers in same_colour.values():
            numbers.sort()
            for i in range(len(numbers) - 2):
                if numbers[i] + 1 == numbers[i + 1] and numbers[i + 1] + 1 == numbers[i + 2]:
                    return True
        #  chcke a group in same number with different colour
        same_number = {}
        for card in self.collection:
            if card.number not in same_number:
                same_number[card.number] = set()
            same_number[card.number].add(card.colour)
        # travers the numbers group
        #check for the existence of a valid group with same numbers of different colour
        check=False  #check where there is a valid group
        for colours in same_number.values():
          if 0<len(colours)<3:
            return False
          if check==True:#the existence of a valid group
            return False
          if len(colours) >= 3:
            check=True
        if check==True:
          return True
        else:
          return False
        return False
    def find_valid_group(self):
        n = len(self.collection)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    group = [self.collection[i], self.collection[j], self.collection[k]]
                    # transfer into string
                    group_strs = []
                    for card in group:
                        group_strs.append(str(card))
                    collection = CollectionOfCards(group_strs)
                    if collection.is_valid_group():
                        return group
        return None
    def find_largest_valid_group(self):
     n = len(self.collection)
     max_group = None
    # "Create a dictionary same_number，
    #keys are the card numbers
    #the values are all the colors corresponding to that number
     same_number = {}
     for card in self.collection:
        if card.number not in same_number:
            same_number[card.number] = set()
        same_number[card.number].add(card.colour)
    # Traverse same_number
    #the same number of colors is greater than or equal to 3
    #create a new group of cards and update max_group
     for number, colours in same_number.items():
        if len(colours) >= 3:
            group = []
            for colour in colours:
                group.append(Card(colour, number))
            if max_group is None or len(group) > len(max_group):
                max_group = group
    #check same colour of consecutive numbers
     if max_group is None:
        for group_size in range(3, n + 1):
            for start in range(n):
                if start + group_size <= n:
                    #Extract a subset from self.collection
                    #using slicing to form the current group of cards
                    group = self.collection[start:start + group_size]
                    group_strs = []
                    for card in group:
                        group_strs.append(str(card))
                    collection = CollectionOfCards(group_strs)
                    if collection.is_valid_group():
                        if max_group is None or len(group) > len(max_group):
                            max_group = group
     result=[]
     for card in max_group:
        result.append(str(card))
     return result

def probability_of_valid_group(hands):
    # check first player have a valid group
    if hands[0].is_valid_group():
        return 1.0

    # collect all players hands cards
    held_cards = list()
    other_hands = list()
    hand = hands[0]
    for card in hand.collection:
        held_cards.append(str(card))
    for hand in hands[1:]:
        for card in hand.collection:
            other_hands.append(str(card))
    # sun_cards = list(),all players hands cards
    sun_cards = held_cards + other_hands
    # all cards
    total_cards = list()
    for colour in ['red', 'blue', 'green', 'yellow', 'red', 'blue', 'green', 'yellow']:
        for number in range(1, 11):
            total_cards.append(f'{colour} {number}')
    rest_cards = total_cards

    for i in sun_cards:
        # if j in total_cards:
        rest_cards.remove(i)


    # calculate first player have a valid group after get a card
    valid_group_count = 0
    for card_str in rest_cards:
    #temporarily store the first player's hand and the new card
        temp_collection_list = []
        for card in hands[0].collection:
            temp_collection_list.append(str(card))
        temp_collection_list.append(card_str)
        temp_collection = CollectionOfCards(temp_collection_list)
        if temp_collection.is_valid_group():
            valid_group_count += 1
    # calculate probility
    if rest_cards:
        return valid_group_count / len(rest_cards)
    else:
        return 0.0
