from fontTools.ttLib import TTFont

#Open Sans
input_file_opensans = "./fonts/OpenSans-VariableFont_wdth,wght.ttf"
font_opensans = TTFont(input_file_opensans)

output_file_woff_opensans = "./fonts/OpenSans-VariableFont_wdth,wght.woff"
font_opensans.flavor = 'woff'
font_opensans.save(output_file_woff_opensans)

output_file_woff2_opensans = "./fonts/OpenSans-VariableFont_wdth,wght.woff2"
font_opensans.flavor = 'woff2'
font_opensans.save(output_file_woff2_opensans)

#Poppins
input_file_poppins = "./fonts/Poppins-VariableFont_wght.ttf"
font_poppins = TTFont(input_file_poppins)

output_file_woff_poppins = "./fonts/Poppins-VariableFont_wght.woff"
font_poppins.flavor = 'woff'
font_poppins.save(output_file_woff_poppins)

output_file_woff2_poppins = "./fonts/Poppins-VariableFont_wght.woff2"
font_poppins.flavor = 'woff2'
font_poppins.save(output_file_woff2_poppins)

print("Fonts converted successfully!")
