import discord
import random
from discord.ext import commands
import os
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)



@bot.command()
async def info(ctx):
    embed = discord.Embed( 
        title="**WarmPlanet🌍** | Команды бота", 
        description="Команды для основного использования.", 
        color= discord.Color.blue ()  
    ) 
    embed.add_field( 
    name="Глобальное потепление", 
    value="Команда - !globalwarm. Информация о глобальном потеплении и информация о причинах.", 
    inline=False  
    ) 
    embed.add_field( 
    name="Переработка мусора", 
    value="Команда - !recycle. Информация о переработке мусора, видах мусора и вредности.", 
    inline=False  
    ) 
    embed.add_field( 
    name="Прчиины глобального потепления", 
    value="Команда - !reasons. Причины глобального потепления, изменения климата, факты.", 
    inline=False  
    ) 
    embed.add_field( 
    name="Прчиины глобального потепления", 
    value="Команда - !randomfact. Рандомный факт о глобальном потеплении.", 
    inline=False  
    ) 
    embed.add_field( 
    name="Последствия", 
    value="Команда - !consequences. Последствия глобального потепления если его игнорировать.", 
    inline=False  
    ) 
    embed.add_field( 
    name="О боте", 
    value="Команда - !botinfo. Информация о самом боте, идее, авторе", 
    inline=False  
    ) 
    embed.set_image(url="https://i.imgur.com/5tgGSQR.png")
    await ctx.send(embed=embed) 

@bot.command()
async def globalwarm(ctx):
    embed = discord.Embed(
        title="**WarmPlanet🌍** | Глобальное потепление",
        description="Информация о глобальном потеплении и его последствиях.",
        color=discord.Color.orange()
    )

    embed.add_field(name="Насколько эта проблема серьезна?", 
                    value="Глобальное потепление является одной из самых серьезных проблем современности. "
                          "Оно влияет на климатические условия, экосистемы и жизнь людей по всему миру. "
                          "Неотложные меры необходимы, чтобы предотвратить необратимые изменения в окружающей среде.",
                    inline=False)

    embed.add_field(name="Что провоцирует глобальное потепление?", 
                    value="Основные причины глобального потепления включают:"
                          "- Выбросы парниковых газов, таких как углекислый газ (CO2) и метан (CH4), "
                          "в результате сжигания ископаемых видов топлива."
                          "- Вырубка лесов, что уменьшает количество деревьев, поглощающих CO2."
                          "- Промышленное производство и сельское хозяйство, которые также выделяют парниковые газы.",
                    inline=False)

    embed.add_field(name="Как мы можем сдерживать глобальное потепление?", 
                    value="Мы можем сдерживать глобальное потепление следующими способами:"
                          "- Переход на возобновляемые источники энергии, такие как солнечная и ветровая энергия."
                          "- Снижение потребления энергии и улучшение энергоэффективности."
                          "- Увеличение лесных насаждений и сохранение экосистем."
                          "- Развитие устойчивых методов сельского хозяйства и сокращение отходов.",
                    inline=False)

    embed.add_field(name="Последствия глобального потепления:", 
                    value="Глобальное потепление приводит к:"
                          "- Изменению климата и увеличению частоты экстремальных погодных условий."
                          "- Таянию ледников и повышению уровня моря, что угрожает прибрежным регионам."
                          "- Ухудшению качества воздуха и здоровья людей."
                          "- Потере биоразнообразия и угрозе многим видам животных и растений.",
                    inline=False)
    embed.set_image(url="https://i.imgur.com/euK4CkH.png")
    await ctx.send(embed=embed)
@bot.command()
async def botinfo(ctx):
    embed = discord.Embed( 
        title="**WarmPlanet🌍** | Информация о боте", 
        description='''Данный бот был создан по идее борьбе с глобальным потеплением, причинами, и способами избежать такой ситуации.

        Бот имеет несоклько команд которые напрямую связаны с известной проблемой, первая, основная команда **!globalwarm** которая дает информацию и факты о глобальном потеплении, следом идут команды **!reasons** и **!recycle**, **!consequences**

        Данные команды несут немало важную роль ведь указывают на причины и переработку мусора
        
        Версия бота: 0.0.1
        Автор: @.soulrifter (Discord)''', 
        color= discord.Color.blue ()
        
    )
    embed.set_image(url="https://i.imgur.com/WgfQvfd.png")
    
    await ctx.send(embed=embed) 

