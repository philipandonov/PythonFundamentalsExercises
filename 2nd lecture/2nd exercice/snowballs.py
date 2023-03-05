number_of_snowballs = int(input())
max_weight_of_the_ball = 0
max_time_of_the_ball = 0
max_quality_of_the_ball = 0
max_snowball_value = 0
for snowball in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    snowball_value = (current_weight / current_time) ** current_quality
    if snowball_value > max_snowball_value:
        max_quality_of_the_ball = current_quality
        max_weight_of_the_ball = current_weight
        max_time_of_the_ball = current_time
        max_snowball_value = snowball_value
print(f"{max_weight_of_the_ball} : {max_time_of_the_ball} = {int(max_snowball_value)} ({max_quality_of_the_ball})")

