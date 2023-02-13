import base64

L337_H4X = b'aHR0cHM6Ly9ycHdkbC5lemRyb3dpZS5nb3YucGwvUlBaL0RldGFpbHNDb25maXJtP3JlZ2lzdHJ5\nTnVtYmVyPXt1aWR9\n'

URL_BASE = base64.decodebytes(L337_H4X).decode("ascii")

UID_LENGTH = 12

OUTPUT_DIR = "results"

MAX_UID = 250000
