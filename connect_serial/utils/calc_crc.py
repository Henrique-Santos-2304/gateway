def crc(buffer, tamanho):
    bitbang = 0
    crc_calc = 0xC181
    for x in range(0, tamanho):
        crc_calc^= buffer[x] & 0x00FF
        for j in range(0,8):
            bitbang=crc_calc
            crc_calc>>=1
            if int(bitbang) & 1:
                crc_calc^=0xA001
    return crc_calc