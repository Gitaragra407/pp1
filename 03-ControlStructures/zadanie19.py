dog_age_in_human_years = float(input("Give the age of your dog in human years "))
dog_age_in_dog_years = 0.0
if dog_age_in_human_years > 2:
    dog_age_in_human_years -=2
    dog_age_in_dog_years = dog_age_in_human_years * 4
    dog_age_in_dog_years += 21
else:
    dog_age_in_dog_years = dog_age_in_human_years * 10.5
print("Your dog's age in dog years: ",dog_age_in_dog_years)
