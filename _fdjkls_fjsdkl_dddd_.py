












# 补充零到指定长度（补齐到16位，即2^4）
def pad_to_16_bits(bin_value):
    return bin_value.zfill(16)

# 二进制字符串分割并转化为汉字
def split_and_convert_to_char(bin_value, bit_length):
    # 根据bit_length分割二进制
    part_length = bit_length  # 这里是16位，2^4位
    parts = [bin_value[i:i+part_length] for i in range(0, len(bin_value), part_length)]
    
    # 确保每部分都有足够的位数
    parts_padded = [pad_to_16_bits(part) for part in parts]

    # 转换为十六进制
    hex_values = [hex(int(part, 2))[2:].upper() for part in parts_padded]

    # 转换为汉字
    chars = [chr(int(hex_val, 16)) for hex_val in hex_values]
    
    return hex_values, chars


## 示例二进制数据
#bin_value = '011011111101110101111010110110111011'

bin_value_=" 111110001110011 101100001010100 101111110001000 101001111101111 111001000110001 "





# 进行操作并输出结果
bit_length = 16  # 每部分16位，即2^4
hex_values, chars = split_and_convert_to_char(bin_value_, bit_length)

# 输出结果
for i in range(len(hex_values)):
    print(f"分割后的十六进制：{hex_values[i]}")
    print(f"对应的汉字：{chars[i]}")
