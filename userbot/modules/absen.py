from time import sleep

from userbot import CMD_HANDLER as cmd

from userbot import CMD_HELP

from userbot.utils import edit_or_reply, yan_cmd

@yan_cmd(pattern="aa(?: |$)(.*)")

async def _(event):

    await event.client.send_message(

        event.chat_id,

        "**Hadir bang**",

        reply_to=event.reply_to_msg_id,

    )

    await event.delete()

@yan_cmd(pattern="ab(?: |$)(.*)")

async def _(event):

    await event.client.send_message(

        event.chat_id,

        "**Hallo semuanya sory baru nimbrung**",

        reply_to=event.reply_to_msg_id,

    )

    await event.delete()

@yan_cmd(pattern="ba(?: |$)(.*)")

async def _(event):

    await event.client.send_message(

        event.chat_id,
        f"**Haii Salken Saya {me.first_name} . Buat semuanya rajin-rajin ya nimbrung disini**")

        reply_to=event.reply_to_msg_id,
    
    )

    await event.delete()

@yan_cmd(pattern="bc(?: |$)(.*)")

async def _(event):

    await event.client.send_message(

        event.chat_id, "**hallo semuanya gw hadir kembali*", reply_to=event.reply_to_msg_id

    )

    await event.delete()

@yan_cmd(pattern="yn(?: |$)(.*)")

async def _(event):

    me = await event.client.get_me()

    xx = await edit_or_reply(event, f"**Haii Salken Saya {me.first_name}**")

    sleep(2)

    await xx.edit("**Assalamualaikum**")

@yan_cmd(pattern="ny(?: |$)(.*)")

async def _(event):

    xx = await edit_or_reply(event, "**WOYY ADMIN**")

    sleep(3)

    await xx.edit("**NIMBRUNG GOBLOKK!!!🔥**")

@yan_cmd(pattern="iy(?: |$)(.*)")

async def _(event):

    me = await event.client.get_me()

    xx = await edit_or_reply(event, f"**Hallo KIMAAKK SAYA {me.first_name}**")

    sleep(2)

    await xx.edit("**LU SEMUA NGENTOT 🔥**")

@yan_cmd(pattern="iyan(?: |$)(.*)")

async def _(event):

    xx = await edit_or_reply(event, "**Hai cewek cantik*")

    sleep(2)

    await xx.edit("**pc yuk pc**")

CMD_HELP.update(

    {

        "absen": f"**Plugin : **`absen`\

        \n\n  •  **Syntax :** `{cmd}ab`\

        \n  •  **Function : **Hallo semuanya sory baru nimbrung\

        \n\n  •  **Syntax :** `{cmd}aa`\

        \n  •  **Function : **Hadir bang\

        \n\n  •  **Syntax :** `{cmd}l`\

        \n  •  **Function : **Untuk Menjawab salam\

        \n\n  •  **Syntax :** `{cmd}ass`\

        \n  •  **Function : **Salam Bahas arab\

        \n\n  •  **Syntax :** `{cmd}semangat`\

        \n  •  **Function : **Memberikan Semangat.\

        \n\n  •  **Syntax :** `{cmd}ywc`\

        \n  •  **Function : **nMenampilkan Sama sama\

        \n\n  •  **Syntax :** `{cmd}sayang`\

        \n  •  **Function : **Kata I Love You.\

        \n\n  •  **Syntax :** `{cmd}k`\

        \n  •  **Function : **LU SEMUA NGENTOT 🔥\

        \n\n  •  **Syntax :** `{cmd}j`\

        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\

    "

    }

)

Footer

© 2023 GitHub, Inc.

Footer navigation

