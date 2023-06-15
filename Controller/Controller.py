from Controller.Tools.PrintContent import PrintContent
from Controller.Codec.Level1Codec import Level1Codec
from Controller.Codec.Level2Codec import Level2Codec
from Controller.Codec.Level3Codec import Level3Codec

class Controller:
    def tools(path):
        return PrintContent(path).execute()

    def codec(level, function, question=None):
        select = {
            '1': Level1Codec().codec_handler,
            '2': Level2Codec().codec_handler,
            '3': Level3Codec().codec_handler
        }

        if question is None:
            question = []

        print(question)
        ans = select[level](function, question)
        print(ans)
        return ans