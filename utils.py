def int_to_state(self, valid_int):
    byte_state = []
    s_val = right_shift(self.block_size, 4)
    cell_size = bin2dec("1" * s_val)
    row_size = s_val * 4
    for x in range(4):
        shift_limit = self.block_size - row_size
        shift_val = shift_limit - (row_size * x)
        word = (valid_int >> shift_val) & (2 ** row_size - 1)
        line_array = []
        for y in range(4):
            line_array.append(word >> ((row_size - s_val) - (y * s_val)) & cell_size)
        byte_state.append(line_array)
    return byte_state


def state_to_int(self, byte_array_state):
    state_int = 0
    s_val = right_shift(self.block_size, 4)
    for row in byte_array_state:
        for cell in row:
            state_int <<= s_val
            state_int += cell
    return state_int


def bin2dec(bin):
    """
    Convert binary to decimal.
    """
    bin = str(bin)
    return int(bin, 2)


def AND(x, y):
    return x & y


def xor(x, y):
    return x ^ y


def right_shift(x, y):
    return x >> y


def left_shift(x, y):
    return x << y


def floor(a, b):
    return a // b
