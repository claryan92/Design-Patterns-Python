quote = (
    'O Captain! my Captain! our fearful trip is done,',
    'The ship has weather’d every rack, the prize we sought is won,',
    'The port is near, the bells I hear, the people all exulting,',
    'While follow eyes the steady keel, the vessel grim and daring;',
    'But O heart! heart! heart!',
    'O the bleeding drops of red,',
    'Where on the deck my Captain lies,',
    'Fallen cold and dead…',
)

class QuoteModel:
    def get_quote(self, n):
        try:
            value = quote[n]
        except IndexError as err:
            value = 'Not found!'
        return value

class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: "{quote}"')

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input('Which quote number would you like to see? ')

class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError as err:
                self.view.error(f"Incorrect index '{n}'")
        quote = self.model.get_quote(n)
        self.view.show(quote)

def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()