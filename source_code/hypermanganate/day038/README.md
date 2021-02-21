
# DAY 38

Google Sheets and NLP API

# Description

Use a natural language API to detect exercises you've done today.
These exercises are automatically added to a workout tracking spreadsheet of your own.

# Environment
OS: Ubuntu Bionic

Python version: 3.8.7

# Dependencies

Requests 2

# How to run script

Get API details from NutritionIX and Sheety

Requires app.cfg:

```
{
    "app": {
        "api": {
            "nutritionix": {
                "api_key": "Your Key",
                "app_id": "Your App ID",
                "endpoint": "https://trackapi.nutritionix.com/v2/natural/exercise"
            },
            "sheety": {
                "api_key": "Your Key",
                "endpoint": "https://api.sheety.co/YOUR ENDPOINT"
            }
        }
    }
}
```

Call the script, and provide input

# Sample output
```
{
    "app": {
        "api": {
            "nutritionix": {
                "api_key": "eccfc7c8bcd026fe798f0dd891384e00",
                "app_id": "c53692c8",
                "endpoint": "https://trackapi.nutritionix.com/v2/natural/exercise"
            },
            "sheety": {
                "api_key": "jjXHkLCtWyTH7btY2Buz",
                "endpoint": "https://api.sheety.co/4265ac8fa5555f3f009b6520a022f5a2/myWorkouts/workouts"
            }
        }
    }
}
```

![Sample of App](https://raw.githubusercontent.com/Its-All-About-the-Journey/100daysofcode/hypermanganate/source_code/hypermanganate/day038/app.png)