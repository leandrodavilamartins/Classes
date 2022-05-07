class ClubCard:
    def __init__(self,valor,naipe="Club"):
        self.valor = valor
        self.naipe = naipe
    
class DiamondCard:
    def __init__(self,valor,naipe="Diamond"):
        self.valor = valor
        self.naipe = naipe

class HeartCard:
    def __init__(self,valor,naipe="Heart"):
        self.valor = valor
        self.naipe = naipe

class SpadeCard:
    def __init__(self,valor,naipe="Spade"):
        self.valor = valor
        self.naipe = naipe


valor = [1,2,3,4,5,6,7,8,9,10]

cards = []

for v in valor:
    clubcard = ClubCard(v)
    diamondcard = DiamondCard(v)
    heartcard = HeartCard(v)
    spadecard = SpadeCard(v)
    cards.append(clubcard,diamondcard,heartcard,spadecard)