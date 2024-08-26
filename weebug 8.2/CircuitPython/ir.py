import pulseio
import adafruit_irremote
import asyncio


BUTTONS = {
    (255, 0, 93, 162): "power",
    (255, 0, 29, 226): "menu",
    (255, 0, 221, 34): "test",
    (255, 0, 253, 2): "plus",
    (255, 0, 61, 194): "back",
    (255, 0, 31, 224): "rewind",
    (255, 0, 87, 168): "play",
    (255, 0, 111, 144): "forward",
    (255, 0, 151, 104): "0",
    (255, 0, 103, 152): "minus",
    (255, 0, 79, 176): "c",
    (255, 0, 207, 48): "1",
    (255, 0, 231, 24): "2",
    (255, 0, 133, 122): "3",
    (255, 0, 239, 16): "4",
    (255, 0, 199, 56): "5",
    (255, 0, 165, 90): "6",
    (255, 0, 189, 66): "7",
    (255, 0, 181, 74): "8",
    (255, 0, 173, 82): "9",
}


async def ir_remote(pin, obj):
    pulsein = pulseio.PulseIn(pin, maxlen=120, idle_state=True)
    decoder = adafruit_irremote.NonblockingGenericDecode(pulsein)

    while True:
        for message in decoder.read():
            if isinstance(message, adafruit_irremote.IRMessage):
                obj.command = BUTTONS.get(message.code)
                print(obj.command)
        await asyncio.sleep(0.1)

