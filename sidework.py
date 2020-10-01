name1 = input("What is the name that you want to test? ")
fatlevel1 = int(input("On a scale of 1 - 10 how fat is this guy? "))

if (fatlevel1 > 10):
    print("That is too fat, use a scale of 1 - 10.")
else:
    def sped_detec(name1, fat_level1):
        if int(fat_level1) == 10:
            return "Ding... Ding... Ding... Sped Level MAX"
            
        elif fat_level1 == 9:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

        elif fat_level1 == 8:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

        elif fat_level1 == 7:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

        elif fat_level1 == 6:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

        elif fat_level1 == 5:
            return name1 + " Sped on level " + str(fat_level1) + "/10"
        
        elif fat_level1 == 4:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

        elif fat_level1 == 3:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

        elif fat_level1 == 2:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

        elif fat_level1 == 1:
            return name1 + " Sped on level " + str(fat_level1) + "/10"

       

    sped_level = sped_detec(name1, fatlevel1)

    print(sped_level)