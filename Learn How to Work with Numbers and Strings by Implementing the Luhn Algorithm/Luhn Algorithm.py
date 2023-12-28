def main():
    card_number = "4111-1111-4555-1142"
    translation_table = str.maketrans({"-": "", " ": ""})
    translated_card_number = card_number.translate(translation_table)
    return print(translated_card_number)

main()