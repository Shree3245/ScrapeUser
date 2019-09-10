from telethon import TelegramClient
from telethon.tl.functions.contacts import ResolveUsernameRequest, GetAdminLogRequest, GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch,InputChannel,ChannelAdminLogEventsFilter,InputUserSelf,InputUser,PeerUser, PeerChat, PeerChannel
from telethon.tl.functions.channels import InviteToChannelRequest, GetParticipantsRequest,GetFullChannelRequest
import time
import codecs
import re

api_id = '1123'     #input your api id 
api_hash = '6b90b' #input your api hash

client = TelegramClient('name', api_id, api_hash) #give a name for the session to open with 
client.start()


tt=open("new.txt", "a+")
queryKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all_participants = []
channel = str(input("Link to the group: "))
all_participants=[]
for key in queryKey:
    offset = 0
    limit = 1000
    while True:
        participants = client(GetParticipantsRequest(
            channel, ChannelParticipantsSearch(key), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        for user in participants.users:
            try:
                if re.findall(r"\b[a-zA-Z]", user.first_name)[0].lower() == key:
                    all_participants.append(user)
                    print(user.username)
                    print(len(all_participants))
                    if "None" not in user.username:
                        tt.write(user.username)
                        tt.write(",")
                    
            except:
                pass

        offset += len(participants.users)
    


    
