# virtualgym_bot
Bot for automatic Gym bookings at virtuagym

**Usage:**
Based on cron scheduler, this script starts execution. I use 5 min intervals betwen runs.

1. Script checks the schedule for the next day
2. Finds available slots based on pre-defined conditions
3. Makes an appointment
4. Shares appointment info via Telegram
