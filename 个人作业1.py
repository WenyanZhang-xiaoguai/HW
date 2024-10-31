def verify_cards(cards):
  card_colours={'red','blue','green','yellow'}
  card_count={}
  for card in cards:
    # -Each string in the list is correctly formatted;
    lower_card=card.lower()
    parts=lower_card.split(" ")
    if len(parts)!=2:
      return False
    colour=parts[0]
    number=int(parts[1])
   # Each card in the list has a valid colour and a valid number
    if colour not in card_colours:
      return False
    if number<1 or number>10:
      return False
   #No more than two cards of the same colour and number appear in the list
    card_continer=tuple(parts)
    if card_continer in card_count:
      card_count[card_continer] +=1
    else:
      card_count[card_continer]=1
    if card_count[card_continer]>2:
      return False
  return True