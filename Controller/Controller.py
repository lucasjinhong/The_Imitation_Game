from Controller.Tools.PrintContent import PrintContent
from Controller.Codec.Level1Codec import Level1Codec
from Controller.Codec.Level2Codec import Level2Codec

class Controller:
    def tools(path):
        return PrintContent(path).execute()

    def codec(level, function, answer_last=''):
        select = {
            '1': Level1Codec().codec_handler,
            '2': Level2Codec().codec_handler
        }

        return select[level](function, answer_last)