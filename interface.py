class Displayer:
    @staticmethod
    def renderLoginForm():
        print('\n    --- Welcome to the ticket shop! ---\n')
        name = input(' -> Step 1/2: Please tell us your name: ')
        cpf = input(' -> Step 1/2: And now your cpf: ')
        return {
            'name': name,
            'cpf': cpf
        }

    @staticmethod
    def getUserOption():
        MAIN_MENU =  '''
--- What do you want to do? ---
  -1 Show movies 🎬
  -2 Buy ticket 🎫
  -3 List my purchases 🛍️
  -4 Exit 🚪

-> '''
        return input(MAIN_MENU)

    @staticmethod
    def renderExitMessage():
        print("\nLater! :)\n")

    @staticmethod
    def listMovies(movies: list):
        for movie in movies:
            print(f'''
    --- {movie.name} ---
      -> ID:      {movie.id}
      -> Type:    {movie.TYPE}
      -> Generes: {movie.generes}
      -> Rating:  {movie.getRating()}/10 🌟
      -> Price:   $ {movie.price}
''')

    @staticmethod
    def renderTicketPurchaseProcess() -> dict:
        print("\n--- Buying Ticket 💰 ---")

        movieId    = input('  -> Movie id: ')
        cinemaName = input('  -> Cinema name: ')
        roomCode   = input('  -> Room code: ')
        seatNumber = input('  -> Seat number: ')
        return {
            'movieId': movieId,
            'cinemaName': cinemaName,
            'roomCode': roomCode,
            'seatNumber': seatNumber
        }

    @staticmethod
    def renderSuccessfullyPurchased():
        print('\n--- Ticket successfully purchased! ✅ ---\n')

    @staticmethod
    def renderPurchaseList(purchases: list):
        print('\n--- Your Purchases 🛍️ ---\n')
        for purchase in purchases:
            print(f' - Items:\n')
            for ticket in purchase.getItems():
                print(f'    - Ticket: {ticket.movie.name}\n')
                print(f'    - Price:  $ {ticket.getPrice()}\n')

