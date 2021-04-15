# Steal
{
    "output_file": "config.json",

    "liveOnly": {
        "type": "checkbox",
        "value": true,
        "label": "Live Only Mode",
        "tooltip": "True if you want it to only run when you are live",
        "group" : "General"
    },
    "command": {
        "type": "textbox",
        "value": "!steal",
        "label": "Command",
        "tooltip": "Name of the command",
        "group": "General"
    },
    "permission": {
        "type": "dropdown",
        "value": "Everyone",
        "items": ["Everyone","Regular","Subscriber","Moderator","Editor"],
        "label": "Permission level",
        "tooltip": "Set the permission level for the command",
        "group": "General"
    },
    "costs": {
        "type": "numberbox",
        "value": 5,
        "label": "Cost to play the game",
        "tooltip": "Set the default cost for this command.",
        "group": "General"
    },
    "minReward": {
        "type": "numberbox",
        "value": 10,
        "label": "Min reward",
        "tooltip": "Minimum ammount of points that the user can steal",
        "group" : "General"
    },
    "maxReward": {
        "type": "numberbox",
        "value": 20,
        "label": "Max reward",
        "tooltip": "Maximum ammount of points that the user can steal",
        "group" : "General"
    },
    "useCooldown": {
        "type": "checkbox",
        "value": true,
        "label": "Use Cooldowns",
        "tooltip": "Enable/Disable cooldown and user cooldown",
        "group": "Cooldown"
    },
    "useCooldownMessages": {
        "type": "checkbox",
        "value": true,
        "label": "Use Cooldown Messages",
        "tooltip": "Enable/Disable cooldown messages",
        "group": "Cooldown"
    },
    "cooldown": {
        "type": "numberbox",
        "label": "Cooldown (seconds)",
        "value": 1,
        "tooltip": "Cooldown in seconds.",
        "group": "Cooldown"
    },
    "onCooldown": {
        "type": "textbox",
        "value": "$user, $command is still on cooldown for $cd minutes!",
        "label": "Cooldown Response",
        "tooltip": "The message that the bot will display when the command is on cooldown. \r\n $user = Username \r\n $cd = Time remaining \r\n $command = Command name",
        "group": "Cooldown"
    },
    "userCooldown": {
        "type": "numberbox",
        "label": "User Cooldown (seconds)",
        "value": 120,
        "tooltip": "User cooldown in seconds.",
        "group": "Cooldown"
    },
    "onUserCooldown": {
        "type": "textbox",
        "value": "$user, $command is still on user cooldown for $cd minutes!",
        "label": "User Cooldown Response",
        "tooltip": "The message that the bot will display when the command is on user cooldown. \r\n $user = Username \r\n $cd = Time remaining \r\n $command = Command name",
        "group": "Cooldown"
    },
    "responseWon": {
        "type": "textbox",
        "value": "$user stole $reward $currency from $victim",
        "label": "User wins message",
        "tooltip": "Message that will be posted if the user wins.\r\n $user = Username\r\n $points = Current user points\r\n $currency = Name of Currency\r\n $reward = Winning reward",
        "group": "Response Messages"
    },
    "responseLost": {
        "type": "textbox",
        "value": "$user couldn't steal any $currency from $victim and lost $reward $currency",
        "label": "User looses message",
        "tooltip": "Message that will be posted if the user loose.\r\n $user = Username\r\n $points = Current user points\r\n $currency = Name of Currency ",
        "group": "Response Messages"
    },
    "responseNotEnoughPoints": {
        "type": "textbox",
        "value": "$user you $cost $currency to steal.",
        "label": "Not enough points",
        "tooltip": "Message that will be posted if the user doesn't have enough points.\r\n $user = Username\r\n $currency = Name of Currency\n $cost = Cost to play\r\n $minReward = Min reward\r\n $maxReward = Max reward",
        "group": "Response Messages"
    },
    "openReadMe": {
        "type": "button",
        "label": "Open 'Readme Me' file",
        "tooltip": "Opens the 'Readme.txt' for this script.",
        "function": "OpenReadMe",
        "wsevent": "",
        "group": ""
    }
}
© 2021 GitHub, Inc.
