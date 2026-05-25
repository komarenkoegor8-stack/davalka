import discord
from discord.ext import commands

# Включаем необходимые разрешения (Intents)
# Важно: GUILD_MEMBERS обязательно нужно включить и в панели разработчика Discord!
intents = discord.Intents.default()
intents.members = True  

bot = commands.Bot(command_prefix="!", intents=intents)

# Имя или ID роли, которую нужно выдавать автоматом
ROLE_NAME_OR_ID = "Member"  # Замените на название вашей роли

@bot.event
async def on_ready():
    print(f"Бот {bot.user.name} успешно запущен и готов к работе!")

@bot.event
async def on_member_join(member):
    # Пытаемся найти роль на сервере по имени или ID
    guild = member.guild
    role = discord.utils.get(guild.roles, name=ROLE_NAME_OR_ID)
    
    # Если роль по имени не найдена, пробуем найти по ID (если вы указали цифры)
    if not role and ROLE_NAME_OR_ID.isdigit():
        role = guild.get_role(int(ROLE_NAME_OR_ID))

    if role:
        try:
            await member.add_roles(role)
            print(f"Роль '{role.name}' успешно выдана пользователю {member.name}")
        except discord.Forbidden:
            print(f"Ошибка: У бота нет прав для выдачи роли '{role.name}'. Передвиньте роль бота выше в списке ролей.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
    else:
        print(f"Ошибка: Роль '{ROLE_NAME_OR_ID}' не найдена на сервере '{guild.name}'.")

# Сюда нужно вставить токен вашего бота
bot.run("ВАШ_ТОКЕН_БОТА_СЮДА")
