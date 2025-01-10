import time

def oven_baking_cycle():
    # Time duration for each stage (in seconds)
    preheating_duration = 8  # Preheating the oven
    baking_duration = 15     # Baking the food
    cooling_duration = 5     # Cooling down the oven

    while True:
        # Preheating
        print("Preheating the oven...")
        time.sleep(preheating_duration)
        print("Preheating completed!")
        time.sleep(1)  # Short transition before baking

        # Baking
        print("Baking in progress...")
        time.sleep(baking_duration)
        print("Baking completed! Enjoy your food.")
        time.sleep(1)  # Short transition before cooling

        # Cooling down
        print("Cooling down the oven...")
        time.sleep(cooling_duration)
        print("Oven is ready for the next use.")
        time.sleep(1)  # Short break before restarting the cycle

# Run the oven baking cycle
oven_baking_cycle()