@bot.command()
async def recycle(ctx):
    embed = discord.Embed( 
        title="**WarmPlanet🌍** | Переработка мусора", 
        description="Список всех доступных команд для информации переработки мусора.", 
        color= discord.Color.blue ()
    ) 
    embed.add_field( 
    name="Переработка пластика", 
    value="Команда - !plastic. Информация о вреде мусора пластика, о переработке и пользе переработки", 
    inline=False  
    ) 
    embed.add_field( 
    name="Переработка стекла", 
    value="Команда - !glass. Информация о вреде мусора стекла, переработке и её переработки", 
    inline=False  
    ) 
    
    embed.set_image(url="https://i.imgur.com/MrhmKef.png")
    await ctx.send(embed=embed)

@bot.command()
async def plastic(ctx):
    embed = discord.Embed(
        title="**WarmPlanet🌍** | Переработка пластика",
        description="Способы переработки пластика и его преимущества.",
        color=discord.Color.green()
    )

    embed.add_field(name="Способы переработки пластика:", 
                    value="1. **Механическая переработка:** Пластик дробится, очищается и плавится для создания новых изделий."
                          "2. **Химическая переработка:** Пластик разлагается на мономеры, которые затем используются для создания нового пластика."
                          "3. **Пиролиз:** Пластик нагревается без доступа кислорода, что позволяет получить масла и газы, которые можно использовать как топливо или сырье для производства химических продуктов."
                          "4. **Биологическая переработка:** Используются микроорганизмы для разложения пластика на более простые компоненты.",
                    inline=False)

    embed.add_field(name="Преимущества переработки пластика:", 
                    value="1. **Снижение объема отходов:** Помогает сократить количество пластиковых отходов, попадающих на свалки или в окружающую среду."
                          "2. **Экономия ресурсов:** Переработка пластика позволяет сэкономить энергию и сырье, которые иначе были бы использованы для производства нового пластика."
                          "3. **Снижение загрязнения окружающей среды:** Помогает сократить загрязнение воды, почвы и воздуха от пластиковых отходов."
                          "4. **Создание новых рабочих мест:** Процесс переработки пластика требует рабочей силы, что способствует созданию новых рабочих мест.",
                    inline=False)
    embed.set_image(url="https://i.imgur.com/U6iB0Jr.jpeg")
    await ctx.send(embed=embed)

