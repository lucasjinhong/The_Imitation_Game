from Controller.Tools.PrintContent import PrintContent
from Controller.Codec.Level1Codec import Level1Codec
from Controller.Codec.Level2Codec import Level2Codec

class Controller:
    def tools(path):
        return PrintContent(path).execute()

    def codec(function, last_answer=''):
        codec = {
            'dec_to_bin': Level1Codec.dec_to_bin,
            'bin_to_dec': Level1Codec.bin_to_dec,
            'dec_to_hex': Level1Codec.dec_to_hex,
            'hex_to_dec': Level1Codec.hex_to_dec,
            'future': Level1Codec.future_codec,
            'nor_to_not': Level2Codec.nor_to_not,
            'nor_and_not': Level2Codec.nor_and_not,
            'nor_or_and': Level2Codec.nor_or_and,
            'nor_xor_or': Level2Codec.nor_xor_or,
            'hex_to_bin': Level2Codec.hex_to_bin,
            'all_in_one': Level2Codec.all_in_one
        }

        return codec[function](last_answer)