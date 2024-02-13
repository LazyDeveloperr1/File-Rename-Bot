from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup 
from config import ADMIN
 

@Client.on_message(filters.command("start") & filters.private)                             
async def start_cmd(bot, msg):
    txt="This is personal use bot 🙏. Do you want your own bot? 👇 Click the source code to deploy"
    btn = InlineKeyboardMarkup([[
        InlineKeyboardButton("🛠️ Hᴇʟᴩ", url="https://t.me/+U84WCV9bRV44NTRl")
        ],[
        InlineKeyboardButton("🎛️ Aʙᴏᴜᴛ", url="https://youtu.be/oc847WvOUaI")
    ]])
    if msg.from_user.id != ADMIN:
        return await msg.reply_text(text=txt, reply_markup=btn, disable_web_page_preview = True)
    await start(bot, msg, cb=False)


@Client.on_callback_query(filters.regex("start"))
async def start(bot, msg, cb=True):   
    txt=f"ʜᴇʟʟᴏ {msg.from_user.mention} ◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ 4GB Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ◈ I Cᴀɴ Rᴇɴᴀᴍᴇ Fɪʟᴇs, Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟs, Cᴏɴᴠᴇʀᴛ Bᴇᴛᴡᴇᴇɴ Vɪᴅᴇᴏ Aɴᴅ Fɪʟᴇ, Aɴᴅ Sᴜᴘᴘᴏʀᴛ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟs Aɴᴅ Cᴀᴘᴛɪᴏɴs <b><a href=https://github.com/LazyDeveloperr1>LazyDeveloperr1</a></b>"                                     
    button= [[
        InlineKeyboardButton("🤖 Bot Updates", url="https://t.me/+U84WCV9bRV44NTRl")
        ],[
        InlineKeyboardButton("🎛️ Aʙᴏᴜᴛ", callback_data="about"),
        InlineKeyboardButton("🛠️ Hᴇʟᴩ", callback_data="help") 
    ]]  
    if cb:
        await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)
    else:
        await msg.reply_text(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("help"))
async def help(bot, msg):
    txt = "just send a file and /rename <new name> with replayed your file\n\n"
    txt += "send photo to set thumbnail automatic \n"
    txt += "/view to see your thumbnail \n"
    txt += "/del to delete your thumbnail"
    button= [[        
        InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data="del"),
        InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True)


@Client.on_callback_query(filters.regex("about"))
async def about(bot, msg):
    me=await bot.get_me()
    Master=f"<a href=https://t.me/Mo_Tech_YT>MoTech</a> & <a href=https://t.me/venombotupdates>MhdRzn</a>"  
    Source="<a href=https://github.com/MrMKN/Simple-Rename-Bot>Click Here</a>"
    txt=f"<b>Bot Name: {me.mention}\nDeveloper: <a href=https://github.com/MrMKN>MrMKN</a>\nBot Updates: <a href=https://t.me/mkn_bots_updates>Mᴋɴ Bᴏᴛᴢ™</a>\nMy Master's: {Master}\nSource Code: {Source}</b>"                 
    button= [[        
        InlineKeyboardButton("🔒 Cʟᴏꜱᴇ", callback_data="del"),
        InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data="start") 
    ]]  
    await msg.message.edit(text=txt, reply_markup=InlineKeyboardMarkup(button), disable_web_page_preview = True, parse_mode=enums.ParseMode.HTML)


@Client.on_callback_query(filters.regex("del"))
async def closed(bot, msg):
    try:
        await msg.message.delete()
    except:
        return


