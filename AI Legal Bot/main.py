import sys
from typing import Final, Union

import numpy as np
from tabulate import tabulate
import pandas as pd
from pandas import DataFrame
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

import m2

if m2.response.status_code != 200:
    sys.exit()
token: Final = '6520700450:AAFytpeKhZG1fRS4GvA5LevhaLl6juKmMRY'
bot_username: Final = '@legal_aid777_bot'


# basics
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I am a Indian Legal Rights and Resources Bot. Please type in the number"
                                    "whose category you want legal information about. The numbers are listed below for "
                                    "information  about that field: - \n"
                                    "1 -  Education in Hindi\n"
                                    "2 -  Education in English\n"
                                    "3 -  Housing in Hindi\n"
                                    "4 -  Housing in English\n"
                                    "5 -  Property Laws in Hindi\n"
                                    "6 -  Property Laws in English\n"
                                    "7 -  Intellectual Property in Hindi\n"
                                    "8 -  Intellectual Property in English\n"
                                    "9 -  Ownership in Hindi\n"
                                    "10 - Ownership in English\n"
                                    "11 - Company Laws in Hindi\n"
                                    "12 - Company Laws in English\n"
                                    "13 - Animal Laws in Hindi\n"
                                    "14 - Animal Laws in English\n"
                                    "\n"
                                    "\n"
                                    "नमस्ते! मैं एक भारतीय कानूनी अधिकार और संसाधन बॉट हूं। कृपया नंबर टाइप करें"
                                    "आप किस श्रेणी के बारे में कानूनी जानकारी चाहते हैं। इसके लिए नंबर नीचे सूचीबद्ध "
                                    "हैं"
                                    "उस फ़ील्ड के बारे में जानकारी: - \n"
                                    "1 - हिंदी में शिक्षा\n"
                                    "2 - अंग्रेजी में शिक्षा\n"
                                    "3 - हिंदी/अंग्रेजी में आवास\n"
                                    "4 - अंग्रेजी में आवास\n"
                                    "5 - संपत्ति कानून हिंदी में\n"
                                    "6 - संपत्ति कानून अंग्रेजी में\n"
                                    "7 - बौद्धिक संपदा हिंदी में\n"
                                    "8 - अंग्रेजी में बौद्धिक संपदा\n"
                                    "9 - स्वामित्व हिंदी में\n"
                                    "10 - स्वामित्व अंग्रेजी में\n"
                                    "11 - कंपनी कानून हिंदी में\n"
                                    "12 - कंपनी कानून अंग्रेजी में\n"
                                    "13 - पशु कानून हिंदी में\n"
                                    "14 - अंग्रेजी में पशु कानून")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Please type something so that I can respond")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command")


# responses


def handle_responses(text: str) -> Union[str, DataFrame]:
    pro: str = text.lower()
    if pro == '1':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Education_Hindi.csv'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsEducation_Hindi.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '2':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Education_English.csv'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsEducation_English.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '3':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Housing_Hindi.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsHousing_Hindi.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '4':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Housing_English.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsHousing_English.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '5':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Property_Hindi.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsProperty_Hindi.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '6':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Property_English.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsProperty_English.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '7':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Intellectual Property_Hindi.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsIntellectual Property_Hindi.xlsx').to_csv(path,
                                                                                                               index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '8':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Intellectual Property_English.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsIntellectual Property_English.xlsx').to_csv(path,
                                                                                                                 index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '9':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Ownership_Hindi.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsOwnership_Hindi.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '10':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Ownership_English.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsOwnership_English.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '11':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Company Laws_Hindi.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsCompany Laws_Hindi.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '12':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Company Laws_English.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsCompany Laws_English.xlsx').to_csv(path,
                                                                                                        index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        return table

    elif pro == '13':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Animal Laws_Hindi.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsAnimals_Hindi.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        table.replace('nan', ' ')
        return table

    elif pro == '14':
        path = 'D:\\AI Therapy Bot\\Legal_CSV\\Animal Laws_English.txt'
        file = pd.read_excel('D:\\AI Therapy Bot\\Legal\\Legal RightsAnimals_English.xlsx').to_csv(path, index=False)
        dataset = pd.read_csv(path, index_col=False)
        table = tabulate(dataset, showindex=False)
        table.replace('nan', ' ')
        return table

    return "I do not understand what you are trying to say....Please enter one of the numbers for the given categories."


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if bot_username in text:
            new_text: str = text.replace(bot_username, '').strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')


if __name__ == '__main__':
    print('Starting bot....')
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling....')
    app.run_polling(poll_interval=3)