@bot.command()
async def consequences(ctx):
    embed = discord.Embed(
        title="Последствия глобального потепления",
        color=discord.Color.red()
    )

    # Последствия с изображениями и текстом
    embed.add_field(
        name="Повышение уровня моря",
        value="Угрожает прибрежным регионам и островам.",
        inline=False
    )

    embed.add_field(
        name="Экстремальные погодные условия",
        value="Более частые и интенсивные ураганы, наводнения и засухи.",
        inline=False
    )

    embed.add_field(
        name="Потеря биоразнообразия",
        value="Изменения климата угрожают многим видам животных и растений.",
        inline=False
    )

    embed.add_field(
        name="Ухудшение здоровья",
        value="Увеличивается риск заболеваний и тепловых ударов.",
        inline=False
    )

    embed.add_field(
        name="Продовольственная безопасность",
        value="Снижение урожайности из-за изменения климата.",
        inline=False
    )

    embed.add_field(
        name="Таяние вечной мерзлоты",
        value="Высвобождение CO2 и метана, что ускоряет потепление.",
        inline=False
    )

    embed.add_field(
        name="Засухи и дефицит воды",
        value="В некоторых регионах ухудшается доступ к воде.",
        inline=False
    )

    embed.add_field(
        name="Повышение кислотности океанов",
        value="Угроза для морских экосистем.",
        inline=False
    )

    embed.add_field(
        name="Экономические потери",
        value="Разрушение инфраструктуры и снижение производительности.",
        inline=False
    )
    embed.set_image(url="https://www.inesnet.ru/wp-content/uploads/2022/06/img08062022.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def randomfact(ctx):
    facts = [
        "Средняя глобальная температура Земли увеличилась примерно на 1,2°C с конца 19 века.",
        "Уровень углекислого газа (CO2) в атмосфере сейчас выше, чем за последние 800,000 лет.",
        "Ледники в Гренландии и Антарктиде теряют массу быстрее, чем когда-либо ранее.",
        "Уровень моря поднимается примерно на 3.3 мм в год из-за таяния льда и теплового расширения океанов.",
        "Увеличивается частота и интенсивность экстремальных погодных явлений, таких как ураганы и наводнения.",
        "Около 30% CO2, выбрасываемого в атмосферу, поглощается океанами, что приводит к их кислотности.",
        "Глобальное потепление угрожает множеству видов животных и растений, создавая риск вымирания.",
        "Изменение климата может снизить урожайность некоторых сельскохозяйственных культур, таких как пшеница и кукуруза.",
        "Глобальное потепление может повлиять на здоровье человека, увеличивая риски инфекционных заболеваний и ухудшая качество воздуха.",
        "Экономические потери от изменений климата могут достигнуть сотен миллиардов долларов в год.",
        "Проблемы с продовольственной безопасностью возрастают из-за изменения климата и экосистем.",
        "Таяние вечной мерзлоты может высвобождать парниковые газы, что усугубляет потепление.",
        "Глобальное потепление влияет на миграцию и поведение многих животных.",
        "Сохранение лесов является важным шагом в борьбе с глобальным потеплением.",
        "Температура океанов продолжает расти, что влияет на морские экосистемы.",
        "В некоторых регионах происходит увеличение засух и ухудшение условий для жизни.",
        "По данным ООН, более 70% углерода, выбрасываемого в атмосферу, связано с деятельностью человека.",
        "Климатические изменения могут вызвать изменения в распространении инфекционных заболеваний.",
        "Подъем уровня моря угрожает прибрежным городам и экосистемам.",
        "Люди могут снижать свои выбросы углерода, используя общественный транспорт и велосипед.",
        "Энергетическая эффективность зданий может значительно сократить потребление энергии."
    ]

    # Выбираем случайный факт
    random_fact = random.choice(facts)

    # Отправляем случайный факт
    await ctx.send(random_fact)

@bot.command()
async def glass(ctx):
    embed = discord.Embed(
        title="**WarmPlanet🌍** | Переработка стекла",
        description="Способы переработки стекла и его преимущества.",
        color=discord.Color.green()
    )

    embed.add_field(name="Способы переработки стекла:", 
                    value="1. **Дробление:** Стекло дробится на мелкие кусочки, которые затем могут быть использованы для создания нового стекла или других продуктов."
                          "2. **Плавление:** Дробленное стекло плавится и формуется в новые изделия, такие как бутылки, оконные стекла и стеклянные украшения."
                          "3. **Использование в дорожном строительстве:** Дробленное стекло может использоваться в качестве заполнителя в асфальте или бетоне."
                          "4. **Изготовление декоративных изделий:** Стекло может быть переработано в декоративные элементы, такие как плитка, мозаика или скульптуры.",
                    inline=False)

    embed.add_field(name="Преимущества переработки стекла:", 
                    value="1. **Экономия энергии:** Переработка стекла требует меньше энергии, чем производство нового стекла из сырья."
                          "2. **Сохранение природных ресурсов:** Переработка стекла позволяет сэкономить природные ресурсы, так как не требуется использование новых сырьевых материалов."
                          "3. **Сокращение отходов:** Переработка стекла помогает снизить объем отходов, попадающих на свалки, и уменьшить загрязнение окружающей среды."
                          "4. **Уменьшение выбросов парниковых газов:** Изготовление стекла из переработанного стекла требует меньше энергии и, следовательно, снижает выбросы парниковых газов в атмосферу.",
                    inline=False)
    embed.set_image(url="https://i.imgur.com/YqABUnA.jpeg") 
    await ctx.send(embed=embed)

bot.run("NOTHING") 



