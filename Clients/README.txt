THE GUI -

First things first, login with the account information you gave me (I set it up the exact way you gave the information to me).  The form should start off with the cursor in the username box, and one tab should go to the password box.  Once the password is entered, you can hit return (enter) key or click 'Login' to login.  The wrong information will result in a program termination, the correct information will close the Login tab and bring you to Bot Control.  Contact me with any problems with login.

!!!!IMPORTANT!!!!
Access to the port you are using (default is 8888) needs to be completely free.  That means you will need to forward that port on your router, and it also means you will need to make exceptions for that port in any and all firwalls.  Or to make sure the traffic is free, disable any and all firewalls, like me :P

One thing to note quickly, any misbehavior with Arxbot will be subject to a login termination.  I reserve the right to delete your login information from my login server, thereby cutting off access to any features.  But I'm sure we won't have any trouble, because we are of course only testing :)

I tried to make the main Control page as user friendly as possible.  The bottom text displaying "Awaiting Connections" is your 'output' text, it will display what Arxbot is doing, and help you in general.  The arguments box is self explanatory, that is where you will type arguments for the commands (i.e. for ddos you need to specify the ip to ddos, the port, and the length of time).  To easily understand what arguments go for which commands, simply type 'help' in the arguments box and click on any command.  The command will not run, but instead display what commands it needs to run properly.  Here are the arguments for all the commands:

Update List -
	No Arguments Needed

DDOS -
	<ip> <port> <time-in-seconds>

SynFlood -
	<ip> <port> <time-in-seconds>

Get -
	<url> <save-file-path> <1/0 run/justSave>

Update Bot -
	<url> <save-file-path>

Run -
	<file-path-to-run>

Vaccinate -
	No Arguments Needed

Info -
	No Arguments Needed

Some further explanations of some of the commands.  To clear up any confusion, the third argument for the 'Get' command is a 1 or 0 (zero), 1 is to run the file right after it is downloaded, and 0 is to just save the file.  Update bot is different than the 'Get' command because it not only downloads the new bot and runs it, it also terminates the current bot, so that all you're left with is the updated bot.  To vaccinate one bot at a time, select that one bot from the list, and Hit Vaccinate.  To vaccinate all bots at once, deselect all bots, and Hit Vaccinate.  To deselect all bots, simply Hit 'Update List'.  And finally, the 'Info' button changes all the bots display text to the computers name followed by it's operating system INSTEAD of the bot's IP address.

Things that definitely need to be tested:
-the 'Get' command
-the 'Update Bot' command
-different versions of Windows operating system
(currently only been tested on Windows 7)


THE SERVER (BIN) -

With every package of Arxbot, two versions of the server are included.  The one marked "HIDDEN" is the actual server, for spreading purposes.  The one marked "UNHIDDEN" will show the cmd window and will show output; this is for debugging purposses.

Currently adds itself to startup.  You can rename it to anything and run.  But once it has run, it will copy itself to System32 as name "GoogleUpdate0.exe" and that is what is added to startup.  Currrently you can find the running process in Processes as the name it is saved as.  In the future I plan on making it attach itself to another running process.  But you shouldn't have to worry about Processes because vaccinate terminates it anyway.

And although many of you will mention the largeness of the bin, you should consider a few things: 3.74 mb is not that large (might vary slightly), a normal home connection can download that in a matter of seconds, and I plan on slimming the bin size further with more research and vigorous testing.  So please don't let that discourage you completely.


That's all, thank for reading, and thanks for your interest in ArxBot.
Contact me on HF via a PM for questions/concerns/reviews/TV sessions/anything
Also contact me on MSN if you want:
runhacker@cia.gov

(No I'm not from the government :P)