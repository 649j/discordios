# DiscordiOS 📱

Make your Discord bot appear as if it's running on a mobile device (iOS, Android, or Desktop).

## Features

- ✅ Emulate iOS, Android, or Desktop devices
- ✅ Simple and easy to use
- ✅ Built on top of discord.py
- ✅ Fully compatible with discord.py features

## Installation

### From GitHub
```bash
pip install git+https://github.com/649j/discordios.git
```

### Local Development
```bash
git clone https://github.com/649j/discordios.git
cd DiscordiOS
pip install -e .
```

## Quick Start

```python
import discord
from discordios import MobileClient, DeviceType

# Create a bot that appears as iOS
bot = MobileClient(
    device=DeviceType.IOS,
    intents=discord.Intents.default()
)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} is online!')
    print(f'📱 Device: {bot.device_name}')

bot.run('YOUR_TOKEN_HERE')
```

## Usage

### Device Types

You can use any of these device types:

```python
from discordios import DeviceType

# iOS Device
bot = MobileClient(device=DeviceType.IOS)

# Android Device
bot = MobileClient(device=DeviceType.ANDROID)

# Desktop (default discord.py)
bot = MobileClient(device=DeviceType.DESKTOP)
```

### Using Strings

You can also use strings instead of enums:

```python
bot = MobileClient(device='ios')
bot = MobileClient(device='android')
bot = MobileClient(device='desktop')
```

### Changing Device

You can change the device type at runtime:

```python
@bot.event
async def on_ready():
    print(f'Connected as: {bot.device_name}')
    
    # Change to Android
    bot.change_device('android')
    # Note: You need to reconnect for changes to take effect
```

### Properties

```python
# Get current device
print(bot.device)  # DeviceType.IOS

# Get device name
print(bot.device_name)  # "Discord iOS"
```

## Full Example

```python
import discord
from discordios import MobileClient, DeviceType

bot = MobileClient(device=DeviceType.IOS, intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'Bot: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print(f'Device: {bot.device_name}')
    print('━' * 40)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == '!ping':
        await message.channel.send('🏓 Pong!')
    
    elif message.content == '!device':
        await message.channel.send(f'📱 Running on: {bot.device_name}')
    
    elif message.content.startswith('!switch '):
        device = message.content.split(' ')[1].lower()
        try:
            bot.change_device(device)
            await message.channel.send(f'✅ Switched to {device}! (reconnect to apply)')
        except Exception as e:
            await message.channel.send(f'❌ Error: {e}')

bot.run('YOUR_TOKEN_HERE')
```

## How It Works

DiscordiOS works by overriding the Discord gateway connection properties to make Discord think your bot is connecting from a mobile device. This changes:

- The device icon shown in member lists (📱 instead of 🤖)
- The "Playing on" status
- Device identification in Discord's API

## Requirements

- Python 3.8+
- discord.py 2.0.0+

## License

MIT License - feel free to use this in your projects!

## Credits

Created by **B3nderServices**

## Support

For issues, questions, or contributions, please visit:
https://github.com/B3nderServices/DiscordiOS

---


⭐ If you like this project, please give it a star on GitHub!
