def trasnform_data_to_ordinal(intention: str) -> list:
    msg = list(map(ord, intention))
    ordinals = list(filter(lambda x: x != 32, msg))
    return ordinals

def of_byte_return_int(byt: str):
    for x in range(0, 50):
        num_byte = x.to_bytes(1, 'big')
        by_to_string = str(num_byte).replace("\\", "")
        new_byt_received = f"b'{byt}'"
        if new_byt_received == by_to_string: 
            return x
        
