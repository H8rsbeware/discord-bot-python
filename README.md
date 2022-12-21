## discord-bot-python

###DEPRECIATED LIBRARY FOR DISCORD INTERACTION

a discord bot build on discord.py

#### commands

- kick, k, boot (member, reason) : kicks users, returns embed with reason
- clear, purge, c, p (amount) : clears amount of messages
- ban, b (member, reason) : bans user, returns embed with reason
- tempban, tempBan, tb (member, time (durationConverter), reason) : bans user for set time, returns embed with reason
- unban, ub (userid) : unbans user
- mute, m (member, reason) : prevents a user from messaging, returns embed with reason
- tempmute, tempMute, tm (member, time (durationConverter), reason) : prevent a user from speaking till the time elapses, returns embed with reason
- unmute, um (member) : unmutes user
- prefix, Prefix, pfx (prefix) : changes servers prefix and saves to json file
- user-info, user, info (member) : returns user information

- help (command) : returns info on commands

- 8ball, 8 (question) : returns random response
- avatar, av (member = author) : returns users profile picture

- status cycler () : cycles through discord cycles - cant be called
