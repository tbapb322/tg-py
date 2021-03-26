import datanews
from telegram.ext import Updater, CommandHandler

DOLLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk01NWm6viYijAo3HXYOEQUyDEDtFEw%3A1584716087546&source=hp&ei=N9l0XtDXHs716QTcuaXoAg&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+&gs_l=psy-ab.3.0.35i39i70i258j0i131l4j0j0i131l4.3044.4178..5294...1.0..0.83.544.7......0....1..gws-wiz.......35i39.5QL6Ev1Kfk4'

datanews.api_key = "0egfn0xoypf2i6kuypz9chk3c"
USAGE = '/greet <name> - Greet me!'
updater = Updater("1735011861:AAE7QTdbPfuG2AF-EZtYIszqc17hdNFtUHI", use_context=True)


def start(update, context):
    update.message.reply_text(USAGE)


def greet_command(update, context):
    update.message.reply_text(f'Hello {context.args[0]}!')


def search_command(update, context):
    def fetcher(query):
        return datanews.headlines(query, size=10, sortBy='date', page=0, language='en')
    _fetch_data(update, context, fetcher)


def _fetch_data(update, context, fetcher):
    if not context.args:
        update.message.reply_text('No news is good news')
        return

    query = '"' + ' '.join(context.args) + '"'
    result = fetcher(query)

    if not result['hits']:
        update.message.reply_text('No news is good news')
        return

    last_message = update.message
    for article in reversed(result['hits']):
        text = article['title'] + ': ' + article['url']
        last_message = last_message.reply_text(text)


def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("greet", greet_command))
    dp.add_handler(CommandHandler("search", search_command))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
