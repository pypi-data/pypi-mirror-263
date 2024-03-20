from .groq import GROQ

from json import dumps

bot = GROQ('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')

resp = bot.ask('hello')

print(dumps(resp, indent=4))