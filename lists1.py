the_hunt = []
the_hunt.append('Anjanath')
the_hunt.append('Rathalos')
the_hunt.append('Shagaru-Magala')
the_hunt.append('Fatalis')
the_hunt.append('Seregios')
the_hunt.append('Safi\'jiiva')

index = 0

# Here is my WHILE loop
# It has a start at index, and finishes at the end of the list.
print("\v----WHILE LOOP----")
while index < len(the_hunt):
    print(the_hunt[index])
    index = index + 1

# Here is a FOR loop
print("\v----FOR LOOP----")
for monster in the_hunt:
    print(monster + '\v')
