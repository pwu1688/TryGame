from gamePackage.playgame import TryGame

game = TryGame()
while True:
    user_input = input("> ")
    output = game.guess(user_input)
    print(output.get("message") + ", input_in_range = " + str(output.get("input_in_range")) + ", gen_number = " + str(output.get("gen_number")))
    if output.get("input_in_range") == 1 or output.get("count") > 4:
        break
