from Controller.Tools.PrintContent import PrintContent
from Controller.Codec.BinaryCodec import BinaryCodec
from Controller.Codec.HexadecimalCodec import HexadecimalCodec
from Controller.Codec.FutureCodec import FutureCodec

class Controller:
    def tools(path):
        return PrintContent(path).execute()

    def codec(function):
        codec = {
            'dec_to_bin': BinaryCodec.dec_to_bin,
            'bin_to_dec': BinaryCodec.bin_to_dec,
            'dec_to_hex': HexadecimalCodec.dec_to_hex,
            'hex_to_dec': HexadecimalCodec.hex_to_dec,
            'future': FutureCodec.future_codec
        }

        return codec[function]()