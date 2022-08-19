from colors import color
import math

# Simple program to print three significant digits

# Below shows the scientific notation using {:e}

scientific_notation="{:e}".format(0.0000056578)
print(f"\n{scientific_notation}")

# And we can limit it to the significant digits by such

more_scientific_notation="{:.2e}".format(0.0000056578)
print(f"\n{more_scientific_notation}")

# Now on to some examples

item_1 = 101455348/1111419
item_1_formatted_string = "{:.3f}".format(item_1)
item_1_float_value = float(item_1_formatted_string)

print(color.AEG + "\nOriginal Result:" + color.AIF)
print(item_1)
print(color.AEG + "\nFormatted Result:" + color.AIF)
print(item_1_float_value)


item_2 = 0.000000612*0.00031119
item_2_formatted_string = "{:.2e}".format(item_2)
item_2_float_value = float(item_2_formatted_string)

print(color.AEG + "\nOriginal Result:" + color.AIF)
print(item_2)
print(color.AEG + "\nFormatted Result:" + color.AIF)
print(item_2_float_value)


item_3 = 297060/0.0004839

print(color.AEG + "\nOriginal Result:" + color.AIF)
print(item_3)
print(color.AEG + "\nFormatted Result:" + color.AIF)
item_3_scientific_notation = "{:.2e}".format(item_3)
print(item_3_scientific_notation)

# reset color
print(color.ENDC + "")